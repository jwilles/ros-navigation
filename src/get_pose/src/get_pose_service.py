#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyReponse


def callback(request):
    
    

rospy.init_node('get_pose_service')
get_pose_service = rospy.Service('/get_pose_service', Empty, callback)
