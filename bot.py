# import dependencies
import tweepy
import os
from dotenv import load_dotenv
from streamlistener import StreamListener

# load our .env file to make use of the environment variables
load_dotenv()

# import and assign our environment variables
API_KEY = os.getenv('twitter_api_key')
API_SECRET = os.getenv('twitter_api_secret')
ACCESS_TOKEN = os.getenv('twitter_access_token')
ACCESS_SECRET = os.getenv('twitter_access_token_secret')

# instantiate oauth handler and set access token
oauth = tweepy.OAuthHandler(API_KEY, API_SECRET)
oauth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# instantiate tweepy api object using the authentication handler object
api = tweepy.API(oauth, wait_on_rate_limit=True)

# attempt credential verification
user = api.verify_credentials()
print(f"Successfully logged into {user.screen_name}")

# create instance of StreamListener
keywords = ["tweepy", "#elasticbeanstalk"] # add any keywords and hashtags you want to track
users = ["UCBerkeley", "SpaceLiminalBot", "RabbitEveryHour"] # add the @s of users you want to track
userids = [api.get_user(screen_name=name).id for name in users]
print(f"searching for tweets with keywords {keywords} and from users {users}")
streamlistener = StreamListener(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET, api, keywords, userids)
streamlistener.filter(follow=userids, track=keywords)
