import tweepy
import json

consumer_key = "E6uJ66Idggzd2ztGxyHhyzs3q"
consumer_secret = "5CwZpFz9gzeOLzOX08Byp1fxweoGJ3NuwUT6E0DwPN5l2dI3oX"
access_token = "700398196724400129-wZXwo1uL7sERuxa4e3LIxVQW6o3kps2"
access_token_secret = "kc8Dm2oYE511qIGU4Btg1Szn37zdE9H9QhyTimCh6ULgW"

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        #print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        if ("forward" or "backward" or "left" or "right") in ('%s' % (decoded['text'].encode('ascii', 'ignore'))).lower():
            print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        print ''
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = tweepy.Stream(auth, l)
    #stream.filter(track=['@turtlebot'])
    stream.filter(track=['@turtlebot'])
