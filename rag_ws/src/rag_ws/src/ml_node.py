#!/usr/bin/env python3
import rospy

from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2


def feed_callback(msg):
    bridge = CvBridge()

     
    feed = bridge.imgmsg_to_cv2(msg)
    cv2.imshow("Camera_feed" , feed)
    if cv2.waitKey(1) == ord('q'):
        rospy.signal_shutdown("Shutting Down")
def camera_subscriber():
    rospy.init_node("ml_node", anonymous=True)
    rospy.Subscriber("camera_image_raw",Image , feed_callback)

    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    camera_subscriber()

