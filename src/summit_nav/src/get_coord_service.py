#! /usr/bin/env python

import rospy
import os
import rosparam
from summit_nav.srv import GetCoord, GetCoordResponse
from send_coord_action_client import SendCoordinates

class GetCoordService:
    def __init__(self):
        self.get_coord_service = rospy.ServiceProxy('/get_coordinates', GetCoord, self.callback)
        
        
    def callback(self, req):
        label = req.label
        res = GetCoordResponse()
        
        os.chdir("/home/user/catkin_ws/src/summit_nav")
        paramlist=rosparam.load_file("spots.yaml",default_namespace=None)
        
        for params,ns in paramlist: #ns,param
        
            for key, value in params.iteritems():
                if key == label:
                    rosparam.upload_params(ns,params) #ns,param
                    res.message = "Correctly uploaded parameters"
                    
        send_coordinates = SendCoordinates(label)
        
        res.navigation_successfull = True
        
        return response
        

        
        
        
        
        
if __name__ == '__main__':
    rospy.init_node('get_coord_service')
    GetCoordService()
    rospy.spin()