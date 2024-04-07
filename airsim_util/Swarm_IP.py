import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
from collections import defaultdict

class Door_Detector():

    def __init__(self,thresh_low,thresh_high,image,vehicle_name):

        self.tl = thresh_low
        self.th = thresh_high
        self.image = image
        self.image_size = image.shape
        self.vehicle_name = vehicle_name

        self.top_half = image.shape
        self.gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        self.edge = cv2.Canny(image, thresh_low, thresh_high) 
        
        

        def get_point_clusters():
            pts = []
            lat=[]
            lon=[]
            for i in range(20,self.image_size[0]//2):
                for j in range(self.image_size[1]):
                    if self.edge[i][j] == 255:
                        pts.append([i,j])
                        lat.append(i)
                        lon.append(j)
            
            return [pts,lat,lon]
        
        self.pts,self.lats,self.lons = get_point_clusters()

        def split_image():
            img_size = self.image.shape
            tp = img_size[0]//2
            top_half = self.image[::tp]
            centre_x = img_size[1]//2
            top_left =[]
            top_right = []
            for i in range(tp):
                for j in range(centre_x):
                    if self.image[i][j] == 255:
                        top_left.append([i,j])
            for i in range(tp):           
                for j in range(centre_x,2*centre_x):
                    if self.image[i][j] == 255:
                        top_right.append([i,j])
            
            return [top_left,top_right]
        
    def check_door(self):
        lat_to_lon = defaultdict(int)
        for x,y in self.pts:
            lat_to_lon[x] += 1
        result_dict = dict(lat_to_lon)
        lst = list(result_dict.values())

        quadrat_y= []
        for i in self.pts:
            if result_dict[i[0]] == 4:
                quadrat_y.append(i[1])
        set_y = list(set(quadrat_y))
        print(lst.count(4))
        print(np.mean(set_y))
        if lst.count(4) > 28 and np.mean(set_y) < 150 and np.mean(set_y)> 125:
            return True
        else:
            return False




    

