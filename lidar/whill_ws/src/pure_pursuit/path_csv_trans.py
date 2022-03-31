#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import csv
import tf
from nav_msgs.msg import Path
from math import *
global a,b,count
x=[]
def global_path(msg):
	for i in range(len(msg.poses)):
		a=msg.poses[i].pose.position.x
		b=msg.poses[i].pose.position.y
		#x=a[14000:14500]
		#print(x)	
		print('{0},{1}'.format(a,b))
		
    		
if __name__ == '__main__':
    rospy.init_node('tf_broadcaster')
    #rospy.Subscriber('/move_base/TrajectoryPlannerROS/global_plan', Path,global_path)
    rospy.Subscriber('/move_base/NavfnROS/plan', Path,global_path)
    #br = tf.TransformBroadcaster()
    r = rospy.Rate(0.4)
    while not rospy.is_shutdown():
        r.sleep()
