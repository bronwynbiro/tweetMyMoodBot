#Import the necessary methods from tweepy library
from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import creds
import json

#Variables that contains the user credentials to access Twitter API
access_token = creds.accessToken
access_token_secret = creds.accessTokenSecret
consumer_key = creds.consumerKey
consumer_secret = creds.consumerSecret

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        if 'RT' not in json.loads(data)['text'] and '@' not in json.loads(data)['text'] and json.loads(data)['lang'] == 'en' and 'http' not in json.loads(data)['text']:
            print json.loads(data)['text']
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords
    #stream.filter(track=['angry', 'frustrated', '#annoyed', '#sodone', '#overit', '#pissed', 'idiots'])
    #stream.filter(track=['happy', 'thankful', 'happiness', 'joyful', 'joy', 'excited', 'elated', 'thrilled', 'stoked'])
    #stream.filter(track=['surprised', 'cant believe', 'shocked', 'unbelievable'])
    #stream.filter(track = ['disgusted', 'disgusting', 'gross', 'revolting'])
    stream.filter(track = ['fear', 'scared', 'scary', 'nervous', 'fearing'])
