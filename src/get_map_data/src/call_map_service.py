#! /usr/bin/env python

import rospy
from nav_msgs.srv import GetMap, GetMapRequest

rospy.init_node('get_map_data')
rospy.wait_for_service('/static_map')
get_map_request = GetMapRequest()
get_map_client = rospy.ServiceProxy('/static_map', GetMap)
map_data = get_map_client(get_map_request)
rospy.loginfo(map_data)

