#!/usr/bin/env python
import rospy
from ros_package.msg import custom

def talk_to_me():
     pub =rospy.Publisher('chatter', custom, queue_size=10)
     rospy.init_node('publisher',anonymous=True)
     rate =rospy.Rate(10)
     while not rospy.is_shutdown():
          msg =custom()
          msg.message="Showing integer and float values: "
          msg.dec=34.5
          msg.num=500
          rospy.loginfo(msg)
          pub.publish(msg)
          rate.sleep()
if __name__ == '__main__':
   try:
      talk_to_me()
   except rospy.ROSInterruptException:
      pass     
      
