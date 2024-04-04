
import rclpy
from rclpy.node import Node

from turtlesim.srv import Spawn
from interface_package.msg import SingleList
from interface_package.srv import CatchTurtle
from std_msgs.msg import String
#from geometry_msgs.msg import Twist
from math import pi
from random import randint


class turtleCatch(Node):

    def __init__(self):
        super().__init__('hw4_3')
        self.srv = self.create_service(CatchTurtle,'/catch_turtle', self.kill_turtle)

        self.publisher = self.create_publisher(String,'/kill_turtle',10)

    def kill_turtle(self,request,response):
        msg = String()
        msg.data = request.data
        self.publisher.publish(msg) # sends to turtle spawner node


   

def main(args=None):
    rclpy.init(args=args)

    turtle_catch = turtleCatch()

    rclpy.spin(turtle_catch)

    turtle_catch.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()