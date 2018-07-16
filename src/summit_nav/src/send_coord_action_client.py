#! /usr/bin/env python

import rospy
import actionlib
import rosparam
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, PoseWithCovarianceStamped


class SendCoordinates:
    
    def __init__(self, label):
        
        self.ctrl_c = False
        rospy.on_shutdown(self.shutdownhook)
        
        client = actionlib.SimpleActionClient('/move_base', MoveBaseAction, )
        rate = rospy.Rate(1)
        
        goal = MoveBaseGoal()
        target_pose = Pose()
        
        while not self.ctrl_c:
            
            target_pose.position.x=rosparam.get_param(label+'/position/x')
            target_pose.position.y=rosparam.get_param(label+'/position/y')
            target_pose.position.z=rosparam.get_param(label+'/position/z')
            target_pose.orientation.x=rosparam.get_param(label+'/orientation/x')
            target_pose.orientation.y=rosparam.get_param(label+'/orientation/y')
            target_pose.orientation.z=rosparam.get_param(label+'/orientation/z')
            target_pose.orientation.w=rosparam.get_param(label+'/orientation/w')
            goal.target_pose.pose=target_pose
            goal.target_pose.header.frame_id='map'
            
            client.wait_for_server()
            client.send_goal(goal, feedback_cb=self.feedback_callback)
            client.wait_for_result()
            result=client.get_state()
                
            #print result
            if result==3:
                print('successfuly reached point')
                self.shutdownhook()
            
        
    def shutdownhook(self):
        rospy.loginfo("shutdown")
        self.ctrl_c = True
        
    def feedback_callback(self, feedback):
        rospy.loginfo(feedback)
        
        
        
        