#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
import numpy

def callback(data):
    msg = LaserScan()
    msg = data
    rho = msg.ranges[0:10]
    theta = []
    for i in range(10):
        theta.append( msg.angle_min + i*msg.angle_increment)
    
    x = numpy.zeros(10)
    y = numpy.zeros(10)
    for i in range(10):
        x[i] = rho[i]*numpy.cos(theta[i])
        y[i] = rho[i]*numpy.sin(theta[i])
    
    xc = numpy.mean(x)
    yc = numpy.mean(y)
    
    x_t = numpy.zeros(10)
    y_t = numpy.zeros(10)

    x_t = xc - x
    y_t = yc - y
    
    sum1 = numpy.sum(x_t*y_t)
    sum2 = numpy.sum(y_t**2 - x_t**2)

    alpha = 0.5*numpy.arctan2(-2*sum1,sum2) 
    
    r = xc*numpy.cos(alpha) + yc*numpy.sin(alpha)

    rospy.loginfo(r)
    rospy.loginfo(alpha)





rospy.init_node("line_fitting_node")
rospy.Subscriber("/kobuki/laser/scan",LaserScan,callback)
rospy.loginfo("Ready to fit lines!")
rospy.spin()