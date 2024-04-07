import numpy as np
import random

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def sense_obstacles(self, grid):
        obstacles = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= self.x + i < len(grid) and 0 <= self.y + j < len(grid[0]):
                    obstacles.append(grid[self.x + i][self.y + j])
                else:
                    obstacles.append(1)  # Assume obstacle if outside grid
        return obstacles

def slam(robot, grid, num_iterations):
    for _ in range(num_iterations):
        # Simulate movement
        dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        robot.move(dx, dy)

        # Update the map
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= robot.x + i < len(grid) and 0 <= robot.y + j < len(grid[0]):
                    grid[robot.x + i][robot.y + j] = 0

    return grid

# Define grid size
grid_size = 20
grid = np.zeros((grid_size, grid_size), dtype=int)

# Create a robot instance
robot = Robot(10, 10)

# Run SLAM
updated_grid = slam(robot, grid, num_iterations=5)

# Print the updated grid
print("Updated Grid:")
for row in updated_grid:
    print(row)
