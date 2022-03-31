#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import csv
# import for ros function
import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Header
from nav_msgs.msg import Path
#########################
# Simple Path publisher #
#########################
class Simple_path_simulator():
    ##################
    # Initialization #
    ##################
    def __init__(self):
        rospy.init_node('Simple_Path_Publisher', anonymous=True)
        self.r = rospy.Rate(1)  # 50hz
        #Initialize odometry header
        self.path_header = Header()
        self.path_header.seq = 0
        self.path_header.stamp = rospy.Time.now()
        self.path_header.frame_id = "start"
        self.path = Path()
        self.path.header = self.path_header
        #get pose data from csv
        self.csv_path_data = pd.read_csv("c")
        print(self.csv_path_data)
        pose_list = self.get_poses_from_csvdata()
        self.path.poses =pose_list
        #initialize publisher
        self.path_pub = rospy.Publisher("path_whill", Path, queue_size=50)
	
    #############################################
    # Update odometry form User request cmd_vel #
    #############################################
    def get_poses_from_csvdata(self):
        #Get poses from csv data
        poses_list = []
        for indx in range(len(self.csv_path_data)):
            temp_pose = PoseStamped()
            #print(len(self.csv_path_data))
            temp_pose.pose.position.x = self.csv_path_data["x"][indx]
            #print(temp_pose.pose.position.x)
            temp_pose.pose.position.y = self.csv_path_data["y"][indx]
            temp_pose.pose.position.z = self.csv_path_data["z"][indx]
   	   
            temp_pose.pose.orientation.x = self.csv_path_data["w0"][indx]
            temp_pose.pose.orientation.y = self.csv_path_data["w1"][indx]
            temp_pose.pose.orientation.z = self.csv_path_data["w2"][indx]
            temp_pose.pose.orientation.w = self.csv_path_data["w3"][indx]
            #temp_pose.pose.orientation.w = self.csv_path_data["w3"][indx]
            temp_pose.header = self.path_header
            temp_pose.header.seq = indx
            poses_list.append(temp_pose)
	    print(poses_list)
        return poses_list
    def publish_path_topic(self):
        self.path_pub.publish(self.path)
        self.r.sleep()       ​
        
if __name__ == '__main__':
    print('Path Publisher is Started...')
    test = Simple_path_simulator()
    try:
        while not rospy.is_shutdown():
            test.publish_path_topic()
    except KeyboardInterrupt:
        print("finished!")
