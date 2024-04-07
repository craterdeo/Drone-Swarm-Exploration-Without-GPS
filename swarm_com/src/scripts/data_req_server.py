#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from swarm_com.srv import Detatch_Request, Detatch_Response

class DataRequestServer:
    def __init__(self):
        rospy.init_node('data_request_server')
        self.data = 0
        self.subscriber = rospy.Subscriber('Detatch_Data', Int32, self.data_callback)
        rospy.Service('request_detatch_data', Detatch_Request, self.handle_request_data)

    def data_callback(self, msg):
        self.data = msg.data

    def handle_request_data(self, request):
        response = Detatch_Response()
        response.data_received = self.data
        return response

if __name__ == '__main__':
    try:
        data_request_server = DataRequestServer()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
