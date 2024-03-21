# Instalacija neophodnih paketa

Komanda za instalaciju ROS paketa:
```
  sudo apt-get install ros-noetic-joy ros-noetic-teleop-twist-joy \
  ros-noetic-teleop-twist-keyboard ros-noetic-laser-proc \
  ros-noetic-rgbd-launch ros-noetic-rosserial-arduino \
  ros-noetic-rosserial-python ros-noetic-rosserial-client \
  ros-noetic-rosserial-msgs ros-noetic-amcl ros-noetic-map-server \
  ros-noetic-move-base ros-noetic-urdf ros-noetic-xacro \
  ros-noetic-compressed-image-transport ros-noetic-rqt* ros-noetic-rviz \
  ros-noetic-gmapping ros-noetic-navigation ros-noetic-interactive-markers
```

Komanda za instalaciju TurtleBot3 paketa:
```
sudo apt-get install ros-noetic-dynamixel-sdk
sudo apt-get install ros-noetic-turtlebot3-msgs
sudo apt-get install ros-noetic-turtlebot3
sudo apt-get install ros-noetic-turtlebot3-simulations
```

# Pokretnje simulacije
Da bi simulator znao kog robota treba da simulira potrebno je pokrenuti sledeću komandu:
```
export TURTLEBOT3_MODEL=burger
```
Sledećom komandom se pokreće Gazebo simulator:
```
roslaunch turtlebot3_gazebo turtlebot3_world.launch
```

U novom terminalu zatim se poziva program za kontrolu robota:
```
rosrun move_robot move_robot_node.py
```
***Napomena: neophodno je pre pokretanja kompajlovati paket***

