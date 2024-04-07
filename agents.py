import airsim
import cv2
import numpy as np
import os
import pprint
# import setup_path 
import tempfile
from airsim.types import YawMode
import pandas as pd
from datetime import datetime
import os
import matplotlib.pyplot as plt
# import tensorflow
# from keras.models import load_model
from keras_preprocessing import image
from Swarm_IP import Door_Detector
import time
#connect to Airsim

client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True, "Front_Drone")
client.enableApiControl(True, "Left_Drone")
client.enableApiControl(True, "Master_Drone")
client.enableApiControl(True, "Right_Drone")
client.enableApiControl(True, "Back_Drone")

client.armDisarm(True, "Front_Drone")
client.armDisarm(True, "Left_Drone")
client.armDisarm(True, "Master_Drone")
client.armDisarm(True, "Right_Drone")
client.armDisarm(True, "Back_Drone")

airsim.wait_key('Press any key to takeoff')

f1 = client.takeoffAsync(vehicle_name="Front_Drone")
f2 = client.takeoffAsync(vehicle_name="Left_Drone")
f3 = client.takeoffAsync(vehicle_name="Master_Drone")
f4 = client.takeoffAsync(vehicle_name="Right_Drone")
f5 = client.takeoffAsync(vehicle_name="Back_Drone")
f1.join()
f2.join()
f3.join()
f4.join()
f5.join()

# f11 = client.moveByVelocityAsync(0.0,0.0,2.0,2.0,0, YawMode(is_rate=False, yaw_or_rate = 0.0),"Front_Drone")
# f12 = client.moveByVelocityAsync(0.0,0.0,2.0,2.0,0, YawMode(is_rate=False, yaw_or_rate = -90),"Left_Drone")
# f13 = client.moveByVelocityAsync(0.0,0.0,2.0,2.0,0, YawMode(is_rate=False, yaw_or_rate = 0.0),"Master_Drone")
# f14 = client.moveByVelocityAsync(0.0,0.0,2.0,2.0,0, YawMode(is_rate=False, yaw_or_rate = 90),"Right_Drone")
# f15 = client.moveByVelocityAsync(0.0,0.0,2.0,2.0,0, YawMode(is_rate=False, yaw_or_rate = 0.0),"Back_Drone")
# f11.join()
# f12.join()
# f13.join()
# f14.join()
# f15.join()

path_data = []
lidar_pose_data = []
timestamps = []
segments=[]
images = []
imu_str=[]
# model_door = load_model('Door_Detection\door_model.h5')
k=0
stop_flag = 0
door_flag = 0
for i in range(40):
      
      duration = 1
      if stop_flag == 1:
            duration = 0
      yaw_rate = -0.01
      k+=1
      if k%10 == 0:
            yaw_rate = 0.01
      f1 = client.moveByVelocityAsync(2.0,0.0,yaw_rate,duration,0, YawMode(is_rate=False, yaw_or_rate = 0.0),"Front_Drone")
      f2 = client.moveByVelocityAsync(2.0,0.0,yaw_rate,duration,0, YawMode(is_rate=False, yaw_or_rate = -90),"Left_Drone")
      f3 = client.moveByVelocityAsync(2.0,0.0,yaw_rate,duration,0, YawMode(is_rate=False, yaw_or_rate = 0.0),"Master_Drone")
      f4 = client.moveByVelocityAsync(2.0,0.0,yaw_rate,duration,0, YawMode(is_rate=False, yaw_or_rate = 90),"Right_Drone")
      f5 = client.moveByVelocityAsync(2.0,0.0,yaw_rate,duration,0, YawMode(is_rate=False, yaw_or_rate = 0.0),"Back_Drone")
      f1.join()
      f2.join()
      f3.join()
      f4.join()
      f5.join()
      # print("calling")
      temp_time = 0
      while door_flag == 1:
            time.sleep(2)
            f2 =client.moveByVelocityAsync(0.0,-2.0,yaw_rate-0.04,temp_time,0, YawMode(is_rate=False, yaw_or_rate = -90),"Left_Drone")
            f4 =client.moveByVelocityAsync(0.0,2.0,yaw_rate-0.04,temp_time,0, YawMode(is_rate=False, yaw_or_rate = 90),"Right_Drone")
            temp_time +=1 
  
      imu_data = client.getImuData(imu_name = "Imu_f", vehicle_name = "Front_Drone")
      imu_str.append(imu_data)
      #################################################################
      lidar_data = client.getLidarData("Lidar2","Left_Drone")
      # lidar_segment_set = set(lidar_data.segmentation)
      # segments.append(lidar_data.segmentation)
      path_data.append(lidar_data.point_cloud)
      lidar_pose_data.append(lidar_data.pose)
      timestamps.append(datetime.now().strftime("%H:%M:%S"))
      #################################################################
      if i%2 == 0:
            img = client.simGetImage("0",airsim.ImageType.Scene,vehicle_name="Left_Drone")
            img1d = airsim.string_to_uint8_array(img)       #np.fromstring(img.image_data_uint8, dtype=np.uint8) 
            rawImage = client.simGetImage(0,airsim.ImageType.Scene,vehicle_name="Left_Drone")    
            png = cv2.imdecode(airsim.string_to_uint8_array(rawImage), cv2.IMREAD_UNCHANGED)
            png = png[:,:,:3]
            ################################################################
            # png = cv2.resize(png,(224,224))
            # x = image.img_to_array(png)
            # x = np.expand_dims(x, axis=0) / 255
      
            detector = Door_Detector(50,150,png,"Left_Drone")
            # if k%10 == 0:
            #     cv2.imshow("image",png)
            #     cv2.waitKey(0)
            if detector.check_door():
                  print("Door_Detected")
                  stop_flag = 1
                  door_flag = 1
            else:
                  print("Door Not Detected")
            
      
      

  
            # fm1 = client.moveByVelocityAsync(0.0,0.0,0.0,1.0,0, YawMode(is_rate=False, yaw_or_rate = 0.0),"Front_Drone")
            # fm2 = client.moveByVelocityAsync(0.0,0.0,0.0,1.0,0, YawMode(is_rate=False, yaw_or_rate = -90),"Left_Drone")
            # fm3 = client.moveByVelocityAsync(0.0,0.0,0.0,1.0,0, YawMode(is_rate=False, yaw_or_rate = 0.0),"Master_Drone")
            # fm4 = client.moveByVelocityAsync(0.0,0.0,0.0,1.0,0, YawMode(is_rate=False, yaw_or_rate = 90),"Right_Drone")
            # fm5 = client.moveByVelocityAsync(0.0,0.0,0.0,1.0,0, YawMode(is_rate=False, yaw_or_rate = 0.0),"Back_Drone")
            # fm1.join()
            # fm2.join()
            # fm3.join()
            # fm4.join()
            # fm5 .join()

            # fl1 = client.moveByVelocityAsync(0.0,2.0,0.0,0.0,0, YawMode(is_rate=False, yaw_or_rate = -90),"Left_Drone")
            # fl1.join()

    
    # classes = model_door(x,training=False)
    # print(np.argmax(classes[0]),classes[0])
    
    # if np.argmax(classes[0]) == 1:
    #     print("door_detected")
    #     cv2.imshow("image",png)
    #     cv2.waitKey(0)
    #     break
    
    # print(len(img1d)) 
    # png_image = client.simGetImage("0", airsim.ImageType.Scene)
    # responses = client.simGetImages([airsim.ImageRequest("front_right", airsim.ImageType.Scene, False, False)])
    # images.append(responses)
    # print(lidar_data)

# print(segments[0])
# i=0
# for response in images[0]:
#     img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8)
#     name = "img" + str(i) + ".png"
#     # img = cv2.imdecode(np.frombuffer(img1d, dtype=np.uint8), 3)
#     cv2.imwrite(name,img1d)
#     i+=1

# print(len(path_data))
# lidar_data = client.getLidarData("Lidar1","Master_Drone")
# lidar_segment_set = set(lidar_data.segmentation)
# segments.append(lidar_data.segmentation)
# path_data.append(lidar_data.point_cloud)
print(timestamps)
print(len(timestamps))
df = pd.DataFrame(path_data,timestamps)
df1 = pd.DataFrame(lidar_pose_data)
df = df.transpose()
df1 = df1.transpose()

lidar_csv = df.to_csv("IMU_Data\Left_Lidar_with_tv.csv",index=False)
lidar_pose_csv = df1.to_csv("IMU_Data\Left_Lidar_with_pose.csv",index=False)
print(df.head())

# lidar_data = client.getLidarData("Lidar1","Master_Drone")
# lidar_segment_set = set(lidar_data.segmentation)
# print(lidar_data)
# print("________")
# print(lidar_segment_set)
# print("_________")
# point_cloud = np.array(lidar_data.point_cloud)
# print(point_cloud.shape)