# import dependencies
import tweepy
import os
from dotenv import load_dotenv
from time import sleep
from streamlistener import StreamListener

# load our .env file to make use of the environment variables
load_dotenv()

# import and assign our environment variables
API_KEY = os.getenv('twitter_api_key')
API_SECRET = os.getenv('twitter_api_secret')
ACCESS_TOKEN = os.getenv('twitter_access_token')
TOKEN_SECRET = os.getenv('twitter_access_token_secret')

# instantiate oauth handler and set access token
twitter_oauth = tweepy.OAuthHandler(API_KEY, API_SECRET)
twitter_oauth.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)

# instantiate tweepy api object using the authentication handler object
twitter_api = tweepy.API(twitter_oauth, wait_on_rate_limit=True)

# attempt credential verification
id = twitter_api.verify_credentials().id
print(id)
print("Successfully logged in")

# twtcount = 0
# for tweet in twitter_api.search_30_day(label="dev", query="zhengting"):
#     if not hasattr(tweet, 'retweeted_status') and tweet.user.id != id:
#         print(f"NEXT TWEET: {tweet.text}")
#         twtcount += 1
#         try:
#             tweet.retweet()
#             print("Retweeted!")
#         except tweepy.TweepyException as e:
#             print(e)
#         sleep(5)
#     if twtcount > 40:
#         break

arr = ["zhuzhengting", "zhengting", "朱正廷"]
# streamlistener = StreamListener(API_KEY, API_SECRET, ACCESS_TOKEN, TOKEN_SECRET, twitter_api, arr)
# streamlistener.filter(track=arr)
found = False
for s in arr:
    found = found or s in twitter_api.get_status(1478867333427134466).text.lower()
    print(f"check if {s} is found in {twitter_api.get_status(1478867333427134466).text.lower()}: {found}")
print(found)
print("朱正廷" in "朱正廷《信尔》(动画第一季官方授权音乐专辑概念曲) https://t.co/zdDjBxuPwb… @QQ音乐".lower())
newfound = False
for s in arr:
    newfound = newfound or s in twitter_api.get_status(1478730582398050304).text.lower()
    print(f"check if {s} is found in {twitter_api.get_status(1478730582398050304).text.lower()}: {newfound}")

print(hasattr(twitter_api.get_status(1478867333427134466), 'quoted_status'))
print(hasattr(twitter_api.get_status(1478730582398050304), 'quoted_status'))