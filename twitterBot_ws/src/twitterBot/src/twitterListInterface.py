#!/usr/bin/env python

# Every python controller needs these lines
import roslib; roslib.load_manifest('lab1')
import rospy

#imports for twitter API
import tweepy
import json
import string
from heapq import *

#String and Time
from std_msgs.msg import String
from std_msgs.msg import Time

def pulledKeyword(heap, keyword):
    if (len(heap) != 0 and (keyword in (zip(*heap)[1]))):
        #print (heap[zip(*heap)[1].index(keyword)][0])
        heap[zip(*heap)[1].index(keyword)][0] += 1
        #print (heap[zip(*heap)[1].index(keyword)][0])
        # if ((nlargest(1, heap)[1] == keyword) & (heap[zip(*heap)[1].index(keyword)][0]) > (10 + heap[zip(*heap)[1].index(prevGoal)][0])):
        #     ## make a call to change the goal
        #     ## this may be difficult...
        #     ## return is for setting the currentGoal
        #     return (nlargest(1, heap)[1])
    else:
        lst = [1, keyword]
        heappush (heap, lst)
    return heap

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        global directionList
        # Twitter returns data in JSON format - we need to decode it first
        tweet = json.loads(data)
        tweetText = ('{0}'.format(tweet['text'].encode('ascii', 'ignore'))).lower()
        tweetText = tweetText.translate(string.maketrans("",""), string.punctuation)
        tweetText = " " + tweetText + " "

        rospy.loginfo tweetText

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        #print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        for data in dictionary:
            if (data) in tweetText:
                rospy.loginfo '@{0}: {1}'.format(tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore'))
                data = data.strip()
                directionList.append(data)
                rospy.loginfo (directionList)
                return directionList
        return True

    def on_error(self, status):
        rospy.loginfo status

def keyword_changer(event):
    global command
    if len(directionList > 0):
        command = directionList.pop(0)
    return True

#API Keys
consumer_key = "E6uJ66Idggzd2ztGxyHhyzs3q"
consumer_secret = "5CwZpFz9gzeOLzOX08Byp1fxweoGJ3NuwUT6E0DwPN5l2dI3oX"
access_token = "700398196724400129-wZXwo1uL7sERuxa4e3LIxVQW6o3kps2"
access_token_secret = "kc8Dm2oYE511qIGU4Btg1Szn37zdE9H9QhyTimCh6ULgW"

#Defaults for dictionary and handle
dictionary = [" forward ", " backward ", " left ", " right "]
handle = "@turtlebot"

#list of directions
directionList = []
command = ""

if __name__ == '__main__':
    rospy.init_node('twitterListInterface')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = tweepy.Stream(auth, StdOutListener())

    stream.filter(track=[handle])

    # A publisher for the move data
    pub = rospy.Publisher('teleop_directions', String)

    # Loop at 10Hz, publishing movement commands until we shut down.
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.Timer(rospy.Duration(1), keyword_changer)
        pub.publish(command)
        rate.sleep()
