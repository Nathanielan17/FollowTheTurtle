
import rclpy
from rclpy.node import Node

from turtlesim.srv import Spawn
from turtlesim.msg import Pose
from interface_package.msg import SingleList
from interface_package.srv import CatchTurtle
import numpy as np
from geometry_msgs.msg import Twist
from math import pi
#from random import randint


class turtleController(Node):

    def __init__(self):
        super().__init__('hw4_3')

        # Is the client to the catch_turtle service
        self.cli_catch = self.create_client(CatchTurtle, '/catch_turtle')
        self.req_catch = CatchTurtle.Request()

        self.sub_pose = self.create_subscription(Pose,'/turtlesim1/turtle1/pose',self.pose_callback,10)

        self.sub_alive = self.create_subscription(SingleList, '/alive_turtles', self.update_target,10) # sends array to a topic

        self.publisher = self.create_publisher(Twist,'turtlesim1/turtle1/cmd_vel',10)
        timer_period = 1 # seconds
        self.timer = self.create_timer(timer_period,self.timer_callback)

    # collects live data of turtle1 and stores it
    def pose_callback(self,msg):
        self.curr_x = msg.x
        self.curr_y = msg.y
        self.curr_theta = msg.theta
        self.curr_lin_vel = msg.linear_velocity
        self.curr_ang_vel = msg.angular_velocity

    # updates target live
    def update_target(self,msg):
        self.target_name = msg.data[0]
        x,y = msg.data[1].split(',')    # original msg is a string format of 'x,y'
        self.target_x = float(x)
        self.target_y = float(y)
        self.get_logger().info('x: %s, y: %s' % (x,y))


    # call when a turtle has been determined to be captured
    def catch_turtle(self):
        self.req_catch.data = self.target_name
        self.future = self.cli_catch.call_async(self.req_catch)

    
    # will control turtle1 and determine when to send a request to catch a turtle
    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 1.0
        run = self.target_x - self.curr_x
        rise = self.target_y - self.curr_y
        if rise == 0 and run != 0:
            ang_vel = pi
            msg.angular.z = ang_vel
            self.publisher.publish(msg)
        elif run == 0 and rise != 0:
            ang_vel = pi
            msg.angular.z = ang_vel
        elif run != 0 and rise != 0:
            ang_vel = np.arctan(rise/run)
            msg.angular.z = ang_vel

        else:   # turtle has reached target
            self.catch_turtle()
        



def main(args=None):
    rclpy.init(args=args)

    turtle_controller = turtleController()

    rclpy.spin(turtle_controller)

    turtle_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()