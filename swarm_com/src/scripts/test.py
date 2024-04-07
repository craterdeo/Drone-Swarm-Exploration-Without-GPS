# def slam(self, door_dist,init_point):      
#         path_forward = []  
#         break_flag = 0
#         self.x = init_point[0] 
#         self.y = init_point[1]
#         self.checkpoint = [self.x,self.y]
#         for i in range(door_dist-1):
#             for i, j in [(-1, 0)]:  # Coordinates for 4 surrounding robots
#                 pygame.draw.rect(screen, RED, ((self.x + i) * CELL_SIZE, (self.y + j) * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
#               # pygame.draw.rect(screen, WHITE, ((new_pose_x+ i) * CELL_SIZE, (new_pose_y + j) * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
#             time.sleep(0.5)
#             path_forward.append((self.y + self.vel_y,self.x+self.vel_x))
#             self.x += self.vel_x
#             self.y += self.vel_y 
#             pygame.display.flip()
            
#         print(self.checkpoint)
#         print(self.x,self.y)
#         while break_flag != 1:
#             print(break_flag)
#             print(self.x,self,y)
#             # Extract the lidar_scan
#             padded_matrix = np.pad(self.grid, 3, mode='constant', constant_values=1)
#             extracted_array = padded_matrix[self.y:self.y+7, self.x:self.x+7]
#             lidar_scan =  extracted_array
#             print(lidar_scan)

            
#             neighbor_indices_left = []
#             neighbor_indices_right = []
#             neighbor_indices_top = []
#             neighbor_indices_bottom = []
#             if lidar_scan[3, 2] != 1:  
#                 neighbor_indices_left.append((-1,0))
#             if lidar_scan[2, 2] != 1:  
#                 neighbor_indices_left.append((- 1,- 1))
#             if lidar_scan[4, 2] != 1:  
#                 neighbor_indices_left.append((-1, 1))

#             if lidar_scan[2, 3] != 1:  
#                 neighbor_indices_top.append((0,-1))
#             if lidar_scan[2, 2] != 1:  
#                 neighbor_indices_top.append((- 1,- 1))
#             if lidar_scan[2, 4] != 1:  
#                 neighbor_indices_top.append((1, -1))

#             if lidar_scan[2, 4] != 1:  
#                 neighbor_indices_right.append((1,-1))
#             if lidar_scan[3, 4] != 1:  
#                 neighbor_indices_right.append((1,0))
#             if lidar_scan[4, 4] != 1:  
#                 neighbor_indices_right.append((1, 1))
            
#             if lidar_scan[4, 2] != 1:  
#                 neighbor_indices_left.append((-1,1))
#             if lidar_scan[4, 3] != 1:  
#                 neighbor_indices_left.append((0,1))
#             if lidar_scan[4, 4] != 1:  
#                 neighbor_indices_left.append((1, 1))
#             print(neighbor_indices_left)
            
#             # print(np.array(lidar_scan))
#             if len(neighbor_indices_left) > 0:
#                 choice = neighbor_indices_left[random.randint(0,len(neighbor_indices_left)-1)]
                
#                 self.vel_x = choice[0]
#                 self.vel_y = choice[1]
#                 # print(self.vel_x,self.vel_y)
#                 print(self.x+self.vel_x,self.vel_y+self.y)
#                 obstacles = []
#                 for i in range(len(lidar_scan)):
#                     for j in range(len(lidar_scan[0])):
#                         if lidar_scan[i][j] == 1:
#                             if (self.y+i-3,self.x+j-3) not in obstacles:
#                                 obstacles.append((self.y+i-3,self.x+j-3))
#                 print(obstacles)
#                 self.obstacles.append(obstacles)
#                 path_forward.append((self.y + self.vel_y,self.x+self.vel_x))
                
#                 if ((self.y + self.vel_y,self.x+self.vel_x) not in obstacles and 
#                     self.x + self.vel_x <29 and self.y + self.vel_y <29 and 
#                     self.x + self.vel_x >0 and self.y + self.vel_y >0 ) :
#                     self.x += self.vel_x
#                     self.y += self.vel_y
#                     time.sleep(0.5)
#                     pygame.draw.rect(screen, RED, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
#                     pygame.display.flip()
                
#             elif len(neighbor_indices_top) > 0:
#                 choice = neighbor_indices_top[random.randint(0,len(neighbor_indices_top)-1)]
                
#                 self.vel_x = choice[0]
#                 self.vel_y = choice[1]
#                 # print(self.vel_x,self.vel_y)
#                 print(self.x+self.vel_x,self.vel_y+self.y)
#                 obstacles = []
#                 for i in range(len(lidar_scan)):
#                     for j in range(len(lidar_scan[0])):
#                         if lidar_scan[i][j] == 1:
#                             if (self.y+i-3,self.x+j-3) not in obstacles:
#                                 obstacles.append((self.y+i-3,self.x+j-3))
#                 print(obstacles)
#                 self.obstacles.append(obstacles)
#                 path_forward.append((self.y + self.vel_y,self.x+self.vel_x))
                
#                 if ((self.y + self.vel_y,self.x+self.vel_x) not in obstacles and 
#                     self.x + self.vel_x <29 and self.y + self.vel_y <29 and 
#                     self.x + self.vel_x >0 and self.y + self.vel_y >0 ) :
#                     self.x += self.vel_x
#                     self.y += self.vel_y
#                     time.sleep(0.5)
#                     pygame.draw.rect(screen, RED, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
#                     pygame.display.flip()

#             elif len(neighbor_indices_right) > 0:
#                 choice = neighbor_indices_right[random.randint(0,len(neighbor_indices_right)-1)]
                
#                 self.vel_x = choice[0]
#                 self.vel_y = choice[1]
#                 # print(self.vel_x,self.vel_y)
#                 print(self.x+self.vel_x,self.vel_y+self.y)
#                 obstacles = []
#                 for i in range(len(lidar_scan)):
#                     for j in range(len(lidar_scan[0])):
#                         if lidar_scan[i][j] == 1:
#                             if (self.y+i-3,self.x+j-3) not in obstacles:
#                                 obstacles.append((self.y+i-3,self.x+j-3))
#                 print(obstacles)
#                 self.obstacles.append(obstacles)
#                 path_forward.append((self.y + self.vel_y,self.x+self.vel_x))
                
#                 if ((self.y + self.vel_y,self.x+self.vel_x) not in obstacles and 
#                     self.x + self.vel_x <29 and self.y + self.vel_y <29 and 
#                     self.x + self.vel_x >0 and self.y + self.vel_y >0 ) :
#                     self.x += self.vel_x
#                     self.y += self.vel_y
#                     time.sleep(0.5)
#                     pygame.draw.rect(screen, RED, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
#                     pygame.display.flip()

#             elif len(neighbor_indices_bottom) > 0:
#                 choice = neighbor_indices_bottom[random.randint(0,len(neighbor_indices_bottom)-1)]
                
#                 self.vel_x = choice[0]
#                 self.vel_y = choice[1]
#                 # print(self.vel_x,self.vel_y)
#                 print(self.x+self.vel_x,self.vel_y+self.y)
#                 obstacles = []
#                 for i in range(len(lidar_scan)):
#                     for j in range(len(lidar_scan[0])):
#                         if lidar_scan[i][j] == 1:
#                             if (self.y+i-3,self.x+j-3) not in obstacles:
#                                 obstacles.append((self.y+i-3,self.x+j-3))
#                 print(obstacles)
#                 self.obstacles.append(obstacles)
#                 path_forward.append((self.y + self.vel_y,self.x+self.vel_x))
                
#                 if ((self.y + self.vel_y,self.x+self.vel_x) not in obstacles and 
#                     self.x + self.vel_x <29 and self.y + self.vel_y <29 and 
#                     self.x + self.vel_x >0 and self.y + self.vel_y >0 ) :
#                     self.x += self.vel_x
#                     self.y += self.vel_y
#                     time.sleep(0.5)
#                     pygame.draw.rect(screen, RED, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
#                     pygame.display.flip()
#             else:
#                 print("Obstacles Everywhere, Backtracking")
#                 backtrack = path_forward[::-1]
#                 for i,j in backtrack:
#                     time.sleep(0.5)
#                     self.x = j 
#                     self.y = i
#                     print(self.x+1,self.y,self.checkpoint)
#                     pygame.draw.rect(screen, GREEN, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
#                     pygame.display.flip()
#                     if (self.x+1 == self.checkpoint[0]) and (self.y == self.checkpoint[1]):
#                         break_flag = 1
  
#         return obstacles

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

pygame.init()

# Init_pos = [27,27]
# vel_x = 1
# vel_y = 1
WIDTH, HEIGHT = 30, 40
CELL_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (0,255, 0)
BLUE = (150, 150, 255)

# screen = pygame.display.set_mode((WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE))
# pygame.display.set_caption("Grid with Obstacles and Robots")

obstacles = [(0, 39), (1, 39), (2, 39), (3, 39), (4, 39), (5, 39), (6, 39), (7, 39), (8, 39), (9, 39), (10, 39), (11, 39), (12, 39),
              (13, 39), (14, 39), (15, 39), (16, 39), (17, 39), (18, 39), (19, 39), (20, 39), (21, 39), (22, 39), (23, 39), (24, 39),
                (0,0), (0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15), (0, 16),
                      (0, 17), (0, 18), (0, 19), (0, 20), (0, 21), (0, 22), (0, 23), (0, 24), (0, 25), (0, 26), (0, 27), (0, 28),
                      (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0), 
                      (15, 0), (16, 0), (17, 0), (18, 0), (19, 0), (20, 0), (21, 0), (22, 0), (23, 0), (24, 0), (25, 0), (26, 0), (27, 0), (28, 0), (29, 0)
                       , (0, 29), (0, 30), (0, 31), (0, 32), (0, 33), (0, 34), (0, 35), (0, 36), (0, 37), (0, 38), (0, 39), (0, 39),
                          (1, 39), (2, 39), (3, 39), (4, 39), (5, 39), (6, 39), (7, 39), (8, 39), (9, 39), (10, 39), (11, 39), (12, 39),
                            (13, 39), (14, 39), (15, 39), (16, 39), (17, 39), (18, 39), (19, 39), (20, 39), (21, 39), (22, 39), 
                            (23, 39), (24, 39), (1, 15), (1, 16), (1, 17), (1, 18), (2, 15), (2, 16), (2, 17), (2, 18), (3, 15), 
                            (3, 16), (3, 17), (3, 18), (4, 15), (4, 16), (4, 17), (4, 18), (5, 15), (5, 16), (5, 17), (5, 18), (6, 15)
                            , (6, 16), (6, 17), (6, 18), (7, 15), (7, 16), (7, 17), (7, 18), (8, 15), (8, 16), (8, 17), (8, 18), 
                            (9, 15), (9, 16), (9, 17), (9, 18), (10, 15), (10, 16), (10, 17), (10, 18), (11, 15), (11, 16), (11, 17),
                              (11, 18), (12, 15), (12, 16), (12, 17), (12, 18), (13, 15), (13, 16), (13, 17), (13, 18), (14, 15)
                              , (14, 16), (14, 17), (14, 18), (15, 15), (15, 16), (15, 17), (15, 18), (16, 15), (16, 16), 
                              (16, 17), (16, 18), (17, 15), (17, 16), (17, 17), (17, 18), (18, 15), (18, 16), (18, 17), (18, 18), 
                              (19, 15), (19, 16), (19, 17), (19, 18), (20, 15), (20, 16), (20, 17), (20, 18), (21, 15), (21, 16), 
                              (21, 17), (21, 18), (1, 23), (1, 24), (1, 25), (1, 26), (2, 23), (2, 24), (2, 25), (2, 26), (3, 23),
                                (3, 24), (3, 25), (3, 26), (4, 23), (4, 24), (4, 25), (4, 26), (5, 23), (5, 24), (5, 25), (5, 26),
                                 (6, 23), (6, 24), (6, 25), (6, 26), (7, 23), (7, 24), (7, 25), (7, 26), (8, 23), (8, 24), (8, 25),
                             (8, 26), (9, 23), (9, 24), (9, 25), (9, 26), (10, 23), (10, 24), (10, 25), (10, 26), (11, 23),
                                 (11, 24), (11, 25), (11, 26), (12, 23), (12, 24), (12, 25), (12, 26), (13, 23), (13, 24), (13, 25), 
                                 (13, 26), (14, 23), (14, 24), (14, 25), (14, 26), (15, 23), (15, 24), (15, 25), (15, 26), (16, 23),
                                   (16, 24), (16, 25), (16, 26), (17, 23), (17, 24), (17, 25), (17, 26), (18, 23), (18, 24),
                                     (18, 25), (18, 26), (19, 23), (19, 24), (19, 25), (19, 26), (20, 23), (20, 24), (20, 25),
                                     (20, 26), (21, 23), (21, 24), (21, 25), (21, 26), (1, 31), (1, 32), (1, 33), (1, 34), 
                                     (2, 31), (2, 32), (2, 33), (2, 34), (3, 31), (3, 32), (3, 33), (3, 34), (4, 31), (4, 32),
                                     (4, 33), (4, 34), (5, 31), (5, 32), (5, 33), (5, 34), (6, 31), (6, 32), (6, 33), 
                                     (6, 34), (7, 31), (7, 32), (7, 33), (7, 34), (8, 31), (8, 32), (8, 33), (8, 34), 
                                     (9, 31), (9, 32), (9, 33), (9, 34), (10, 31), (10, 32), (10, 33), (10, 34), (11, 31),
                                    (11, 32), (11, 33), (11, 34), (12, 31), (12, 32), (12, 33), (12, 34), (13, 31), 
                                      (13, 32), (13, 33), (13, 34), (14, 31), (14, 32), (14, 33), (14, 34), (15, 31),
                                         (15, 32), (15, 33), (15, 34), (16, 31), (16, 32), (16, 33), (16, 34), (17, 31),
                                       (17, 32), (17, 33), (17, 34), (18, 31), (18, 32), (18, 33), (18, 34), (19, 31),
                                         (19, 32), (19, 33), (19, 34), (20, 31), (20, 32), (20, 33), (20, 34), (21, 31),
                                     (21, 32), (21, 33), (21, 34),(29, 0), (29, 1), (29, 2), (29, 3), (29, 4), (29, 5), (29, 6), 
                                     (29, 7), (29, 8), (29, 9), (29, 10), (29, 11), (29, 12), (29, 13), (29, 14), (29, 15), (29, 16),
                                       (29, 17), (29, 18), (29, 19), (29, 20), (29, 21), (29, 22), (29, 23), (29, 24), (29, 25), (29, 26),
                                         (29, 27), (29, 28), (29, 29), (29, 30), (29, 31), (29, 32), (29, 33), (29, 34), (29, 35), (29, 36), 
                                         (29, 37), (29, 38),(5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (10, 10), (11, 10), (12, 10), 
                                         (13, 10), (14, 10), (15, 10), (16, 10), (17, 10), (18, 10), (19, 10), (20, 10), (21, 10), (22, 10), 
                                         (23, 10), (24, 10), (25, 10), (26, 10), (27, 10), (28, 10), (29, 10)]

grid = np.zeros((40,30))

for i in range(30):
    for j in range(40):
        if (i,j) in obstacles:
          grid[j][i] = 1
        else:
          grid[j][i] = 2
x = 27
y = 37

vel_x = 0
vel_y = -1
# print(grid)
def get_cam_scan(array, y, x):
        # Define the dimensions of the subgrid
        copy_arr = array
        left_right = 6
        front_back = 3
        # copy_arr[x][y] = 20
        

        # Calculate the indices for slicing
        start_x = max(0, x - front_back + 1)
        end_x = min(array.shape[0], x + front_back + 1)
        start_y = max(0, y - left_right)
        end_y = min(array.shape[1], y + left_right + 1)
        print(start_x,end_x, start_y,end_y)

        # Extract the subgrid
        subgrid = copy_arr[start_x:end_x, start_y:end_y]


        return subgrid

print(grid[0:5])

cam_scan = get_cam_scan(grid,x,y)
new_pose_x = x + vel_x
new_pose_y = y + vel_y
print(x,y)
print(new_pose_x,new_pose_y)
# source_col = 0
# for i in cam_scan:
#     if 20 in i:
#         source_col= list(i).index(20)
print(cam_scan)        
# pat = detect_pattern(cam_scan,[x,y])
# print(pat)