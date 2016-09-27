#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import sys

#Variables that contains the user credentials to access Twitter API 
access_token = "772083660484780032-KJ0DHZ535tA9KSXKp7gOLkLh5jUm5zF"
access_token_secret = "zaUC6TracMsfFKXSJyuvIox8YUXl1aTkIvnk2HsBIKR9V"
consumer_key = "JlapdjTbD5x988S6K8O8oHUlk"
consumer_secret = "rxYBSHX44Drskh1vhwTzoRTegs33yEgbgusURfOakRjUenH6JE"


access_tokenPM = "166860232-E7XDQFvUrqan4TT5T6JFfpPoUctPnXesXdmTPnth"
access_token_secretPM = "60IizseD6AYQu7Azyu8OOsAJsMuO1KfHo2sUwP3LSBxsI"
consumer_keyPM = "zKoQbJOhJr91wFCV5UTiQLI64"
consumer_secretPM = "BEOx061eFPn1QhWqjN3vGKcBR5sR51Go2auiaPz5dAnPwsK3Bo"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        timeLimit = 9000
        if (time.time() - startTime) < timeLimit:
            print data
        else:
            #print "End of Stream"
            sys.exit()
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    timeLimit = 9000
    startTime = time.time()
    l = StdOutListener()
    auth = OAuthHandler(consumer_keyPM, consumer_secretPM)
    auth.set_access_token(access_tokenPM, access_token_secretPM)
    stream = Stream(auth, l)

        #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Trump\'s','Trump','Donald Trump\'s','Donald Trump', 'republican nominee', 'rep nom'])

   
