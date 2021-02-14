import praw
import sys
import json
import redis
import os
from data import *
import time
import pandas as pd
#import matplotlib.pyplot as plt
#import squarify
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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
#subs = ['wallstreetbets', 'stocks', 'investing', 'stockmarket']     # sub-reddit to search
subs = ['TrailerParkBets']     # sub-reddit to search
#post_flairs = {'Daily Discussion', 'Weekend Discussion', 'Discussion'}    # posts flairs to search || None flair is automatically considered
post_flairs = {}    # posts flairs to search || None flair is automatically considered
goodAuth = {'AutoModerator'}   # authors whom comments are allowed more than once
uniqueCmt = True                # allow one comment per author per symbol
ignoreAuthP = {'example'}       # authors to ignore for posts
ignoreAuthC = {'example'}       # authors to ignore for comment
upvoteRatio = 0.00         # upvote ratio for post to be considered, 0.70 = 70%
ups = 0       # define # of upvotes, post is considered if upvotes exceed this #
limit = 100      # define the limit, comments 'replace more' limit
upvotes = 0     # define # of upvotes, comment is considered if upvotes exceed this #
picks = 10     # define # of picks here, prints as "Top ## picks are:"
picks_ayz = 5   # define # of picks for sentiment analysis
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

    # sorts the dictionary
    symbols = dict(sorted(tickers.items(), key=lambda item: item[1], reverse = True))
    top_picks = list(symbols.keys())[0:picks]
    time_elapsed = (time.time() - start_time)

    # print top picks
    print("It took {t:.2f} seconds to analyze {c} comments in {p} posts in {s} subreddits.\n".format(t=time_elapsed, c=c_analyzed, p=posts, s=len(subs)))
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
            scores[symbol][key]  = "{pol:.3f}".format(pol=scores[symbol][key])

    # printing sentiment analysis
    #print(f"\nSentiment analysis of top {picks_ayz} picks:")
    #df = pd.DataFrame(scores)
    #df.index = ['Bearish', 'Neutral', 'Bullish', 'Total']
    #df = df.T
    #print(df.to_json())

    d = [time.asctime(time.localtime(time.time())), scores]

    r = redis.Redis()
    r.lpush("scores", json.dumps(d))
    r.ltrim("scores", 0, 99)

while True:
    harvest()
    print("Sleep")
    sys.stdout.flush()
    time.sleep(10)

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