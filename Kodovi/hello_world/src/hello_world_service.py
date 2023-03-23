#!/usr/bin/env python3

import rospy
from hello_world.srv import add_value_file, add_value_fileResponse

def respons_callback(req):
    f = open('value_file.txt', 'a+')
    f.write(str(req.value)+'\n')
    f.close()
    return add_value_fileResponse(True)

rospy.init_node('add_value_file_service')
srv = rospy.Service('add_value_file', add_value_file, respons_callback)
rospy.loginfo('Service is ready!!!')
rospy.spin()
