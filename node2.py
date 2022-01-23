#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def call_back(data):
    print("Recieved message: ",data.data)

def node2():
    rospy.init_node('Node2', anonymous=True)
    pub = rospy.Publisher('Talker2', String, queue_size=10)
    rospy.Subscriber('Talker1', String, call_back)
    while not rospy.is_shutdown():
	message=input()
	pub.publish(message)

    
    rospy.spin()

if __name__ == "__main__":
    try:
	node2()
    except rospy.ROSInterruptException:
	pass
