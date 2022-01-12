# twitterbot-python
Simple twitter bot that automatically retweets and likes tweets from a list of keywords and users in real-time. Uses the [Tweepy](https://docs.tweepy.org/en/stable/) library to access the Twitter API. Functionality can be modified or expanded upon for the purposes of the account.

## Getting started

Clone the repo and install the following dependencies:
```
pip install tweepy
pip install python-dotenv
```
Alternately, you can use a virtual environment and install from `requirements.txt`:
```
pip install -r requirements.txt
```
The python-dotenv module will be used to store environment variables, namely the API keys unique to your Twitter account. Create a file named ```.env``` in the base directory of the project with this format:
```
twitter_api_key=<YOUR API KEY HERE>
twitter_api_secret=<YOUR API SECRET KEY HERE>
twitter_access_token=<YOUR ACCESS TOKEN HERE>
twitter_access_token_secret=<YOUR ACCESS SECRET HERE>
```
The next step will be to generate your secret keys.

## Account setup
First, sign up for a new Twitter account for your bot. To utilize the Twitter API, you will need a developer account where you can create a new project and generate your API keys. [Apply here](https://developer.twitter.com/en) (while logged into your bot account) and click "Create New Project" in the dashboard. Copy your **API key** and **API secret key** into the .env file. 

Next, you should see your project and app in the menu on the left side of the screen. Go to your app settings and make sure that the app has read and write permissions. Then, go to "Keys and tokens" and generate your **access token** and **access secret**; copy these into the .env file as well.

## Usage
Modify the keywords and users tracked by the bot in ```bot.py``` and the functionality of the bot in ```streamlistener.py```. The bot uses an instance of tweepy's ```Stream``` class whose documentation can be found [here](https://docs.tweepy.org/en/stable/stream.html).

With your API keys and any required dependencies installed, you can run the bot like so:
```
python bot.py
```
To run the bot continuously, consider running your script using a cron job or on an online server!
