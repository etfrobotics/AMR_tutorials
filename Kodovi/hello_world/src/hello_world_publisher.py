#!/usr/bin/env python3

import rospy                                    # Import Python ros libraby
from std_msgs.msg import String                 # Import String data type from standard msg

def talker():
    rospy.init_node('hello_world_publisher',anonymous = False)          # Init Python node 
    pub = rospy.Publisher('hello_topic', String, queue_size = 10)       # Define publisher
    r = rospy.Rate(10)                                                  # Define rate for while loop in HZ
    while not rospy.is_shutdown():
        data = 'Hello world %s' %rospy.get_time()                       # Create data to be send
        rospy.loginfo(data)                                             # Log data in node terminal
        pub.publish(data)                                               # Send data to 'hello_topic'
        r.sleep()                                                       # Sleep for define time

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass