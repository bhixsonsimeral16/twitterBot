#!/usr/bin/env python


# Every python controller needs these lines
#import roslib; roslib.load_manifest('lab1')
import rospy
import sys
import numpy
from std_msgs.msg import Float64

# The velocity command message
from geometry_msgs.msg import Twist
def callback(data):
    global currentGoal
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    rospy.loginfo("I heard: {0}".format(data.data))
    if(currentGoal > -1):
        currentGoal = data.data
        return currentGoal

def setCommand():
    global position
    global command
    global currentGoal
    #currentGoal = float(currentGoal)
    rospy.loginfo("position: {0}".format(position))
    rospy.loginfo("currentGoal: {0}".format(currentGoal))
    # if we are at the goal, stop
    if ((position > (currentGoal - 0.015)) and (position < (currentGoal + 0.015))):
        command.linear.x = 0
    # if the goal is ahead, move forward
    # add distance moved to position
    elif (currentGoal > position):
        command.linear.x = 0.3
        position += 0.03
    # if the goal is behind, move backward
    # add distance moved to position
    elif (currentGoal < position):
        command.linear.x = -0.3
        position -= 0.03
    rospy.loginfo("Made it into the setCommand: {0}".format(currentGoal))
    return command


if __name__ == '__main__':
    #start position is 1.5 meters
    position = 1.5
    currentGoal = 1.5
    rospy.init_node('turtlebot_tug')

    # A publisher for the move data
    pub = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size = 10)
    # take the strings from the 'tweets' topic and push them to the callback method
    rospy.Subscriber('tug', Float64, callback)
	
    command = Twist()

    command.linear.x = 0.0
    command.linear.y = 0.0
    command.linear.z = 0.0
    command.angular.x = 0.0
    command.angular.y = 0.0
    command.angular.z = 0.0
    #command = setCommand()
    

    # Loop at 10Hz, publishing movement commands until we shut down.
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        command = setCommand()
        pub.publish(command)
        rate.sleep()
