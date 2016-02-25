#!/usr/bin/env python

# Every python controller needs these lines
import roslib; roslib.load_manifest('lab1')
import rospy

#imports for twitter API
import string

#String and Time
from std_msgs.msg import String
from std_msgs.msg import Time

def keyword_changer(event):
    global command
    global directionList
    if (len(directionList) > 0):
        command = directionList.pop(0)
        rospy.loginfo (command)
    return True

def callback(data):
    global directionList
    directionList.append(data)
    rospy.loginfo(directionList)
    return True

#API Keys
consumer_key = "E6uJ66Idggzd2ztGxyHhyzs3q"
consumer_secret = "5CwZpFz9gzeOLzOX08Byp1fxweoGJ3NuwUT6E0DwPN5l2dI3oX"
access_token = "700398196724400129-wZXwo1uL7sERuxa4e3LIxVQW6o3kps2"
access_token_secret = "kc8Dm2oYE511qIGU4Btg1Szn37zdE9H9QhyTimCh6ULgW"

#Defaults for dictionary and handle
dictionary = [" forward ", " backward ", " left ", " right "]
handle = "@turtlebot"

directionList=[]
command = "test"

if __name__ == '__main__':
    try:
        # Loop at 10Hz, publishing movement commands until we shut down.
        rospy.init_node('tweetBuffer')

        # A publisher for the move data
        pub = rospy.Publisher("nextMove", String, queue_size=10)

        rate = rospy.Rate(10)
    	while not rospy.is_shutdown():
            sub = rospy.Subscriber("twitterDirection", String,callback)
            rospy.Timer(rospy.Duration(2), keyword_changer)
            pub.publish(command)

	    rate.sleep()

    except rospy.ROSInterruptException:
        pass
