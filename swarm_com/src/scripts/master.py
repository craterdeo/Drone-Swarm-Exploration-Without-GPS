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

screen = pygame.display.set_mode((WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE))
pygame.display.set_caption("Grid with Obstacles and Robots")

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

cv2.imshow("grid",grid)
cv2.waitKey(0)
class Swarm:
    def __init__(self,init_pos,screen):
        self.init_pos = init_pos
        self.vel_x = 0
        # self.Motion_Data["Moving"] = 0
        self.vel_y = 0
        self.current_pose_x = self.init_pos[0]
        self.current_pose_y = self.init_pos[1]
        self.drone_count = 5
        self.drone_list = ["left","right","master","front","back"]
        self.curr_drone_list = ["left","right","master","front","back"]
        self.Path_Data = []
        self.detatch_data = [0,0,0,0,0]
        self.screen = screen


        self.motion_pub = rospy.Publisher('Motion_Data',Int32MultiArray,queue_size = 1)
        self.det_pub_l = rospy.Publisher('Left_Detatch_Data',Int32MultiArray,queue_size = 10)
        self.det_pub_r = rospy.Publisher('Right_Detatch_Data',Int32MultiArray,queue_size = 10)
        self.det_pub_f = rospy.Publisher('Front_Detatch_Data',Int32MultiArray,queue_size = 10)
        self.det_pub_b = rospy.Publisher('Back_Detatch_Data',Int32MultiArray,queue_size = 10)
        self.Motion_Data = Int32MultiArray()
        self.Motion_Data.data = self.Path_Data
        self.Detatch_Poses = Int32MultiArray()
        self.Detatch_Poses.layout.dim.append(MultiArrayDimension())
        # dim_arr = ["point_x",8,1]
        self.Detatch_Poses.layout.dim[0].label = 'point_x'
        self.Detatch_Poses.layout.dim[0].size = 5
        self.Detatch_Poses.layout.dim[0].stride = 5
        # self.Detatch_Poses.layout.dim = dim_arr

        self.Detatch_Poses.data = self.detatch_data

    def detatch(self,drone_name):
        self.curr_drone_list.remove(drone_name)
        self.drone_count-=1
        if drone_name == "left":
            i=0
            while i < 3:
                print("publishing: ",self.detatch_data)
                self.det_pub_l.publish(self.Detatch_Poses)
                i+=1
        elif drone_name == "right":
            i=0
            while i < 3:
                print("publishing: ",self.detatch_data)
                self.det_pub_r.publish(self.Detatch_Poses)
                i+=1
        elif drone_name == "front":
            i=0
            while i < 3:
                print("publishing: ",self.detatch_data)
                self.det_pub_f.publish(self.Detatch_Poses)
                i+=1
        elif drone_name == "back":
            i=0
            while i < 3:
                print("publishing: ",self.detatch_data)
                self.det_pub_b.publish(self.Detatch_Poses)
                i+=1
        return


    def navigate(self):
        d = door_detector("Master")
        self.current_pose_x = self.init_pos[0]
        self.current_pose_y = self.init_pos[1]
        door_detected = 0
        # cam_scan = d.get_cam_scan(grid,27,27)
        # print(cam_scan)        
        # pat = d.detect_pattern(cam_scan,[self.current_pose_x,self.current_pose_y])
        self.motion_pub.publish(self.Motion_Data)

        while self.drone_count != 1:    
            self.vel_y = 1    
            while door_detected == 0 and self.current_pose_x >0 and self.current_pose_y > 0:
                cam_scan = d.get_cam_scan(grid,self.current_pose_x,self.current_pose_y)
                new_pose_x = self.current_pose_x - self.vel_x
                new_pose_y = self.current_pose_y - self.vel_y
                print(self.current_pose_x,self.current_pose_y)
                print(self.drone_count)
                source_col = 0
                for i in cam_scan:
                    if 20 in i:
                        source_col= list(i).index(20)
                print(cam_scan)        
                pat = d.detect_pattern(cam_scan,[self.current_pose_x,self.current_pose_y])
                print(pat)
                pygame.draw.rect(screen, RED, (new_pose_x * CELL_SIZE, new_pose_y * CELL_SIZE, CELL_SIZE, CELL_SIZE)) 
                if self.drone_count == 5:
                    for i, j in [(-1,0),(0, -1), (1, 0), (0, 1)]:  # Coordinates for 4 surrounding robots
                        pygame.draw.rect(screen, RED, ((S.current_pose_x + i) * CELL_SIZE, (S.current_pose_y + j) * CELL_SIZE, CELL_SIZE, CELL_SIZE)) # Single cell robot
                        pygame.display.flip()
                # pygame.draw.rect(screen, WHITE, (S.current_pose_x * CELL_SIZE, S.current_pose_y * CELL_SIZE, CELL_SIZE, CELL_SIZE),1) 
                if self.drone_count == 4:
                    for i, j in [(0, -1), (1, 0), (0, 1)]:  # Coordinates for 4 surrounding robots
                        pygame.draw.rect(screen, RED, (new_pose_x * CELL_SIZE, new_pose_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))  # Single cell robot
                        pygame.draw.rect(screen, BLUE, ((S.current_pose_x + i) * CELL_SIZE, (S.current_pose_y + j) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                        # pygame.draw.rect(screen, WHITE, ((new_pose_x+ i) * CELL_SIZE, (new_pose_y + j) * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
                        pygame.display.flip()
                        time.sleep(0.5)
                elif self.drone_count == 3:
                        for i, j in [(1, 0), (0, 1)]:  # Coordinates for 4 surrounding robots
                            pygame.draw.rect(screen, RED, (new_pose_x * CELL_SIZE, new_pose_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))  # Single cell robot
                            pygame.draw.rect(screen, RED, ((S.current_pose_x + i) * CELL_SIZE, (S.current_pose_y + j) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                            # pygame.draw.rect(screen, WHITE, ((new_pose_x+ i) * CELL_SIZE, (new_pose_y + j) * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
                            pygame.display.flip()
                            time.sleep(0.5)
                elif self.drone_count == 2:
                        pygame.draw.rect(screen, RED, (new_pose_x * CELL_SIZE, new_pose_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))  # Single cell robot
                        for i, j in [(0, 1)]:  # Coordinates for 4 surrounding robots
                            pygame.draw.rect(screen, BLUE, ((S.current_pose_x + i) * CELL_SIZE, (S.current_pose_y + j) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                            # pygame.draw.rect(screen, WHITE, ((new_pose_x+ i) * CELL_SIZE, (new_pose_y + j) * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)
                            pygame.display.flip()
                            time.sleep(0.5)
                
                

                self.Path_Data.append(self.current_pose_x)
                self.Path_Data.append(self.current_pose_y)
                
                self.current_pose_x = new_pose_x
                self.current_pose_y = new_pose_y
                if pat[0] == True and pat[1] == True:
                    print(self.current_pose_x,self.current_pose_y)
                    print("door_detected")
                    door_detected = 1
                    if self.drone_count == 5:
                        self.vel_y = 0
                        # self.Motion_Data["Moving"] = 0                        
                        self.detatch_data[0] = self.current_pose_x
                        self.detatch_data[1] = self.current_pose_y
                        self.detatch_data[-1] = d.door_dist
                        self.detatch("left")
                        self.vel_y = 1
                        self.vel_y = 1
                        # self.Motion_Data["Moving"] = 1
                    elif self.drone_count == 4:
                        self.vel_y = 0
                        # self.Motion_Data["Moving"] = 0
                        
                        self.detatch_data[0] = self.current_pose_x
                        self.detatch_data[1] = self.current_pose_y
                        self.detatch_data[-1] = d.door_dist
                        self.detatch("back")
                        self.vel_y = 1
                        self.vel_y = 1
                        # self.Motion_Data["Moving"] = 1
                    elif self.drone_count == 3:
                        self.vel_y = 0
                        # self.Motion_Data["Moving"] = 0
                        
                        self.detatch_data[0] = self.current_pose_x
                        self.detatch_data[1] = self.current_pose_y
                        self.detatch_data[-1] = d.door_dist
                        self.detatch("front")
                        self.vel_y = 1
                        self.vel_y = 1
                        # self.Motion_Data["Moving"] = 1
                    elif self.drone_count == 2:
                        self.vel_y = 0
                        # self.Motion_Data["Moving"] = 0
                        
                        self.detatch_data[0] = self.current_pose_x
                        self.detatch_data[1] = self.current_pose_y
                        self.detatch_data[-1] = d.door_dist
                        self.detatch("right")
                        self.vel_y = 1
                        self.vel_y = 1
                        # self.Motion_Data["Moving"] = 1
                    print("Detatched",self.drone_count)
                    door_detected = 0

        if self.drone_count == 1:
            self.detatch_data[2] = self.current_pose_x
            self.detatch_data[3] = self.current_pose_y 

            i=0

            while i < 100:
                self.det_pub_f.publish(self.Detatch_Poses)
                self.det_pub_b.publish(self.Detatch_Poses)
                self.det_pub_r.publish(self.Detatch_Poses)
                self.det_pub_l.publish(self.Detatch_Poses)
                i+=1
                time.sleep(0.25)

        # self.Motion_Data["Moving"] = 0
        
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the grid
    # for x in range(grid.shape[0]):
    #     for y in range(grid.shape[1]):
    #         if grid[y][x] == 1:
    #             pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    #         elif grid[y][x] == 2:
    #             pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    for x in range(0, WIDTH * CELL_SIZE, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT * CELL_SIZE))
    for y in range(0, HEIGHT * CELL_SIZE, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH * CELL_SIZE, y))
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, (obstacle[0] * CELL_SIZE, obstacle[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Update the display
    

    S = Swarm([27,37],screen)      
    rospy.init_node("Swarm_Com",anonymous = True)
    while not rospy.is_shutdown():
        S.navigate()

    # Quit Pygame
    # pygame.quit()