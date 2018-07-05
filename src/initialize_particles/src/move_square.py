#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist, PoseWithCovarianceStamped, Pose 
from std_srvs.srv import Empty, EmptyRequest
import time

class MoveHusky():
    
    def __init__(self):
        self.husky_vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.husky_pose_client = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, self.pose_callback)
        
        self.ctrl_c = False
        self.covariance =[]
        
        rospy.on_shutdown(self.shutdownhook)
        self.rate = rospy.Rate(10) # 10hz
    
    def init_particles(self):
        rospy.wait_for_service('/global_localization')
        particle_client = rospy.ServiceProxy('/global_localization', Empty)
        res = particle_client(EmptyRequest())
        rospy.loginfo('Particles Initialized')
        rospy.loginfo(res)
        
    def pose_callback(self, msg):
        self.covariance = msg.pose.covariance
        
    def get_pose_covariance(self):
        return self.covariance
        
    def shutdownhook(self):
            # works better than the rospy.is_shut_down()
            self.ctrl_c = True

    def move_x_time(self, moving_time, linear_speed=0.2, angular_speed=0.2):
        
        cmd = Twist()
        cmd.linear.x = linear_speed
        cmd.angular.z = angular_speed
        
        tic = time.time()
        toc = time.time()
        
        while toc - tic < moving_time and not self.ctrl_c:
            self.husky_vel_publisher.publish(cmd)
            toc = time.time()
            
        rospy.loginfo("######## Finished")
    
    def move_square(self):
        
        i = 0
        while not self.ctrl_c and i < 4:
            # Move Forwards
            self.move_x_time(moving_time=10.0, linear_speed=0.2, angular_speed=0.0)
            # Stop
            self.move_x_time(moving_time=4.0, linear_speed=0.0, angular_speed=0.0)
            # Turn 
            self.move_x_time(moving_time=20.0, linear_speed=2.0, angular_speed=0.5)
            # Stop
            self.move_x_time(moving_time=1.0, linear_speed=0.0, angular_speed=0.0)
            
            i += 1
        rospy.loginfo("######## Finished Moving in a Square")
        

            
if __name__ == '__main__':
    rospy.init_node('move_husky_square', anonymous=True)
    husky = MoveHusky()
    try:
        husky.init_particles()
        husky.move_square()
        rospy.loginfo(husky.get_pose_covariance())
    except rospy.ROSInterruptException:
        pass
