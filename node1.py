#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def call_back(data):
    print("Recieved message: ",data.data)

def node():
    rospy.init_node('Node1', anonymous=True)
    pub = rospy.Publisher('Talker1', String, queue_size=10)
    rospy.Subscriber('Talker2', String, call_back)
    while not rospy.is_shutdown():
        message=input()
	pub.publish(message)   
   
    rospy.spin()
if __name__ == "__main__":
    try:
	node()
    except rospy.ROSInterruptException:
	pass
