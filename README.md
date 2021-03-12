# babymachine
----------------
Babymachine is the engine that performs the following tasks:
- Produce and store the movement velocity of reddit posts of /r/wallstreetbets
- Produce and store the user sentiment of all stocks mentioned from users meeting the following criteria
  Top mentions and sentiment analysis from COMMENTS every 45 minutes from:
    /r/wallstreetbets
    /r/stocks
    /r/investing
    /r/stockmarket
    /t/TrailerParkBets
    
  Current parameter:
    Only comments from posts that meet following criteria are considered.
    Posts that are considerd 'HOT' e.g. /r/wallstreetbets/hot
    Post Up vote ratio must be above .5 and has at least 5 up votes
    Posts with the following flairs OR without any flairs
      {'DD', 'YOLO', 'Company Discussion', 'Daily Discussion', 'Weekend Discussion', 'Discussion'}
    Each user only count ONCE per Symbol
    Comments of the post must have at least 2 up votes
    
The velocity builder is implemented in Go and the sentiment tracker is in Python for its easy to use natural language processing libraries.

The computation results are stored in Redis.

This repository includes deployement specifications for automatic deployment into Heroku Cloud.
