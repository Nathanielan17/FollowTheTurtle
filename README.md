# FollowTheTurtle

## Purpose
The purpose behind this project was to utilize a solid understanding of the Robot Operating System (ROS) 2 framework and build nodes, servers and design various messages/packets of information between create a simulation that can be applied towards robotic hardware. FollowTheTurtle serves to use the ROS2 framework to build a simulation of a bait-catch approach where the turtlesim (simulated robot) will be automatically controlled via information between nodes and servers to guide itself towards spawned turtles as a target. Targets are spawned at a particular frequency in the displayed window and will be killed/removed once caught by the turtlesim. FollowTheTurtle can be built upon in the future to recognize targets via robotic hardware using Lidar.

## Set Up
The set up of this document was built within a Ubuntu space via a Docker container. The docker container must build an image using a Humble docker file and it must include the neccessary dependencies to run/build this project:
- ros-dev-tools
- python-is-python3
- python3-pip
- setuptools 58.2 ver

## How To Run
To run this on your own Ubuntu space, you must create a ROS2 package and have the neccessary dependencies.

To launch the program type: ros2 launch *__package__name__* turtlecon_launch.py
*Replace the package name with the pkg you created*
