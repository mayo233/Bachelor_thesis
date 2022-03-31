#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

with open("/home/suzukamayo/ros_ws/lidar/whill_ws/src/pure_pursuit/1_24_whill_pathB.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        string = ",".join(row)
        print(string.replace(']', '')) 
        #print(string.replace('[', '')) 
        #print(row.replace(' ', ''))
        
     	
