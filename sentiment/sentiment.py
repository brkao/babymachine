import praw
import sys
import json
from json import encoder
encoder.FLOAT_REPR = lambda o: format(o, '.2f')

import redis
import os
from data import *
import time
import pandas as pd
#import matplotlib.pyplot as plt
#import squarify
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

print("Starting Sentiment bot")
sys.stdout.flush()
os.environ["TZ"]="US/Eastern"
time.tzset()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

reddit = praw.Reddit(user_agent="bigbrainbaby:collector",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    username=USERNAME,
    password=PASSWORD)


'''############################################################################'''
# set the program parameters

#how much time to sleep between each harvest, in seconds
interval = 45 * 60

# sub-reddit to search
subs = ['wallstreetbets', 'stocks', 'investing', 'stockmarket', 'TrailerParkBets']
#subs = ['stocks']
#subs = ['TrailerParkBets']


# posts flairs to search || None flair is automatically considered
post_flairs = {'DD',
               'YOLO',
               'Company Discussion',
               'Daily Discussion',
               'Weekend Discussion',
               'Discussion',
               'Company Analysis',
               'Company News',
               'ETFs',
               'Technical Analysis',
               'Fundamentals/DD'
               }

# authors whom comments are allowed more than once
goodAuth = {'AutoModerator'}

# allow one comment per author per symbol
uniqueCmt = True

# authors to ignore for posts
ignoreAuthP = {'example'}

# authors to ignore for comment
ignoreAuthC = {'example'}

# upvote ratio for post to be considered, 0.70 = 70%
upvoteRatio = 0.50

# number of upvotes required for a post to be considered
ups = 5

# define the limit, comments 'replace more' limit, this is the
# number of iterations that the comment replace more will be called
limit = 150

# number of upvotes required for a comment to be considered
upvotes = 2

# define # of picks here, prints as "Top ## picks are:"
# not current used since only sentiment is stored in redis
picks = 30

# define # of picks for sentiment analysis
# this is the number of stock symbols that sentiment analysis will run on
picks_ayz = 30
'''############################################################################'''

def harvest():
    import time
    start_time = time.time()
    posts, count, c_analyzed, tickers, titles, a_comments = 0, 0, 0, {}, [], {}
    cmt_auth = {}

    for sub in subs:
        subreddit = reddit.subreddit(sub)
        hot_python = subreddit.hot()    # sorting posts by hot

        print("Harvesting /r/%s" % sub)
        sys.stdout.flush()

        submission_count = 0
        # Extracting comments, symbols from subreddit
        for submission in hot_python:
            submission_count += 1
            flair = submission.link_flair_text
            author = submission.author.name
            # checking: post upvote ratio # of upvotes, post flair, and author
            if submission.upvote_ratio >= upvoteRatio and submission.ups > ups and (flair in post_flairs or flair is None) and author not in ignoreAuthP:
                submission.comment_sort = 'new'
                comments = submission.comments
                titles.append(submission.title)
                posts += 1
                submission.comments.replace_more(limit=limit)
                for comment in comments:
                    # try except for deleted account?
                    try: auth = comment.author.name
                    except: pass
                    c_analyzed += 1

                    # checking: comment upvotes and author
                    if comment.score > upvotes and auth not in ignoreAuthC:
                        split = comment.body.split(" ")
                        for word in split:
                            word = word.replace("$", "")
                            # upper = ticker, length of ticker <= 5, excluded words,
                            if word.isupper() and len(word) <= 5 and word not in blacklist and word in us:

                                # unique comments, try/except for key errors
                                if uniqueCmt and auth not in goodAuth:
                                    try:
                                        if auth in cmt_auth[word]: break
                                    except: pass

                                # counting tickers
                                if word in tickers:
                                    tickers[word] += 1
                                    a_comments[word].append(comment.body)
                                    cmt_auth[word].append(auth)
                                    count += 1
                                else:
                                    tickers[word] = 1
                                    cmt_auth[word] = [auth]
                                    a_comments[word] = [comment.body]
                                    count += 1


    print("Done Harvesting...")
    sys.stdout.flush()

    # sorts the dictionary
    symbols = dict(sorted(tickers.items(), key=lambda item: item[1], reverse = True))
    top_picks = list(symbols.keys())[0:picks]
    time_elapsed = (time.time() - start_time)

    # print top picks
    print("It took {t:.2f} seconds to analyze {c} comments in {p} posts in {s} subreddits.\n".format(t=time_elapsed, c=c_analyzed, p=posts, s=len(subs)))
    sys.stdout.flush()
    #print("Posts analyzed saved in titles")
    #for i in titles: print(i)  # prints the title of the posts analyzed

    #print(f"\n{picks} most mentioned picks: ")
    #times = []
    #top = []
    #for i in top_picks:
    #    print(f"{i}: {symbols[i]}")
    #    times.append(symbols[i])
    #    top.append(f"{i}: {symbols[i]}")

    # Applying Sentiment Analysis
    scores, s = {}, {}

    vader = SentimentIntensityAnalyzer()
    # adding custom words from data.py
    vader.lexicon.update(new_words)

    picks_sentiment = list(symbols.keys())[0:picks_ayz]
    for symbol in picks_sentiment:
        stock_comments = a_comments[symbol]

        for cmnt in stock_comments:
            score = vader.polarity_scores(cmnt)
            if symbol in s:
                s[symbol][cmnt] = score
            else:
                s[symbol] = {cmnt:score}
            if symbol in scores:
                for key, _ in score.items():
                    scores[symbol][key] += score[key]
            else:
                scores[symbol] = score

        # calculating avg.
        for key in score:
            scores[symbol][key] = scores[symbol][key] / symbols[symbol]
            #scores[symbol][key]  = "{pol:.3f}".format(pol=scores[symbol][key])
        #print(symbols[symbol])
        scores[symbol]['count'] = symbols[symbol]

    sortedscores = dict(sorted(scores.items(), key=lambda item: item[1]['count'], reverse = True))
    # printing sentiment analysis
    #print(f"\nSentiment analysis of top {picks_ayz} picks:")
    #df = pd.DataFrame(scores)
    #df.index = ['Bearish', 'Neutral', 'Bullish', 'Total']
    #df = df.T
    #print(df.to_json())

    d = {"timestamp" : time.strftime("%m-%d-%Y %T %Z", time.localtime(time.time()))}
    d["tickers"] = sortedscores

    r = redis.from_url(os.environ.get("REDIS_URL"))
    r.lpush("sentiment_scores", json.dumps(d))
    r.ltrim("sentiment_scores", 0, 99)
    print("Stored to REDIS")
    sys.stdout.flush()

while True:
    harvest()
    print("Sleep")
    sys.stdout.flush()
    time.sleep(interval)

# Date Visualization
# most mentioned picks
#squarify.plot(sizes=times, label=top, alpha=.7 )
#plt.axis('off')
#plt.title(f"{picks} most mentioned picks")
#plt.show()

# Sentiment analysis
#df = df.astype(float)
#colors = ['red', 'springgreen', 'forestgreen', 'coral']
#df.plot(kind = 'bar', color=colors, title=f"Sentiment analysis of top {picks_ayz} picks:")
#plt.show()
