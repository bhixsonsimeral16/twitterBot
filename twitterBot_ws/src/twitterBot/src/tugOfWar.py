
#!/usr/bin/env python


# Every python controller needs these lines
import roslib; roslib.load_manifest('lab1')
import rospy
import sys

# The velocity command message
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

#start position is 1.5 meters
position = 1.5

if __name__ == '__main__':
    global position
    rospy.init_node('tug')

    # A publisher for the move data
    pub = rospy.Publisher('cmd_vel_mux/input/navi', Twist)
	
    command = twist()

    command.linear.x = 0.0
    command.linear.y = 0.0
    command.linear.z = 0.0
    command.angular.x = 0.0
    command.angular.y = 0.0
    command.angular.z = 0.0

    # take the strings from the 'tweets' topic and push them to the callback method
    currentGoal = rospy.Subscriber('tweets', StdMsgs, callback)

    # Loop at 10Hz, publishing movement commands until we shut down.
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(command)
        rate.sleep()

def callback(data):
	global position
	# if the goal is ahead, move forward
	# add distance moved to position
	if (currentGoal > position):
		command.linear.x = 0.3
		poistion += 0.03
	# if the goal is behind, move backward
	# add distance moved to position
	elif (currentGoal < position):
		command.linear.x = -0.3
		position -= 0.03
	# if we are at the goal, stop
	elif (currentGoal == position):
		command.linear.x = 0