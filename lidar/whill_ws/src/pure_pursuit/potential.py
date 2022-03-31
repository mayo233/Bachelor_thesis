#!/usr/bin/env python
# -*- coding: utf-8 -*- # 日本語を使うためのおまじない。
import roslib
import rospy
import math
from geometry_msgs.msg import Twist # ロボットの速度を扱う場合は必要
from sensor_msgs.msg import LaserScan # LIDARを使うときは必要

def lidar_callback(msg):
    #range_ahead = msg.ranges[len(msg.ranges)//2] #ロボットの真正面にある障害物までの距離　ranges配列の中央要素

    print(min(msg.ranges))    #正面にある障害物までの距離を表示
    if msg.ranges<0.384999990463:
    	
    	
    		
if __name__ == '__main__':
    rospy.init_node('tf_obstacle')
    rospy.Subscriber('/scan', LaserScan,lidar_callback)
    #br = tf.TransformBroadcaster()
    r = rospy.Rate(0.4)
    while not rospy.is_shutdown():
        r.sleep()
