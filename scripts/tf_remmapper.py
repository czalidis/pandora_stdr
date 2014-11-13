#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

class Remapper(object):

    def __init__(self):
        self.pub = rospy.Publisher("/laser/scan", LaserScan)
        rospy.Subscriber("/robot0/laser_0", LaserScan, self.tf_remapper)

    def tf_remapper(self, msg):
        msg.header.frame_id = 'laser_link'
        self.pub.publish(msg)

if __name__ == '__main__':
    rospy.init_node('laser_rmap')
    remapper = Remapper()
    rospy.spin()
