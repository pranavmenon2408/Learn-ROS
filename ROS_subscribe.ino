#include <str_msgs/String.h>
#include <ros.h>

ros::NodeHandle nh;
void messageCb(const std_msgs::String& msg){
Serial.println(msg.data)
}
ros::Subscriber<std_msgs::String> sub("/arduino_read",&messageCb);

void setup()
{
  Serial.begin(57600);
  nh.initNode();
  nh.subscribe(sub);
}
void loop()
{
  nh.spinOnce();
  delay(1);
}