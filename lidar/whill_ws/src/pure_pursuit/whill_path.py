#!/usr/bin/env python
import rospy
import tf   	

"""
def call_x(fact):
    a=(float(fact[0]))
    
def call_y(fact):
    b=(float(fact[1]))
"""
if __name__ == '__main__':
    # initialize node
    #global flag
    
    rospy.init_node('tf_listener')
    listener = tf.TransformListener()
    rate = rospy.Rate(1.0)
    # loop forever until roscore or this node is down
    while not rospy.is_shutdown():
        try:
            # listen to transform
            (trans,rot) = listener.lookupTransform('/newroom_startB', '/base_link', rospy.Time(0))
            # print the transform
            #rospy.loginfo('---------')
            #a=str(trans[0])
            
            #b=str(trans[1])
            #call_x(str(trans[0]))
            #call_y(str(trans[1]))
            
            print(str(trans))
            #rospy.loginfo('Rotation: ' + str(rot))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        # sleep to control the node frequency
        rate.sleep()
