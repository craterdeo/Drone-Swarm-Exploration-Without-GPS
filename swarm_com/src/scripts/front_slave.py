#!usr/bin/env python3

import rospy
import numpy as np
import pygame 
import sys
import os
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import MultiArrayDimension
import time
import random

# pygame.init()

WIDTH, HEIGHT = 30, 40
CELL_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (0,255, 0)
GREEN = (255,0,0)
BLUE = (150, 150, 255)

screen = pygame.display.set_mode((WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE))
pygame.display.set_caption("Front_Drone_Grid")

obstacles = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0), (15, 0),
            (16, 0), (17, 0), (18, 0), (19, 0), (20, 0), (21, 0), (22, 0), (23, 0), (24, 0), (25, 0), (26, 0), (27, 0), (28, 0), (29, 0),
            (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15),
            (0, 16), (0, 17), (0, 18), (0, 19), (0, 20), (0, 21), (0, 22), (0, 23), (0, 24), (0, 25), (0, 26), (0, 27), (0, 28), (0, 29),
            (0, 29), (1, 29), (2, 29), (3, 29), (4, 29), (5, 29), (6, 29), (7, 29), (8, 29), (9, 29), (10, 29), (11, 29), (12, 29), (13, 29), 
            (14, 29), (15, 29), (16, 29), (17, 29), (18, 29), (19, 29), (20, 29), (21, 29), (22, 29), (23, 29), (24, 29),
            (2,26),(2,26),(3,27),(4,28),(17,27),(18,27),(10,28),
            (5,20),(5,19),(7,18),(7,17),(19,20),(20,19),(11,20),
            (5,9),(5,10),(7,11),(7,10),(19,9),(20,10),(11,20),
            (0, 0), (1, 0), (2, 0),(3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0), (15, 0),
            (16, 0), (17, 0), (18, 0), (19, 0), (20, 0), (21, 0), (22, 0), (23, 0), (24, 0), (25, 0), (26, 0), (27, 0), (28, 0), (29, 0),
            (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15),
            (0, 16), (0, 17), (0, 18), (0, 19), (0, 20), (0, 21), (0, 22), (0, 23), (0, 24), (0, 25), (0, 26), (0, 27), (0, 28), (0, 29),
            (0, 29), (1, 29), (2, 29), (3, 29), (4, 29), (5, 29), (6, 29), (7, 29), (8, 29), (9, 29), (10, 29), (11, 29), (12, 29), (13, 29), 
            (14, 29), (15, 29), (16, 29), (17, 29), (18, 29), (19, 29), (20, 29), (21, 29), (22, 29), (23, 29), (24, 29),(1,5),(1,6),(1,7),(1,8),
            (2,5),(2,6),(2,7),(2,8),(3,5),(3,6),(3,7),(3,8),(4, 5), (4, 6), (4, 7),(4, 8), (5, 5), (5, 6), (5, 7), (5, 8), (6, 5), (6, 6), (6, 7), 
            (6, 8), (7, 5), (7, 6), (7, 7), (7, 8), (8, 5), (8, 6), (8, 7),(8, 8), (9, 5), (9, 6), (9, 7), (9, 8), (10, 5), (10, 6), (10, 7), 
            (10, 8), (11, 5), (11, 6), (11, 7), (11, 8), (12, 5), (12, 6), (12, 7), (12, 8), (13, 5), (13, 6), (13, 7), (13, 8), (14, 5), (14, 6),
            (14, 7), (14, 8), (15, 5), (15, 6), (15, 7), (15, 8), (16, 5), (16, 6), (16, 7), (16, 8), (17, 5), (17, 6), (17, 7), (17, 8),
            (18, 5), (18, 6), (18, 7), (18, 8), (19, 5), (19, 6), (19, 7), (19, 8), (20, 5), (20, 6), (20, 7), (20, 8), (21, 5), (21, 6), 
            (21, 7), (21, 8),(1,13),(1,14),(1,15),(1,16),(2,13),(2,14),(2,15),(2,16),(3,13),(3,14),(3,15),(3,16), (4, 13), (4, 14), (4, 15), 
            (4, 16),(5, 13), (5, 14), (5, 15), (5, 16), (6, 13), (6, 14),(6, 15), (6, 16), (7, 13), (7, 14), (7, 15), (7, 16), (8, 13), 
            (8, 14),(8, 15), (8, 16), (9, 13), (9, 14), (9, 15), (9, 16), (10, 13), (10, 14), (10, 15), (10, 16), (11, 13), (11, 14), (11, 15),
            (11, 16), (12, 13), (12, 14), (12, 15), (12, 16), (13, 13), (13, 14), (13, 15), (13, 16), (14, 13), (14, 14), (14, 15), 
            (14, 16), (15, 13), (15, 14), (15, 15), (15, 16), (16, 13), (16, 14), (16, 15), (16, 16), (17, 13), (17, 14), (17, 15), 
            (17, 16), (18, 13), (18, 14), (18, 15), (18, 16), (19, 13), (19, 14), (19, 15), (19, 16), (20, 13), (20, 14), (20, 15),
            (20, 16), (21, 13), (21, 14), (21, 15), (21, 16),(1,21),(1,22),(1,23),(1,24),(2,21),(2,22),(2,23),(2,24),(3,21),(3,22),(3,23),(3,24),
            (4, 21), (4, 22), (4, 23), (4, 24), (5, 21), (5, 22), (5, 23), (5, 24),
            (6, 21), (6, 22), (6, 23), (6, 24), (7, 21), (7, 22), (7, 23), (7, 24), (8, 21), (8, 22), (8, 23), (8, 24), (9, 21),
            (9, 22), (9, 23), (9, 24), (10, 21), (10, 22), (10, 23), (10, 24), (11, 21), (11, 22), (11, 23), (11, 24), (12, 21), 
            (12, 22), (12, 23), (12, 24), (13, 21), (13, 22), (13, 23), (13, 24), (14, 21), (14, 22), (14, 23), (14, 24), (15, 21),
            (15, 22), (15, 23), (15, 24), (16, 21), (16, 22), (16, 23), (16, 24), (17, 21), (17, 22), (17, 23), (17, 24), 
            (18, 21), (18, 22), (18, 23), (18, 24), (19, 21), (19, 22), (19, 23), (19, 24), (20, 21), (20, 22), (20, 23), 
            (20, 24), (21, 21), (21, 22), (21, 23), (21, 24)]
grid = np.zeros((40,30))

for i in range(30):
    for j in range(40):
        if (i,j) in obstacles:
          grid[j][i] = 1
        else:
          grid[j][i] = 2

class Slave():
    def __init__(self,name,screen):
        self.name = name
        self.vel_x = -1
        self.vel_y = 0
        self.det_data = None
        self.mast_loc = None
        self.screen = screen
        self.x = 0
        self.y = 0
        self.map = np.zeros((30,30))
        self.obstacles = []
        self.checkpoint = [0,0]
        self.grid = grid
        self.map_pub = rospy.Publisher("Front_Data",Int32MultiArray,queue_size = 1)

        self.map_data = Int32MultiArray()
        self.map_data.layout.dim.append(MultiArrayDimension())
        self.map_data.layout.dim[0].label = "len"
        

    def subscriber_callback(self,data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        self.det_data = data.data
        print(data.data)
        # rospy.signal_shutdown("Message Received")
        
    def subscribe_init(self):
        rospy.init_node("Slave_Drone",anonymous=True)
        print("Subscribing")
        print(self.det_data)
        rate = rospy.Rate(3)
        while self.det_data == None:            
            slave_sub = rospy.Subscriber('Front_Detatch_Data',Int32MultiArray,self.subscriber_callback)
            rate.sleep()

    def subscriber_mast_callback(self,data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        self.mast_loc = data.data
        print(data.data)
        rospy.signal_shutdown("Message Received")

    def subscribe_mast_init(self):
        rospy.init_node("Slave_Drone",anonymous=True)
        print("Subscribing _ Master")
        print(self.mast_loc)
        rate = rospy.Rate(3)
        while self.mast_loc == None:         
            slave_sub = rospy.Subscriber('Front_Detatch_Data',Int32MultiArray,self.subscriber_mast_callback)
            rate.sleep()
    

    def get_lidar_scan(matrix, x, y):
        lidar_scan = []
        rows, cols = len(matrix), len(matrix[0])
        
        # Calculate starting and ending indices for the lidar_scan
        start_row = max(0, x - 3)
        end_row = min(rows - 1, x + 3)
        start_col = max(0, y - 3)
        end_col = min(cols - 1, y + 3)
        
        # Extract the lidar_scan
        for i in range(start_row, end_row + 1):
            row = []
            for j in range(start_col, end_col + 1):
                row.append(matrix[i][j])
            lidar_scan.append(row)
    
        return lidar_scan
    
    def path_to_master(self):
        x_dist = abs(self.mast_loc[1] - self.checkpoint[1])
        y_dist = abs(self.mast_loc[0] - self.checkpoint[0])
        print(self.checkpoint)
        print("dist:",x_dist,y_dist,self.x,self.y)

        for i in range(x_dist):
            self.y-=1
            pygame.draw.rect(screen, RED, ((self.x) * CELL_SIZE, (self.y) * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
            pygame.display.flip()
            time.sleep(0.5)
        for i in range(y_dist):
            self.x+=1
            pygame.draw.rect(screen, RED, ((self.x) * CELL_SIZE, (self.y) * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
            pygame.display.flip()
            time.sleep(0.5)
        self.y-= 1
        pygame.draw.rect(screen, RED, ((self.x) * CELL_SIZE, (self.y) * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
        pygame.display.flip()
        time.sleep(0.5)

        print("Master Found")
    
    def get_safe_points(matrix, x, y):
        neighbor_indices = []
        if matrix[x, y - 1] != 1:  # Left
            neighbor_indices.append((x, y - 1))
        if matrix[x - 1, y - 1] != 1:  # Top Left
            neighbor_indices.append((x - 1, y - 1))
        if matrix[x + 1, y - 1] != 1:  # Bottom Left
            neighbor_indices.append((x + 1, y - 1))
        if matrix[x - 1, y] != 1:  # Top
            neighbor_indices.append((x - 1, y))
        if matrix[x + 1, y] != 1:  # Bottom
            neighbor_indices.append((x + 1, y))
        return neighbor_indices
    
    def slam(self, door_dist,init_point):      
        path_forward = []  
        break_flag = 0
        self.x = init_point[0] 
        self.y = init_point[1]
        self.checkpoint = [self.x,self.y]
        for i in range(door_dist-1):
            for i, j in [(-1, 0)]:  # Coordinates for 4 surrounding robots
                pygame.draw.rect(screen, RED, ((self.x + i) * CELL_SIZE, (self.y + j) * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
              # pygame.draw.rect(screen, WHITE, ((new_pose_x+ i) * CELL_SIZE, (new_pose_y + j) * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
            time.sleep(0.5)
            path_forward.append((self.y + self.vel_y,self.x+self.vel_x))
            self.x += self.vel_x
            self.y += self.vel_y 
            pygame.display.flip()
            
        print(self.checkpoint)
        print(self.x,self.y)
        while break_flag != 1:
            print(break_flag)
            print(self.x,self,y)
            # Extract the lidar_scan
            padded_matrix = np.pad(self.grid, 3, mode='constant', constant_values=1)
            extracted_array = padded_matrix[self.y:self.y+7, self.x:self.x+7]
            lidar_scan =  extracted_array
            print(lidar_scan)

            
            neighbor_indices = []
            if lidar_scan[3, 2] != 1:  
                neighbor_indices.append((-1,0))
            if lidar_scan[2, 2] != 1:  
                neighbor_indices.append((- 1,- 1))
            if lidar_scan[4, 2] != 1:  
                neighbor_indices.append((-1, 1))
            print(neighbor_indices)
            
            # print(np.array(lidar_scan))
            if len(neighbor_indices) > 0:
                choice = neighbor_indices[random.randint(0,len(neighbor_indices)-1)]
                
                self.vel_x = choice[0]
                self.vel_y = choice[1]
                # print(self.vel_x,self.vel_y)
                print(self.x+self.vel_x,self.vel_y+self.y)
                obstacles = []
                for i in range(len(lidar_scan)):
                    for j in range(len(lidar_scan[0])):
                        if lidar_scan[i][j] == 1:
                            if (self.y+i-3,self.x+j-3) not in obstacles:
                                obstacles.append((self.y+i-3,self.x+j-3))
                print(obstacles)
                self.obstacles.append(obstacles)
                path_forward.append((self.y + self.vel_y,self.x+self.vel_x))
                
                if ((self.y + self.vel_y,self.x+self.vel_x) not in obstacles and 
                    self.x + self.vel_x <29 and self.y + self.vel_y <29 and 
                    self.x + self.vel_x >0 and self.y + self.vel_y >0 ) :
                    self.x += self.vel_x
                    self.y += self.vel_y
                    time.sleep(0.5)
                    pygame.draw.rect(screen, RED, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
                    pygame.display.flip()
            else:
                print("Obstacles Everywhere, Backtracking")
                backtrack = path_forward[::-1]
                for i,j in backtrack:
                    time.sleep(0.5)
                    self.x = j 
                    self.y = i
                    print(self.x+1,self.y,self.checkpoint)
                    pygame.draw.rect(screen, GREEN, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
                    pygame.display.flip()
                    if (self.x+1 == self.checkpoint[0]) and (self.y == self.checkpoint[1]):
                        break_flag = 1
  
        return obstacles
      
def flatten_tuples(list_of_tuples):
    return [num for tup in list_of_tuples for num in tup]    

left_drone = Slave("left",screen)
left_drone.subscribe_init()
print(left_drone.det_data)
print("Subscribed")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    for x in range(0, WIDTH * CELL_SIZE, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT * CELL_SIZE))
    for y in range(0, HEIGHT * CELL_SIZE, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH * CELL_SIZE, y))
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, (obstacle[0] * CELL_SIZE, obstacle[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    left_drone.slam(left_drone.det_data[-1],[left_drone.det_data[0],left_drone.det_data[1]])
    print("Slam_Complete, Waiting for Master_Callback")
    running = False

left_drone.obstacles = flatten_tuples(left_drone.obstacles)
#back_to_master
left_drone.subscribe_mast_init()
print(left_drone.mast_loc)

screen = pygame.display.set_mode((WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE))
pygame.display.set_caption("Left_Robot_Grid")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    for x in range(0, WIDTH * CELL_SIZE, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT * CELL_SIZE))
    for y in range(0, HEIGHT * CELL_SIZE, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH * CELL_SIZE, y))
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, (obstacle[0] * CELL_SIZE, obstacle[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    left_drone.path_to_master()
    print("Publishing Map")
    left_drone.map_data.layout.dim[0].size = len(left_drone.obstacles)
    left_drone.map_data.layout.dim[0].stride = len(left_drone.obstacles)
    left_drone.map_data.data = left_drone.obstacles
    print(left_drone.map_data)
    left_drone.map_pub.publish(left_drone.map_data)
    print("Published")
    time.sleep(20)
    running=False