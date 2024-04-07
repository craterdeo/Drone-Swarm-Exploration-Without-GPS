import numpy as np
import matplotlib.pyplot as plt
import math
import time

class door_detector():

    def __init__(self,drone_name):
        self.name = drone_name
        self.range = 12
        self.door_dist = 0

    # def get_cam_scan(self,grid, x, y):
    #     subgrid_size = self.range
    #     half_size = subgrid_size // 2
    #     subgrid = grid[max(0, x - half_size): min(grid.shape[0], x + half_size + 1),
    #                 max(0, y - half_size): min(grid.shape[1], y + half_size + 1)]
    #     if subgrid.shape != (subgrid_size, subgrid_size):
    #         # If the subgrid is not the expected size, pad it with zeros
    #         padded_subgrid = np.zeros((subgrid_size, subgrid_size))
    #         x_offset = half_size - min(half_size, x)
    #         y_offset = half_size - min(half_size, y)
    #         padded_subgrid[x_offset:x_offset + subgrid.shape[0], y_offset:y_offset + subgrid.shape[1]] = subgrid
    #         return padded_subgrid
    #     return subgrid
    def get_cam_scan(self,array, y, x):
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

        # Extract the subgrid
        subgrid = copy_arr[start_x:end_x, start_y:end_y]


        return subgrid
    

    def detect_pattern(self,matrix,point):
        rows, cols = matrix.shape
        left_flag = 0
        right_flag = 0

        for col in range(cols):
            for row in range(rows - 5):
                if (matrix[row, col] == 1 and
                    matrix[row + 1, col] == 2 and
                    matrix[row + 2, col] == 2 and
                    matrix[row + 3, col] == 2 and
                    matrix[row + 4, col] == 2 and
                    matrix[row + 5, col]==1):
                        if col < point[1]:
                            left_flag = True
                        elif col > point(1):
                            right_flag = True
                        self.door_dist = 6#abs(source_col - col)
                        return [True,left_flag,right_flag,col]

        return [False,left_flag,right_flag]


