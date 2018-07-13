#! /usr/bin/env python

import rospy
from summit_mapping.srv import RecordPose, RecordPoseResponse
from geometry_msgs.msg import PoseWithCovarianceStamped

def sub_callback(msg):
    global robot_pose
    robot_pose = msg


def callback(req):
    
    global pose_array
    global robot_pose
    
    res = RecordPoseResponse()
    
    if req.label == 'end':
        with open("pose_file.txt", "a") as pose_file:
            for pose in pose_array:
                pose_file.write(pose[0] + ': ' + str(pose[1]))
        res.navigation_successfull = True
        res.message = 'Saved to file'
        return res
    else:
        pose_array.append([req.label, robot_pose])
        res.navigation_successfull = True
        res.message = 'Saved'
        return res
        
    
    

rospy.init_node('record_pose')
robot_pose = PoseWithCovarianceStamped()
pose_array = []
pose_client = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, sub_callback)
record_pose_service = rospy.Service('/record_pose', RecordPose, callback)
rospy.spin()