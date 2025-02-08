#!/usr/bin/env python3
import rospy

from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2


def camera_publisher():
    rospy.init_node("camera_node",anonymous=True)
    pub = rospy.Publisher("camera_image_raw" , Image , queue_size=10)
    rate = rospy.Rate(10)
    bridge = CvBridge()

    video = cv2.VideoCapture(0)

    while not rospy.is_shutdown():
        ret , frame = video.read()
        if not ret:
            rospy.logerr("Failed Bsdk")
            break
        img_msg = bridge.cv2_to_imgmsg(frame)
        pub.publish(img_msg)

        rate.sleep()

    video.release()

if __name__ =="__main__":
    try:
     camera_publisher()
    except rospy.ROSInterruptException:
        pass

