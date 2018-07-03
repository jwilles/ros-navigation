#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import PoseWithCovarianceStamped, Pose 



def service_callback(request):
    global robot_pose
    print robot_pose
    return EmptyResponse()
    
    
def sub_callback(msg):
    global robot_pose
    robot_pose = msg.pose.pose
    

rospy.init_node('get_pose_service')
robot_pose = Pose()
pose_client = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, sub_callback)
get_pose_service = rospy.Service('/get_pose_service', Empty, service_callback)
rospy.spin()