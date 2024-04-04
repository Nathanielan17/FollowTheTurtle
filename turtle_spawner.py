
import rclpy
from rclpy.node import Node

from turtlesim.srv import Spawn
from interface_package.msg import SingleList
from std_msgs.msg import String

#from geometry_msgs.msg import Twist
from math import pi
from random import randint


class turtleSpawner(Node):

    def __init__(self):
        super().__init__('hw4_3')

        self.cli_spawn = self.create_client(Spawn, '/turtlesim1/spawn')
        self.req_spawn = Spawn.Request()
        self.num_alive_turtles = []
        
        # sets timer parameter
        timer_period = 10
        self.declare_parameter('timer_param',1)
        #timer_period = self.get_parameter('timer_param').get_parameter_value().double_value
        self.timer = self.create_timer(timer_period,self.timer_callback)

        self.publisher = self.create_publisher(SingleList, '/alive_turtles',10) # sends array to a topic
        self.sub_kill = self.create_subscription(String, '/kill_turtle', self.kill_turtle,10) # client to kill service
        
        # Initial spawn of turtles
        for i in range(2):
            self.send_request_spawn()
        self.update_current_turtles()

    def update_current_turtles(self):
        msg = SingleList()
        msg.data = self.num_alive_turtles
        self.publisher.publish(msg)


    def send_request_spawn(self):
        x = float(randint(2,9))
        y = float(randint(2,9))
        self.req_spawn.x = x
        self.req_spawn.y = y
        theta = randint(0,360)
        self.req_spawn.theta = float(theta*(2*pi)/360)
        self.req_spawn.name = "" # empty name inputted to get a unique name back
        #self.get_logger().info('x: %d, y: %d' % (x,y))
        self.future_spawn = self.cli_spawn.call_async(self.req_spawn) # sends request to spawn turtle
        s = str(x) + ',' +str(y)
        rclpy.spin_until_future_complete(self,self.future_spawn)
        self.num_alive_turtles.append(self.future_spawn.result().name)
        self.num_alive_turtles.append(s)

        
    def kill_turtle(self,msg):
        name = msg.data
        for i in range(len(self.num_alive_turtles)):
            if self.num_alive_turtles[i] == name:
                self.num_alive_turtles.pop(i) # after popping name, the element replaces it is the coordinates of deleted name
                self.num_alive_turtles.pop(i) # pops the coordinates
                break
        self.update_current_turtles()
        
    
    def timer_callback(self):
        # time has elapsed meaning more turtles need to be spawned
        for i in range(2):
            self.send_request_spawn()
        self.update_current_turtles()
        

def main(args=None):
    rclpy.init(args=args)

    hw4_3_publisher = turtleSpawner()

    rclpy.spin(hw4_3_publisher)

    hw4_3_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()