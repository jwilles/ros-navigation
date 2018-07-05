#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyRequest

rospy.init_node('particle_initialization_node')
rospy.wait_for_service('/global_localization')
particle_client = rospy.ServiceProxy('/global_localization', Empty)
result = particle_client(EmptyRequest())
print result


