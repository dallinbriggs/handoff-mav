#!/usr/bin/env python
import rospy
from rosflight_msgs.msg import GPS

def position_pub():
    pos_pub = rospy.Publisher('/target/position', GPS, queue_size=1)
    rospy.init_node('Target_Position_Publisher')
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        msg = GPS()
        msg.fix = False
        msg.NumSat = 0
        msg.latitude = 40.363209
        msg.longitude = -111.901553
        msg.altitude = 1370.0
        msg.speed = 0.0
        msg.ground_course = 0.0
        msg.covariance = 0.0
        rospy.loginfo(msg)
        pos_pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        position_pub()
    except rospy.ROSInterruptException:
        pass
