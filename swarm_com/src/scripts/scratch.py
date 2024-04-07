# # #!usr/bin/env python3

# # import rospy
# # import math
# # from door_detector import door_detector
# # import numpy as np
# # import cv2
# # from std_msgs.msg import Int32MultiArray
# # import pygame
# # import sys

# # arr = Int32MultiArray()
# # arr.data = [1,2]

# # rospy.init_node("Swarm_Com",anonymous = True)
# # motion_pub = rospy.Publisher('Motion_Data',Int32MultiArray,queue_size = 10)

# # while True:
# #     motion_pub.publish(arr)

# import pygame
# import sys
# import math

# # Define constants
# WIDTH, HEIGHT = 30, 30
# CELL_SIZE = 20
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# BLUE = (100, 100, 255)

# # Obstacles locations (as list of tuples)
# obstacles = [(5, 5), (10, 15), (20, 25)]

# # Starting position for the swarm of 5 robots arranged as a plus sign
# start_x, start_y = 15, 15

# # Initialize pygame
# pygame.init()

# # Set up the screen
# screen = pygame.display.set_mode((WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE))
# pygame.display.set_caption("Grid with Obstacles and Robots")

# # Function to calculate distance between two points
# def distance(p1, p2):
#     return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# # Function to check if a cell is within range of the robot
# def within_range(robot_pos, cell_pos, range_limit):
#     return distance(robot_pos, cell_pos) <= range_limit

# # Function to find the nearest empty cell within range
# def find_nearest_empty(robot_pos, obstacles, range_limit):
#     min_dist = float('inf')
#     nearest_empty = None
#     for x in range(WIDTH):
#         for y in range(HEIGHT):
#             if (x, y) not in obstacles and within_range(robot_pos, (x, y), range_limit):
#                 dist = distance(robot_pos, (x, y))
#                 if dist < min_dist:
#                     min_dist = dist
#                     nearest_empty = (x, y)
#     return nearest_empty

# # Main loop
# while True:
#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     # Clear the screen
#     screen.fill(WHITE)

#     # Draw grid lines
#     for x in range(0, WIDTH * CELL_SIZE, CELL_SIZE):
#         pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT * CELL_SIZE))
#     for y in range(0, HEIGHT * CELL_SIZE, CELL_SIZE):
#         pygame.draw.line(screen, BLACK, (0, y), (WIDTH * CELL_SIZE, y))

#     # Draw obstacles
#     for obstacle in obstacles:
#         pygame.draw.rect(screen, BLACK, (obstacle[0] * CELL_SIZE, obstacle[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

#     # Simulate Alidar for the center robot
#     nearest_empty = find_nearest_empty((start_x, start_y), obstacles, 3)
#     if nearest_empty:
#         start_x, start_y = nearest_empty

#     # Draw Lidar scan area
#     for x in range(start_x - 3, start_x + 4):
#         for y in range(start_y - 3, start_y + 4):
#             if (x, y) not in obstacles and (x, y) != (start_x, start_y):
#                 pygame.draw.rect(screen, (100, 100, 255), (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

#     # Draw swarm of robots (1 single cell robot and 4 around it)
#     pygame.draw.rect(screen, RED, (start_x * CELL_SIZE, start_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))  # Single cell robot
#     for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Coordinates for 4 surrounding robots
#         pygame.draw.rect(screen, RED, ((start_x + i) * CELL_SIZE, (start_y + j) * CELL_SIZE, CELL_SIZE, CELL_SIZE))

#     # Update the display
#     pygame.display.flip()
#!usr/bin/env python3

import rospy
import math
from door_detector import door_detector
import numpy as np
import cv2
from std_msgs.msg import Int32MultiArray
import pygame
import time
import sys

pygame.init()

# Init_pos = [27,27]
# vel_x = 1
# vel_y = 1
WIDTH, HEIGHT = 30, 30
CELL_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (0,255, 0)
BLUE = (150, 150, 255)

screen = pygame.display.set_mode((WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE))
pygame.display.set_caption("Grid with Obstacles and Robots")

obstacles = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0), (15, 0), (16, 0), (17, 0), (18, 0), (19, 0), (20, 0), (21, 0), (22, 0), (23, 0), (24, 0), (25, 0), (26, 0), (27, 0), (28, 0), (29, 0),
             (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15), (0, 16), (0, 17), (0, 18), (0, 19), (0, 20), (0, 21), (0, 22), (0, 23), (0, 24), (0, 25), (0, 26), (0, 27), (0, 28), (0, 29),
             (0, 29), (1, 29), (2, 29), (3, 29), (4, 29), (5, 29), (6, 29), (7, 29), (8, 29), (9, 29), (10, 29), (11, 29), (12, 29), (13, 29), (14, 29), (15, 29), (16, 29), (17, 29), (18, 29), (19, 29), (20, 29), (21, 29), (22, 29), (23, 29), (24, 29),
             (4, 4), (4, 5), (4, 6), (4, 7), (5, 4), (5, 5), (5, 6), (5, 7), (6, 4), (6, 5), (6, 6), (6, 7), (7, 4), (7, 5), (7, 6), (7, 7), (8, 4), (8, 5), (8, 6), (8, 7), (9, 4), (9, 5), (9, 6), (9, 7), (10, 4), (10, 5), (10, 6), (10, 7), (11, 4), (11, 5), (11, 6),
             (11, 7), (12, 4), (12, 5), (12, 6), (12, 7), (13, 4), (13, 5), (13, 6), (13, 7), (14, 4), (14, 5), (14, 6), (14, 7), (15, 4), (15, 5), (15, 6), (15, 7), (16, 4), (16, 5), (16, 6), (16, 7), (17, 4), (17, 5), (17, 6), (17, 7), (18, 4), (18, 5), (18, 6), (18, 7)
             ,(19, 4), (19, 5), (19, 6), (19, 7), (20, 4), (20, 5), (20, 6), (20, 7), (21, 4), (21, 5), (21, 6), (21, 7),(4, 12), (4, 13), (4, 14), (4, 15), (5, 12), (5, 13), (5, 14), (5, 15), (6, 12), (6, 13), (6, 14), (6, 15), (7, 12), (7, 13), (7, 14), (7, 15), (8, 12),
             (8, 13), (8, 14), (8, 15), (9, 12), (9, 13), (9, 14), (9, 15), (10, 12), (10, 13), (10, 14), (10, 15), (11, 12), (11, 13), (11, 14), (11, 15), (12, 12), (12, 13), (12, 14), (12, 15), (13, 12), (13, 13), (13, 14), (13, 15), (14, 12), (14, 13), (14, 14), (14, 15),
             (15, 12), (15, 13), (15, 14), (15, 15), (16, 12), (16, 13), (16, 14), (16, 15), (17, 12), (17, 13), (17, 14), (17, 15), (18, 12), (18, 13), (18, 14), (18, 15), (19, 12), (19, 13), (19, 14), (19, 15), (20, 12), (20, 13), (20, 14), (20, 15), (21, 12), (21, 13), (21, 14), (21, 15),
             (4, 20), (4, 21), (4, 22), (4, 23), (5, 20), (5, 21), (5, 22), (5, 23), (6, 20), (6, 21), (6, 22), (6, 23), (7, 20), (7, 21), (7, 22), (7, 23), (8, 20), (8, 21), (8, 22), (8, 23), (9, 20), (9, 21), (9, 22), (9, 23), (10, 20), (10, 21), (10, 22), (10, 23), (11, 20), (11, 21), (11, 22),
             (11, 23), (12, 20), (12, 21), (12, 22), (12, 23), (13, 20), (13, 21), (13, 22), (13, 23), (14, 20), (14, 21), (14, 22), (14, 23), (15, 20), (15, 21), (15, 22), (15, 23), (16, 20), (16, 21), (16, 22), (16, 23), (17, 20), (17, 21), (17, 22), (17, 23), (18, 20), (18, 21), (18, 22), (18, 23), 
             (19, 20), (19, 21), (19, 22), (19, 23), (20, 20), (20, 21), (20, 22), (20, 23), (21, 20), (21, 21), (21, 22), (21, 23)]

grid = np.zeros((30,30))

for i in range(30):
    for j in range(30):
        if (i,j) in obstacles:
            grid[j][j] = 1
        else:
            grid[j][i] = 0
            print(grid)
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