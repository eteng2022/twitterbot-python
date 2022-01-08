# import dependencies
import tweepy

# create new class "StreamListener" 
# takes in tweepy.StreamListener as a parameter
class StreamListener(tweepy.Stream):
  def __init__(self, apikey, apisecret, accesstoken, accesssecret, api, arr):
    super().__init__(apikey, apisecret, accesstoken, accesssecret)
    self.api = api
    self.me = api.verify_credentials()
    self.arr = arr
  
  # the function containing the logic on what to do for each tweet
  def on_status(self, tweet):
    # We only want the bot to retweet original tweets, not replies.
    # We also don't want the bot to retweet itself
    if tweet.user.id == self.me.id or hasattr(tweet, 'retweeted_status'):
      print("skip rts or own tweet")
      return
    
    # don't retweet if keywords are not directly found in text
    found = False
    for s in arr:
        found = found or s in tweet.text
    if not found:
        print("keyword not found")
        return
    
    # If we haven't retweeted this tweet yet, retweet it   
    if not tweet.retweeted:
      try: 
        print(f"the current tweet is {tweet.text} by {tweet.user.screen_name}")
        self.api.retweet(tweet.id)
        print("Tweet retweeted successfully")
      except Exception as e:
        print(e)
  # the function containing the logic in case there is an error  
  def on_error(self, status):
    print(f"Error while retweeting: {status}")