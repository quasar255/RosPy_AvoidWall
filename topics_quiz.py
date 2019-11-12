#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist # import twist message from geometry_msgs package
from sensor_msgs.msg import LaserScan


def distcalc(msg):
    #print msg.ranges[360] # distance to an obstacle in front of the robot
    if msg.ranges[360] < 1.0:
        pos.angular.z = 7.0
        pos.linear.x = 0.0
    #elif msg.ranges[180] < 1.0:
     #   pos.angular.z = 5.0
      #  pos.linear.x = 0.0
    else:
        pos.angular.z = 0.0
        pos.linear.x = 0.1

pos = Twist()
rospy.init_node('topics_quiz_node')  # initiate a node named 'topics_quiz_node'
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) # Create a Publisher object, that will publish on the /cmd_vel topic
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, distcalc)   # Create a Subscriber object that will listen to the /kobuki/laser/scan

while not rospy.is_shutdown():    # Create a loop that will go until someone stops the program execution
  pub.publish(pos)       # Publish the message within the 'Pos' var