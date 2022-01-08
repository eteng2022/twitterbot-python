# import dependencies
import tweepy

# create new class that takes in tweepy.Stream as a parameter
class StreamListener(tweepy.Stream):
  def __init__(self, apikey, apisecret, accesstoken, accesssecret, api):
    super().__init__(apikey, apisecret, accesstoken, accesssecret)
    self.api = api
    self.me = api.verify_credentials()
  
  # the function containing the logic on what to do for each tweet
  def on_status(self, tweet):
    # bot will not retweet itself or already retweeted tweets
    # bot will only retweet original tweets
    if tweet.retweeted or tweet.user.id == self.me.id or hasattr(tweet, 'retweeted_status'):
      print("skip retweet or own tweet")
      return
    
    # functionality that retweets and likes the current tweet
    try: 
      print(f"the current tweet is {tweet.text} by {tweet.user.screen_name}")
      self.api.create_favorite(tweet.id)
      print("tweet liked successfully")
      self.api.retweet(tweet.id)
      print("tweet retweeted successfully")
    except Exception as e:
      print(e)
