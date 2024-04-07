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
pygame.display.set_caption("Right_Drone_Grid")

obstacles =[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15), (0, 16), (0, 17), 
 (0, 18), (0, 19), (0, 20), (0, 21), (0, 22), (0, 23), (0, 24), (0, 25), (0, 26), (0, 27), (0, 28), (0, 29), (0, 30), (0, 31), (0, 32), (0, 33), (0, 34),
     (0, 35), (0, 36), (0, 37), (0, 38), (0, 39), (1, 0), (1, 15), (1, 16), (1, 17), (1, 18), (1, 23), (1, 24), (1, 25), (1, 26), (1, 31),
     (1, 32), (1, 33), (1, 34), (1, 39), (2, 0), (2, 15), (2, 16), (2, 17), (2, 18), (2, 23), (2, 24), (2, 25), (2, 26), (2, 31), (2, 32), (2, 33),
      (2, 34), (2, 39), (2, 39), (3, 0), (3, 15), (3, 16), (3, 17), (3, 18), (3, 23), (3, 24), (3, 25), (3, 26), (3, 31), (3, 32), (3, 33), (3, 34), (3, 39), 
       (4, 0), (4, 15), (4, 16), (4, 17), (4, 18), (4, 23), (4, 24), (4, 25), (4, 26), (4, 31), (4, 32), (4, 33), (4, 34), (4, 39), (5, 0),
       (5, 10), (5, 15), (5, 16), (5, 17), (5, 18), (5, 23), (5, 24), (5, 25), (5, 26), (5, 31), (5, 32), (5, 33), (5, 34), (5, 39), (6, 0), (6, 10),
        (6, 15), (6, 16), (6, 17), (6, 18), (6, 23), (6, 24), (6, 25), (6, 26), (6, 31), (6, 32), (6, 33), (6, 34), (6, 39), (7, 0), (7, 10), (7, 15),
         (7, 16), (7, 17), (7, 18), (7, 23), (7, 24), (7, 25), (7, 26), (7, 31), (7, 32), (7, 33), (7, 34), (7, 39), (8, 0), (8, 10), (8, 15), (8, 16),
          (8, 17), (8, 18), (8, 23), (8, 24), (8, 25), (8, 26), (8, 31), (8, 32), (8, 33), (8, 34), (8, 39), (9, 0), (9, 10), (9, 15), (9, 16), (9, 17),
           (9, 18), (9, 23), (9, 24), (9, 25), (9, 26), (9, 31), (9, 32), (9, 33), (9, 34), (9, 39), (10, 0), (10, 10), (10, 15), (10, 16), (10, 17),
      (10, 18), (10, 23), (10, 24), (10, 25), (10, 26), (10, 31), (10, 32), (10, 33), (10, 34), (10, 39), (11, 0), (11, 10), (11, 15), (11, 16),
       (11, 17), (11, 18), (11, 23), (11, 24), (11, 25), (11, 26), (11, 31), (11, 32), (11, 33), (11, 34), (11, 39), (12, 0), (12, 10), (12, 15),
        (12, 16), (12, 17), (12, 18), (12, 23), (12, 24), (12, 25), (12, 26), (12, 31), (12, 32), (12, 33), (12, 34), (12, 39), (13, 0), (13, 10),
         (13, 15), (13, 16), (13, 17), (13, 18), (13, 23), (13, 24), (13, 25), (13, 26), (13, 31), (13, 32), (13, 33), (13, 34), (13, 39), (14, 0),
          (14, 10), (14, 15), (14, 16), (14, 17), (14, 18), (14, 23), (14, 24), (14, 25), (14, 26), (14, 31), (14, 32), (14, 33), (14, 34), (14, 39),
           (15, 0), (15, 10), (15, 15), (15, 16), (15, 17), (15, 18), (15, 23), (15, 24), (15, 25), (15, 26), (15, 31), (15, 32), (15, 33), (15, 34),
            (15, 39), (16, 0), (16, 10), (16, 15), (16, 16), (16, 17), (16, 18), (16, 23), (16, 24), (16, 25), (16, 26), (16, 31), (16, 32), (16, 33), (16, 34),
             (16, 39), (17, 0), (17, 10), (17, 15), (17, 16), (17, 17), (17, 18), (17, 23), (17, 24), (17, 25), (17, 26), (17, 31), (17, 32), (17, 33),
              (17, 34), (17, 39), (18, 0), (18, 10), (18, 15), (18, 16), (18, 17), (18, 18), (18, 23), (18, 24), (18, 25), (18, 26), (18, 31), (18, 32),
               (18, 33), (18, 34), (18, 39), (19, 0), (19, 10), (19, 15), (19, 16), (19, 17), (19, 18), (19, 23), (19, 24), (19, 25), (19, 26),
                (19, 31), (19, 32), (19, 33), (19, 34), (19, 39), (20, 0), (20, 10), (20, 15), (20, 16), (20, 17), (20, 18), (20, 23), (20, 24),
                 (20, 25), (20, 26), (20, 31), (20, 32), (20, 33), (20, 34), (20, 39), (21, 0), (21, 10), (21, 15), (21, 16), (21, 17), (21, 18),
                  (21, 23), (21, 24), (21, 25), (21, 26), (21, 31), (21, 32), (21, 33), (21, 34), (21, 39), (22, 0), (22, 10), (22, 39),
                   (23, 0), (23, 10), (23, 39), (24, 0), (24, 10), (24, 39), (25, 0), (25, 10), (26, 0), (26, 10), (27, 0), (27, 10), (28, 0),
                    (28, 10), (29, 0), (29, 1), (29, 2), (29, 3), (29, 4), (29, 5), (29, 6), (29, 7), (29, 8), (29, 9), (29, 10), (29, 10), (29, 11),
                     (29, 12), (29, 13), (29, 14), (29, 15), (29, 16), (29, 17), (29, 18), (29, 19), (29, 20), (29, 21), (29, 22), (29, 23), (29, 24), (29, 25),
                      (29, 26), (29, 27), (29, 28), (29, 29), (29, 30), (29, 31), (29, 32), (29, 33), (29, 34), (29, 35), (29, 36), (29, 37), (29, 38),
                      (6,4),(6,5),(7,4),(7,5),(8,4),(8,5),(13,6),(13,7),(14,6),(14,7),(15,6),(15,7),(16,6),(16,7),(22,3),(22,4),(23,3),(23,4),
                      (24,6),(24,7),(25,6),(25,7)]

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
        self.map_pub = rospy.Publisher("Right_Data",Int32MultiArray,queue_size = 1)

        self.map_data = Int32MultiArray()
        self.map_data.layout.dim.append(MultiArrayDimension())
        self.map_data.layout.dim[0].label = "len"

        self.lf = 0
        self.tf = 0
        self.rf = 0
        self.bf = 0
        

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
            slave_sub = rospy.Subscriber('Right_Detatch_Data',Int32MultiArray,self.subscriber_callback)
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
            slave_sub = rospy.Subscriber('Right_Detatch_Data',Int32MultiArray,self.subscriber_mast_callback)
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

        for i in range(x_dist-1):
            self.y-=1
            pygame.draw.rect(screen, RED, ((self.x) * CELL_SIZE, (self.y) * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
            pygame.display.flip()
            time.sleep(0.5)
        for i in range(y_dist):
            self.x+=1
            pygame.draw.rect(screen, RED, ((self.x) * CELL_SIZE, (self.y) * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
            pygame.display.flip()
            time.sleep(0.5)
        self.x+= 1
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
        backtrack_path = []
        break_flag = 0
        self.x = init_point[0] 
        self.y = init_point[1]
        self.checkpoint = [self.x,self.y]
        self.loop_checkpoint=(0,0)
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

            
            neighbor_indices_left = []
            neighbor_indices_right = []
            neighbor_indices_top = []
            neighbor_indices_bottom = []
            if lidar_scan[3, 2] != 1:  
                neighbor_indices_left.append((-1,0))
            if lidar_scan[2, 2] != 1:  
                neighbor_indices_left.append((- 1,- 1))
            if lidar_scan[4, 2] != 1:  
                neighbor_indices_left.append((-1, 1))

            if lidar_scan[2, 3] != 1:  
                neighbor_indices_top.append((0,-1))
            if lidar_scan[2, 2] != 1:  
                neighbor_indices_top.append((- 1,- 1))
            if lidar_scan[2, 4] != 1:  
                neighbor_indices_top.append((1, -1))

            if lidar_scan[2, 4] != 1:  
                neighbor_indices_right.append((1,-1))
            if lidar_scan[3, 4] != 1:  
                neighbor_indices_right.append((1,0))
            # if lidar_scan[4, 4] != 1:  
            #     neighbor_indices_right.append((1, 1))
            
            if lidar_scan[4, 2] != 1:  
                neighbor_indices_bottom.append((-1,1))
            if lidar_scan[4, 3] != 1:  
                neighbor_indices_bottom.append((0,1))
            if lidar_scan[4, 4] != 1:  
                neighbor_indices_bottom.append((1, 1))
            print(neighbor_indices_left)
            print(neighbor_indices_top)
            print(neighbor_indices_bottom)
            print(neighbor_indices_right)
            
            # print(np.array(lidar_scan))
            if len(neighbor_indices_left) > 0 and self.lf == 0:
                print("trying_left")
                choice = neighbor_indices_left[random.randint(0,len(neighbor_indices_left)-1)]
                
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
                backtrack_path.append((self.y + self.vel_y,self.x+self.vel_x))
                
                
                if ((self.y + self.vel_y,self.x+self.vel_x) not in obstacles and 
                    self.x + self.vel_x <29 and self.y + self.vel_y <29 and 
                    self.x + self.vel_x >0 and self.y + self.vel_y >0 ) :
                    self.x += self.vel_x
                    self.y += self.vel_y
                    time.sleep(0.5)
                    pygame.draw.rect(screen, RED, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
                    pygame.display.flip()

                if self.x == 1:
                    loop_checkpoint = (self.x,self.y)
                    self.lf = 1
                
            elif len(neighbor_indices_top) > 0 and self.tf == 0 and self.lf == 1:
                print("trying_top")
                choice = neighbor_indices_top[random.randint(0,len(neighbor_indices_top)-1)]
                
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
                
                if self.y == 1:
                    self.tf = 1
                

            elif len(neighbor_indices_right) > 0 and self.rf == 0 and self.tf == 1 and self.lf == 1:
                print("trying_right")
                chc = neighbor_indices_right[random.randint(0,len(neighbor_indices_right)-1)]
                
                self.vel_x = chc[0]
                self.vel_y = chc[1]
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
                
                if self.x == 28:
                    self.rf = 1

            elif len(neighbor_indices_bottom) > 0 and self.tf == 1 and self.lf == 1 and self.rf == 1:
                print("trying_bottom")
                choice = neighbor_indices_bottom[random.randint(0,len(neighbor_indices_bottom)-1)]
                
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
                if len(neighbor_indices_bottom) == 0:
                    self.bf = 1
            else:
                print("Exploration Complete, Backtracking")
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