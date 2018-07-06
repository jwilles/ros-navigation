#! /usr/bin/env python

import rospy
from nav_msgs.srv import GetPlan, GetPlanRequest

if __name__ == '__main__':
    rospy.init_node('make_plan_client')
    plan_client = rospy.ServiceProxy('/move_base/make_plan', GetPlan)
    plan_req = GetPlanRequest()
    plan_req.goal.header.frame_id = 'map'
    plan_req.goal.pose.position.x = 0.5
    plan_req.goal.pose.position.y = -0.5
    plan_req.goal.pose.position.z = 0.0
    plan_req.goal.pose.orientation.x = 0.0
    plan_req.goal.pose.orientation.y = 0.0
    plan_req.goal.pose.orientation.z = 0.75
    plan_req.goal.pose.orientation.w = 0.66
    
    result = plan_client(plan_req)
    print result
    
    