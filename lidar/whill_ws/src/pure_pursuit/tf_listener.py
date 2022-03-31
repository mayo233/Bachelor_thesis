#!/usr/bin/env python  
import roslib
import rospy
import math
from nav_msgs.msg import Path
import tf
from geometry_msgs.msg import Twist
import turtlesim.srv
flag=False
count=0
def callback():
	global count
	pub=rospy.Publisher('/whill/controller/cmd_vel',Twist,queue_size=10)
	ls=tf.TransformListener()
	r=rospy.Rate(4.3)
	while not rospy.is_shutdown():
		try:
		       (trans,rot)=ls.lookupTransform('/base_link', '/arrow_pub',rospy.Time(0))
			
		except (tf.LookupException,tf.ConnectivityException,tf.ExtrapolationException):
			continue
		
		shita=math.atan2(trans[1],trans[0])
		
		control=Twist()
		
		control.linear.x=0.0745
		
		control.angular.z=shita
		
		#print(control.angular.z)
		pub.publish(control)
		r.sleep()
		
		
		
if __name__ == '__main__':
    rospy.init_node('pure_pursuit_listen')
    callback()
