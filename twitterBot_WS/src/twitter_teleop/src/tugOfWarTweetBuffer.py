#!/usr/bin/env python

# Every python controller needs these lines
import roslib; roslib.load_manifest('lab1')
import rospy

#imports for twitter API
import string

#String, Time, and Int32
from std_msgs.msg import String
from std_msgs.msg import Int32
from std_msgs.msg import Time

#for ration calculation
import math

def ratio_calc(event):
    global command
    global directionList
    x = directionList[0][1]
    y = directionList[1][1]
    ratio = x/(x+y)
    #turn the ratio into a position for the turtlebot to go to
    command = (math.floor(ratio * 100) * 3) / 100
    rospy.loginfo (command)
    return True

def callback(data):
    global directionList
    if(directionList[0][0] == data):
        directionList[0][1] += 1
    elif(directionList[1][0] == data):
        directionList[1][1] += 1
    rospy.loginfo(directionList)
    return True

#API Keys
consumer_key = "E6uJ66Idggzd2ztGxyHhyzs3q"
consumer_secret = "5CwZpFz9gzeOLzOX08Byp1fxweoGJ3NuwUT6E0DwPN5l2dI3oX"
access_token = "700398196724400129-wZXwo1uL7sERuxa4e3LIxVQW6o3kps2"
access_token_secret = "kc8Dm2oYE511qIGU4Btg1Szn37zdE9H9QhyTimCh6ULgW"

#Defaults for dictionary and handle
dictionary = ["iphone", "android"]
handle = "@turtlebot"

directionList=[]
directionList=directionList.append([])
directionList[0][0] = dictionary[0]
directionList[1][0] = dictionary[1]
directionList[0][1] = 0
directionList[1][1] = 0
command = "test"

if __name__ == '__main__':
    try:
        # Loop at 10Hz, publishing movement commands until we shut down.
        rospy.init_node('tugTweetBuffer')

        # A publisher for the move data
        pub = rospy.Publisher("tug", Int32, queue_size=10)

        rate = rospy.Rate(10)
    	while not rospy.is_shutdown():
            sub = rospy.Subscriber("twitterTugDirection", String, callback)
            #rospy.Timer(rospy.Duration(2), ratio_calc)
            ratio_calc
            pub.publish(command)

	    rate.sleep()

    except rospy.ROSInterruptException:
        pass
