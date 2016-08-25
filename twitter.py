import sys
sys.path.append('/usr/local/lib/python2.7/site-packages/')
import tweepy, creds, time, sys

auth = tweepy.OAuthHandler(creds.consumerKey, creds.consumerSecret)
auth.set_access_token(creds.accessToken, creds.accessTokenSecret)
api = tweepy.API(auth)


def postTweet(tweet):
    status = api.update_status(status=tweet)


def updateDescription(about):
    api.update_profile(description=about)
