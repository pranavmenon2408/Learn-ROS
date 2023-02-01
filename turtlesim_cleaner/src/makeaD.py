#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

PI=3.1415926535897

    
def makingD():
     
     rospy.init_node('makeaD',anonymous=True)
     pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
     vel_msg=Twist()
     
     vel_msg.linear.y=0
     vel_msg.linear.z=0
     vel_msg.angular.x=0
     vel_msg.angular.y=0
     vel_msg.linear.x=0
     t0=rospy.Time.now().to_sec()
     current_angle=0
     vel_msg.angular.z=2*PI/180
     rate=rospy.Rate(10)
     while(current_angle<PI/2):
         pub.publish(vel_msg)
         t1=rospy.Time.now().to_sec()
         current_angle=2*PI*(t1-t0)/180
         rate.sleep()
     vel_msg.angular.z=0
     pub.publish(vel_msg)
     current_dist=0
     vel_msg.linear.x=1
     t2=rospy.Time.now().to_sec()
     while(current_dist<4):
           pub.publish(vel_msg)
           t3=rospy.Time.now().to_sec()
           current_dist=1*(t3-t2)
           rate.sleep()
     vel_msg.linear.x=0
     pub.publish(vel_msg)
     current_angle1=0
     vel_msg.angular.z=-(2*PI/180)
     t4=rospy.Time.now().to_sec()
     while(current_angle1<PI/2):
         pub.publish(vel_msg)
         t5=rospy.Time.now().to_sec()
         current_angle1=2*PI*(t5-t4)/180
         rate.sleep()
     vel_msg.angular.z=0
     pub.publish(vel_msg) 
     vel_msg.linear.x=2*PI/180
     vel_msg.angular.z=-(PI/180)
     current_angle2=0
     t6=rospy.Time.now().to_sec()
     while(current_angle2<PI):
         pub.publish(vel_msg)
         t7=rospy.Time.now().to_sec()
         current_angle2=PI*(t7-t6)/180
         rate.sleep()
     vel_msg.linear.x=0
     vel_msg.angular.z=0
     pub.publish(vel_msg)
     rospy.spin()
if __name__ == '__main__':
   try:
      makingD()
   except rospy.ROSInterruptException:
      pass                     
     
