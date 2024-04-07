import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
from collections import defaultdict


door_img = cv2.imread('image_data\Left_Drone\left_image_399.jpg')     # door in centre
# door_img = cv2.imread('image_data\Left_Drone\left_image_363.jpg')   # door + boxes
# door_img = cv2.imread('image_data\Left_Drone\left_image_270.jpg')   # side boxes
# door_img = cv2.imread('image_data\Left_Drone\left_image_130.jpg')   # entry 0
# door_img = cv2.imread('image_data\Left_Drone\left_image_141.jpg')   # entry 1



gray = cv2.cvtColor(door_img,cv2.COLOR_BGR2GRAY)
size = door_img.shape
k = size[0]//2

print(size)
t_lower = 50  # Lower Threshold 
t_upper = 150  # Upper threshold 
# kernel = np.ones((5, 5), np.uint8) 
  
# Applying the Canny Edge filter 
edge = cv2.Canny(gray, t_lower, t_upper) 
# img_erosion = cv2.erode(edge, kernel, iterations=1) 
# img_dilation = cv2.dilate(edge, kernel, iterations=1) 
# dilate_2 = cv2.dilate(img_dilation, kernel, iterations=1) 
# print(edge)

def is_door(img):
    img_size = img.shape
    tp = img_size[0]//2

    top_half = img[::tp]
    centre_x = img_size[1]//2

    top_left =[]
    top_right = []
    # print(img)
    for i in range(tp):
        for j in range(centre_x):
            if img[i][j] == 255:
                # edge[i][j] = 0
                top_left.append([i,j])

    for i in range(tp):           
        for j in range(centre_x,2*centre_x):
            if img[i][j] == 255:
                # edge[i][j] = 0
                top_right.append([i,j])
        
    # print(top_left)
    # print(top_right)

is_door(edge)

pts = []
lat=[]
lon=[]
for i in range(20,k):
    for j in range(size[1]//4,size[1]):
        if edge[i][j] == 255:
            # edge[i][j] = 0
            pts.append([i,j])
            lat.append(i)
            lon.append(j)
 
# print(set(lat))
# print(set(lon))
# print(pts)


def is_centre(lats,lons):
    avg_x = sum(lats)/len(lats)
    avg_y = sum(lons)/len(lons)

    print(avg_x,avg_y)

    if avg_y < 135 and avg_y > 125 :
        return True
    else:
        return False
    
def is_door_cluster(arr):
    
    lat_to_lon = defaultdict(int)

    for x,y in arr:
        lat_to_lon[x] += 1

    result_dict = dict(lat_to_lon)
    quadrat_y= []
    for i in pts:
        if result_dict[i[0]] == 4:
            quadrat_y.append(i[1])
    set_y = list(set(quadrat_y))
    print(set_y)
    print(np.mean(set_y))
    
    # print(result_dict)
    lst = list(result_dict.values())
    print(lst.count(4))
    if lst.count(4) > 28 and np.mean(set_y) < 148 and np.mean(set_y)> 125 :
        return True
    else:
        return False
            
print("Is Door ?:",is_door_cluster(pts))

print("Door is Centred ?",is_centre(lat,lon))
  
cv2.imshow('original', gray) 
cv2.imshow('edge', edge) 
# cv2.imshow('Erosion', img_erosion) 
# cv2.imshow('Dilation', img_dilation) 
# cv2.imshow('Dilation2', dilate_2) 
cv2.waitKey(0) 