#!usr/bin/env python3

import pygame
import sys
import math
import rospy

# Define constants
WIDTH, HEIGHT = 30, 30
CELL_SIZE = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (0,255, 0)
BLUE = (150, 150, 255)

obstacles = [(11, 0), (11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12),
             (11,19),(11,18),(11,17),(11, 20), (11, 21), (11, 22), (11, 23), (11, 24), (11, 25), (11, 26), (11, 27), (11, 28),(11, 7), (12, 7), (13, 7), 
             (14, 7), (15, 7), (16, 7), (17, 7),(18,7),(23, 7), (24, 7), (25, 7), (26,7), (27, 7), (28, 7),(29,7), (23, 22), (24, 22), (25, 22), (26, 22),
            (27, 22), (28, 22),(29,22),(11, 22), (12, 22), (13, 22), (14, 22), (15, 22), (16, 22), (17, 22),(18,22),(0, 0), (0, 0), (0, 1), (0, 2), (0, 3),
             (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15),(0, 16), (0, 17), (0, 18),
             (0, 19), (0, 20), (0, 21), (0, 22), (0, 23), (0, 24), (0, 25), (0, 26), (0, 27), (0, 28), (0, 29), (0, 29), (1, 0),(1, 29), 
             (2, 0), (2, 29), (3, 0), (3, 29), (4, 0), (4, 29), (5, 0), (5, 29), (6, 0), (6, 29), (7, 0), (7, 29), (8, 0), (8, 29), (9, 0),
             (9, 29),(10, 0), (10, 29), (11, 0), (11, 29), (12, 0), (12, 29), (13, 0), (13, 29), (14, 0), (14, 29), (15, 0), (15, 29),
             (16, 0), (16, 29), (17, 0),(17, 29), (18, 0), (18, 29), (19, 0), (19, 29), (20, 0), (20, 29), (21, 0), (21, 29), (22, 0),
             (22, 29), (23, 0), (23, 29), (24, 0), (24, 29),(25, 0), (25, 29), (26, 0), (26, 29), (27, 0), (27, 29), (28, 0), (28, 29),
             (29, 0), (29, 29)]
# Starting position for the swarm of 5 robots arranged as a plus sign
start_x, start_y = 13, 27

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE))
pygame.display.set_caption("Grid with Obstacles and Robots")

# Function to calculate distance between two points
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Function to check if a cell is within range of the robot
def within_range(robot_pos, cell_pos, range_limit):
    return distance(robot_pos, cell_pos) <= range_limit

# Function to find the nearest empty cell within range
def find_nearest_empty(robot_pos, obstacles, range_limit):
    min_dist = float('inf')
    nearest_empty = None
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (x, y) not in obstacles and within_range(robot_pos, (x, y), range_limit):
                dist = distance(robot_pos, (x, y))
                if dist < min_dist:
                    min_dist = dist
                    nearest_empty = (x, y)
    return nearest_empty

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Draw grid lines
    for x in range(0, WIDTH * CELL_SIZE, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT * CELL_SIZE))
    for y in range(0, HEIGHT * CELL_SIZE, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH * CELL_SIZE, y))

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, (obstacle[1] * CELL_SIZE, obstacle[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Simulate Alidar for the center robot
    nearest_empty = find_nearest_empty((start_x, start_y), obstacles, 3)
    if nearest_empty:
        start_x, start_y = nearest_empty

    # Draw Lidar scan area
    for x in range(start_x - 3, start_x + 4):
        for y in range(start_y - 3, start_y + 4):
            if (x, y) not in obstacles and (x, y) != (start_x, start_y):
                pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw swarm of robots (1 single cell robot and 4 around it)
    pygame.draw.rect(screen, RED, (start_x * CELL_SIZE, start_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))  # Single cell robot
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Coordinates for 4 surrounding robots
        pygame.draw.rect(screen, RED, ((start_x + i) * CELL_SIZE, (start_y + j) * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Update the display
    pygame.display.flip()



