#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "772083660484780032-KJ0DHZ535tA9KSXKp7gOLkLh5jUm5zF"
access_token_secret = "zaUC6TracMsfFKXSJyuvIox8YUXl1aTkIvnk2HsBIKR9V"
consumer_key = "JlapdjTbD5x988S6K8O8oHUlk"
consumer_secret = "rxYBSHX44Drskh1vhwTzoRTegs33yEgbgusURfOakRjUenH6JE"

import tweepy

auth = tweepy.OAuthHandler("JlapdjTbD5x988S6K8O8oHUlk", "rxYBSHX44Drskh1vhwTzoRTegs33yEgbgusURfOakRjUenH6JE")
auth.set_access_token("zaUC6TracMsfFKXSJyuvIox8YUXl1aTkIvnk2HsBIKR9V", "772083660484780032-KJ0DHZ535tA9KSXKp7gOLkLh5jUm5zF")

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text