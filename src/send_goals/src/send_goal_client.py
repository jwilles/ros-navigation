#! /usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def move_base_client(goal):
    move_base_client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
    move_base_client.wait_for_server()
    
    move_base_client.send_goal(goal, feedback_cb=feeback_callback)
    
    rate = rospy.Rate(1)
    
    state = move_base_client.get_state()
    
    while state < 2:
        state = move_base_client.get_state()
        rate.sleep()
        
def feeback_callback(feedback):
    rospy.loginfo(feedback)

    
if __name__ == '__main__':
    rospy.init_node('move_base_client')
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = 'map'
    while True:
        goal.target_pose.pose.position.x = 1.16
        goal.target_pose.pose.position.y = -4.76
        goal.target_pose.pose.position.z = 0.0
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.75
        goal.target_pose.pose.orientation.w = 0.66
        move_base_client(goal)
        
        goal.target_pose.pose.position.x = 0.5
        goal.target_pose.pose.position.y = -0.59
        goal.target_pose.pose.position.z = 0.0
        goal.target_pose.pose.orientation.x = 0.0
        goal.target_pose.pose.orientation.y = 0.0
        goal.target_pose.pose.orientation.z = 0.355
        goal.target_pose.pose.orientation.w = 0.93
        move_base_client(goal)
        
        
        
        


