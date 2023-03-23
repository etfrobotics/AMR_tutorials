#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
        rospy.loginfo(rospy.get_caller_id() + ' I heard %s', data.data)         # Read data from the topic

def listener():
    rospy.init_node('hello_world_subscriber', anonymous = False)                # Init node 
    rospy.Subscriber('hello_topic', String, callback)                           # Define subscriber
    rospy.spin()                                                                # Keep code runnings

if __name__ == '__main__':
    listener()