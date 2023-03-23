#!/usr/bin/env python3

import rospy
from hello_world.srv import add_value_file, add_value_fileResponse              # Load service 

def respons_callback(req):                              # Create respons callback function
    f = open('value_file.txt', 'a+')                    # Open file "value_file.txt" in append mode at the end of file
    f.write(str(req.value)+'\n')                        # Cast int64 in string type add newline character and write it in file
    f.close()                                           # Close file
    return add_value_fileResponse(True)                 # Send repsonse to caller

rospy.init_node('add_value_file_service')                                           # Init node
srv = rospy.Service('add_value_file', add_value_file, respons_callback)             # Create service
rospy.loginfo('Service is ready!!!')                                                # Tell user that the service is ready
rospy.spin()                                                                        # Keep the code runing
