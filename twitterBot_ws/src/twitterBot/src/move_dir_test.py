#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('nextMove', String, queue_size=10)
    rospy.init_node('move_dir_test', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        for x in xrange(1,10):
            move_str = "forward"
            rospy.loginfo(move_str)
            pub.publish(move_str)
            #rate.sleep()
        for y in xrange(1,10):
            move_str = "backwards"
            rospy.loginfo(move_str)
            pub.publish(move_str)
            #rate.sleep()
        for z in xrange(1,10):
            move_str = "left"
            rospy.loginfo(move_str)
            pub.publish(move_str)
            #rate.sleep()
        for a in xrange(1,10):
            move_str = "right"
            rospy.loginfo(move_str)
            pub.publish(move_str)
            #rate.sleep()
        rate.sleep()
      

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
