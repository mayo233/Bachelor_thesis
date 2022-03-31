#!/usr/bin/env python
import rospy
import tf

            
            
if __name__ == '__main__':
	# initialize node
	rospy.init_node('tf_listener')
	listener = tf.TransformListener()
	rate = rospy.Rate(1.0)
    	while not rospy.is_shutdown():
	  try:
		# listen to transform
		(trans,rot) = listener.lookupTransform('/newroom_startB', '/base_link', rospy.Time(0))
		# print the transform
		#rospy.loginfo('---------')
    		a=str(trans[0])
            
		b=str(trans[1])
		print(str(trans))
		#rospy.loginfo('Rotation: ' + str(rot))
          except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
              continue
        # sleep to control the node frequency
          rate.sleep()
