from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            namespace='turtlesim1',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='hw4_3',
            executable='py_hw4_3_spawner',
            name='turtle_spawner',
            parameters=[
                {'timer_param': 10}
            ]            
        ),  
        Node(
            package='hw4_3',
            executable='py_hw4_3_controller',
            name='turtle_controller',           
        ),
        Node(
            package='hw4_3',
            executable='py_hw4_3_service',
            name='catch_turtle_node',           
        )  

    ])