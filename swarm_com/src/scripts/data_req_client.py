#!/usr/bin/env python3

import rospy
from swarm_com.srv import Detatch_Request 

def request_data_client():
    rospy.wait_for_service('request_detatch_data')
    try:
        request_data = rospy.ServiceProxy('request_detatch_data', Detatch_Request)
        response = request_data()
        return response.data_received
    except rospy.ServiceException as e:
        print("Service call failed:", e)

if __name__ == '__main__':
    rospy.init_node('data_request_client')
    data_received = request_data_client()
    print("Data received:", data_received)


