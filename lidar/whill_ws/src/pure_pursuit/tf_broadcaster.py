#!/usr/bin/env python
# -*- coding: utf-8 -*- # 日本語を使うためのおまじない。
import rospy
import csv
import tf
import whill_path
from nav_msgs.msg import Path
from sensor_msgs.msg import LaserScan
from math import *
from visualization_msgs.msg import Marker

pub = rospy.Publisher("arrow_pub", Marker, queue_size = 10)
path_x=[]
path_y=[]
flag=False
count=0
path=[[]]
goal=0
th=1.85337064793
x_0=1.329
y_0=0.749
l_d=1.26811674

#x_r=(whill_path.call_x)
#y_r=(whill_path.call_y)
#print(type(x_r))
#print(type(a))
#障害物回避を行う関数
def lidar_callback(msg):
       global flag
       #print(min(msg.ranges))
       
	#1.85337064793  0.55337064793
       if (min(msg.ranges))<0.55337064793:

       		flag=True
       		
       else:
       		flag=False


if __name__ == '__main__':
    rospy.init_node('tf_broadcaster')
    rospy.Subscriber('/scan', LaserScan,lidar_callback)
    br = tf.TransformBroadcaster()
    r = rospy.Rate(2.4) #2.4
    
    while not rospy.is_shutdown():
	with open("/home/suzukamayo/ros_ws/lidar/whill_ws/src/pure_pursuit/simple_odom_simulator/scripts/freespace/1_15_D*1B_test_csv", "r") as f:
    		reader = csv.reader(f)
    		
    		#障害物を過ぎたらlidar_callbackを呼ばない 143 70
    		if (((count >109) and (count <155)) or ((count <70) and (count >0))):
    		#if (count < 70 and count >0) :
    			flag =False
    			
    		#経路追従を終える
    		if count>153: #141
			break
	        for row in reader:
		        path_x.append(float(row[0]))
		        path_y.append(float(row[1]))
		        
	        """
		#A=1+((y_r-y_0)/ (x_0-x_r))
		A=1+(float(y_r)-y_0 / x_0-float(x_r))
		
		
		B=-2*y_r-2*x_r*((y_r-y_0)/(x_0-x_r))+((y_r-y_0)/(x_0-x_r))*(((l_d)**2+(x_0)**2+(y_0)**2-(th)**2-(x_r)**2-(y_r)**2)/(2*x_0-2*x_r))
		
		C=(x_r)**2+(y_r)**2-(l_d)**2+(((l_d)**2+(x_0)**2+(y_0)**2-(th)**2-(x_r)**2-(y_r)**2)/(2*x_0-2*x_r))**2-x_r*(((l_d)**2+(x_0)**2+(y_0)**2-(th)**2-(x_r)**2-(y_r)**2)/(x_0-x_r))
		
		D=((B**2)-(4*A*C))**1/2
		y_l=-B+D/2*A
		x_l=(y_r-y_0/x_0-x_r)*y_l+((l_d)**2+(x_0)**2+(y_0)**2-(th)**2-(x_r)**2-(y_r)**2/(2*x_0-2*x_r))
		"""
		
	#障害物がないなら前進
	if flag==False:
		print("前進")		
		br.sendTransform((path_x[count],path_y[count],0),
					tf.transformations.quaternion_from_euler(0,0,0),
					rospy.Time.now(),
					'arrow_pub',
					'start')
					
	#障害物と衝突しそうなら目標点をずらす 0.82:y
	else:
		print("障害物回避")
		br.sendTransform((path_x[count]+0.2,path_y[count]+0.52,0), 
					tf.transformations.quaternion_from_euler(0,0,0),
					rospy.Time.now(),
					'arrow_pub',
					'start')
		
		
	count+=1
        
	print(path_x[count])
	print(path_y[count])
	print(count)
	#print(x_l)
		
        rospy.loginfo('Transform Published')
        r.sleep()
