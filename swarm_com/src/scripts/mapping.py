## INCOMPLETE 
#!/usr/bin/env python3

import rospy
import math
from door_detector import door_detector
import numpy as np
import cv2
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import MultiArrayDimension
import pygame
import time
import sys

class Map_Generator:

    def __init__(self,size):
        self.map = []
        self.left_data = None
        self.right_data = None
        self.front_data = None
        self.back_data = None
        self.obstacles = []

    def left_callback(self,data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        self.left_data = data.data
        print(data.data)
        # rospy.signal_shutdown("Message Received")
        
    def left_init(self):
        rospy.init_node("Map_Generator",anonymous=True)
        print("Subscribing")
        rate = rospy.Rate(3)
        while self.left_data == None:            
            slave_sub = rospy.Subscriber('Left_Data',Int32MultiArray,self.left_callback)
            rate.sleep()
    
    def right_callback(self,data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        self.right_data = data.data
        print(data.data)
        # rospy.signal_shutdown("Message Received")
        
    def right_init(self):
        rospy.init_node("Map_Generator",anonymous=True)
        print("Subscribing")
        rate = rospy.Rate(3)
        while self.right_data == None:            
            slave_sub = rospy.Subscriber('Right_Data',Int32MultiArray,self.right_callback)
            rate.sleep()

    def front_callback(self,data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        self.front_data = data.data
        print(data.data)
        # rospy.signal_shutdown("Message Received")
        
    def front_init(self):
        rospy.init_node("Map_Generator",anonymous=True)
        print("Subscribing")
        rate = rospy.Rate(3)
        while self.front_data == None:            
            slave_sub = rospy.Subscriber('Front_Data',Int32MultiArray,self.front_callback)
            rate.sleep()

    def back_callback(self,data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        self.back_data = data.data
        print(data.data)
        # rospy.signal_shutdown("Message Received")
        
    def back_init(self):
        rospy.init_node("Map_Generator",anonymous=True)
        print("Subscribing")
        rate = rospy.Rate(3)
        while self.back_data == None:            
            slave_sub = rospy.Subscriber('Back_Data',Int32MultiArray,self.back_callback)
            rate.sleep()

def transpose_array(arr):
    # Use list comprehension to transpose the array
        return [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]

def merge_arrays(arr1,arr2,row_col_choice):
    if row_col_choice == 1: #merge_by_row
        for i in arr1:
            if i in arr2:
                k1 = arr1.index(i)
                k2 = arr2.index(i)
                print(k1,k2)
                if k1 == len(arr1)-1 and k2 == 0:
                    arr1.extend(arr2[1:])
                    return arr1
                elif k1 == 0 and k2 == len(arr2[1:])-1:
                    arr2.extend(arr1)
                    return arr2
            else:
                print("Cannot be merged")
    elif row_col_choice == 0:
        arr1 = transpose_array(arr1)
        print(arr1)
        arr2 = transpose_array(arr2)
        print(arr2)
        for i in arr1:
            if i in arr2:
                k1 = arr1.index(i)
                k2 = arr2.index(i)
                print(k1,k2)
                if k1 == len(arr1)-1 and k2 == 0:
                    arr1.extend(arr2[1:])
                    return transpose_array(arr1)
                elif k1 == 0 and k2 == len(arr2[1:])-1:
                    arr2.extend(arr1)
                    return transpose_array(arr2)
            else:
                print("Cannot be merged")

mg = Map_Generator((30,30))

mg.left_init()
mg.right_init()
mg.front_init()
mg.back_init()

if mg.left_data!= None:
    mg.obstacles.append(mg.left_data)
if mg.back_data!= None:
    mg.obstacles.append(mg.back_data)
if mg.front_data!= None:
    mg.obstacles.append(mg.front_data)
if mg.right_data!= None:
    mg.obstacles.append(mg.right_data)



print(mg.obstacles)

map = mg.obstacles[0]
for i in range(len(mg.obstacles)-1):
    map =  merge_arrays(map,i+1)

print(map)

    
