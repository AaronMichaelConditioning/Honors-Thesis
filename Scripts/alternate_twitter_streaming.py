#Import the necessary methods from tweepy library

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "772083660484780032-KJ0DHZ535tA9KSXKp7gOLkLh5jUm5zF"
access_token_secret = "zaUC6TracMsfFKXSJyuvIox8YUXl1aTkIvnk2HsBIKR9V"
consumer_key = "JlapdjTbD5x988S6K8O8oHUlk"
consumer_secret = "rxYBSHX44Drskh1vhwTzoRTegs33yEgbgusURfOakRjUenH6JE"

import
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['@realDonaldTrump', '@HillaryClinton'])

