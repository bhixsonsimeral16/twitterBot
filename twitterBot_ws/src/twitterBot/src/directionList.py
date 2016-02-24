import tweepy
import json
import string
from listTest import *
from heapq import *

consumer_key = "E6uJ66Idggzd2ztGxyHhyzs3q"
consumer_secret = "5CwZpFz9gzeOLzOX08Byp1fxweoGJ3NuwUT6E0DwPN5l2dI3oX"
access_token = "700398196724400129-wZXwo1uL7sERuxa4e3LIxVQW6o3kps2"
access_token_secret = "kc8Dm2oYE511qIGU4Btg1Szn37zdE9H9QhyTimCh6ULgW"

dictionary = [" forward ", " backward ", " left ", " right "]
handle = "@turtlebot"

#list of directions
directionList = []

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        global directionList
        # Twitter returns data in JSON format - we need to decode it first
        tweet = json.loads(data)
        tweetText = ('{0}'.format(tweet['text'].encode('ascii', 'ignore'))).lower()
        tweetText = tweetText.translate(string.maketrans("",""), string.punctuation)
        tweetText = " " + tweetText + " "

        print tweetText

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        #print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        for data in dictionary:
            if (data) in tweetText:
                print '@{0}: {1}'.format(tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore'))
                data = data.strip()
                directionList.append(data)
                print (directionList)
                return directionList
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = tweepy.Stream(auth, StdOutListener())

    stream.filter(track=[handle])
