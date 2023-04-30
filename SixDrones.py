import airsim
import cv2
import numpy as np
import os
import pprint
import setup_path 
import tempfile
import solarDetect as solar
import time
import math
import subprocess
# Use below in settings.json with Blocks environment
"""
{
	"SeeDocsAt": "https://github.com/Microsoft/AirSim/blob/main/docs/settings.md",
	"SettingsVersion": 1.2,
	"SimMode": "Multirotor",
	"ClockSpeed": 1,
	
	"Vehicles": {
		"Drone1": {
		  "VehicleType": "SimpleFlight",
		  "X": 4, "Y": 0, "Z": -2
		},
		"Drone2": {
		  "VehicleType": "SimpleFlight",
		  "X": 8, "Y": 0, "Z": -2
		}

    }
}
"""



# def closestCell():
#     # Assuming you have a list of solar cells called "solar_cells_list"
#     solar_cell_names = []
#     objects = client.simListSceneObjects()
#     solar_cells_list = []
#     for object_name in objects:
#         if 'SolarCells' in object_name:
#             # Add the name of the solar cell object to the list
#             solar_cell_names.append(object_name)
#
#     # Retrieve the locations of all solar cells
#     for solar_cell_pose in solar_cell_names:
#         solar_cell_pose = client.simGetObjectPose(solar_cell_pose)
#         solar_cell_location = solar_cell_pose.position
#         x, y, z = solar_cell_location.x_val, solar_cell_location.y_val, solar_cell_location.z_val
#         solar_cells_list.append((x, y))
#
#     closest_solar_cell = None
#     closest_distance = math.inf
#
#     # Get the drone's current position
#     drone_position = client.getMultirotorState().kinematics_estimated.position
#     drone_x, drone_y, drone_z = drone_position.x_val, drone_position.y_val, drone_position.z_val
#
#     # Calculates closest cell
#     for solar_cell in solar_cells_list:
#         solar_cell_x, solar_cell_y = solar_cell
#         distance = math.sqrt((solar_cell_x - drone_x) ** 2 + (solar_cell_y - drone_y) ** 2)
#         if distance < closest_distance:
#             closest_distance = distance
#             closest_solar_cell = solar_cell
#
#     # Move the drone to the closest solar cell
#     target_x, target_y = closest_solar_cell
#     target_z = -6
#     print(f"Moving to closest solar cell at ({target_x}, {target_y})")
#     client.moveToPositionAsync(target_x, target_y, target_z, velocity=10, vehicle_name = "Drone1").join()


# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True, "Drone1")
client.enableApiControl(True, "Drone2")
client.enableApiControl(True, "Drone3")
client.enableApiControl(True, "Drone4")
client.enableApiControl(True, "Drone5")
client.enableApiControl(True, "Drone6")
client.armDisarm(True, "Drone1")
client.armDisarm(True, "Drone2")
client.armDisarm(True, "Drone3")
client.armDisarm(True, "Drone4")
client.armDisarm(True, "Drone5")
client.armDisarm(True, "Drone6")

#airsim.wait_key('Press any key to takeoff')
f1 = client.takeoffAsync(vehicle_name="Drone1")
f2 = client.takeoffAsync(vehicle_name="Drone2")
f3 = client.takeoffAsync(vehicle_name="Drone3")
f4 = client.takeoffAsync(vehicle_name="Drone4")
f5 = client.takeoffAsync(vehicle_name="Drone5")
f6 = client.takeoffAsync(vehicle_name="Drone6")
f1.join()
f2.join()
f3.join()
f4.join()
f5.join()
f6.join()

z = -1
count = 110
duration = 9
speed = 4
# straight
vx = -speed
vy = 0

print("moving by velocity vx=" + str(vx) + ", vy=" + str(vy) + ", yaw=180")
f1 = client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 180), vehicle_name="Drone1")

f2 = client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 180), vehicle_name="Drone2")

f3 = client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 180), vehicle_name="Drone3")

f4 = client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 180), vehicle_name="Drone4")

f5 = client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 180), vehicle_name="Drone5")

f6 = client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 180), vehicle_name="Drone6")
# solar.imageCapture(count)

f1.join()
f2.join()
f3.join()
f4.join()
f5.join()
f6.join()



print("moving by velocity vx=" + str(vx) + ", vy=" + str(vy) + ", yaw=90")
f1 = client.moveByVelocityZAsync(0, 4, z, 10, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 90), vehicle_name="Drone1")


f2 = client.moveByVelocityZAsync(0, 4, z, 10, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 90), vehicle_name="Drone2")

f3 = client.moveByVelocityZAsync(0, 4, z, 10, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 90), vehicle_name="Drone3")

f4 = client.moveByVelocityZAsync(0, 4, z, 10, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 90), vehicle_name="Drone4")

f5 = client.moveByVelocityZAsync(0, 4, z, 10, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 90), vehicle_name="Drone5")

f6 = client.moveByVelocityZAsync(0, 4, z, 10, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 90), vehicle_name="Drone6")
#solar.imageCapture(count)

f1.join()
f2.join()
f3.join()
f4.join()
f5.join()
f6.join()



print("moving by velocity vx=" + str(vx) + ", vy=" + str(vy) + ", yaw=180")
f1 = client.moveByVelocityZAsync(-4, 0, z, 9, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 180), vehicle_name="Drone1")


f2 = client.moveByVelocityZAsync(-4, 0, z, 9, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 180), vehicle_name="Drone2")

f3 = client.moveByVelocityZAsync(-4, 0, z, 9, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 180), vehicle_name="Drone3")

f4 = client.moveByVelocityZAsync(-4, 0, z, 9, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 180), vehicle_name="Drone4")

f5 = client.moveByVelocityZAsync(-4, 0, z, 9, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 180), vehicle_name="Drone5")

f6 = client.moveByVelocityZAsync(-4, 0, z, 9, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 180), vehicle_name="Drone6")
#solar.imageCapture(count)

f1.join()
f2.join()
f3.join()
f4.join()
f5.join()
f6.join()


print("moving by velocity vx=" + str(vx) + ", vy=" + str(vy) + ", yaw=90")
f1 = client.moveByVelocityZAsync(0, 4, z, 12, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 90), vehicle_name="Drone1")


f2 = client.moveByVelocityZAsync(0, 4, z, 12, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 90), vehicle_name="Drone2")

f3 = client.moveByVelocityZAsync(0, 4, z, 12, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 90), vehicle_name="Drone3")

f4 = client.moveByVelocityZAsync(0, 4, z, 12, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 90), vehicle_name="Drone4")

f5 = client.moveByVelocityZAsync(0, 4, z, 12, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 90), vehicle_name="Drone5")

f6 = client.moveByVelocityZAsync(0, 4, z, 12, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 90), vehicle_name="Drone6")
count = 50
#solar.imageCapture(count)


f1.join()
f2.join()
f3.join()
f4.join()
f5.join()
f6.join()
time.sleep(5)
#subprocess.call(["python", "C:\\Users\\frost\\Desktop\\airsim_api\\AirSim\\PythonClient\\multirotor\\DroneOne2Six.py"])

#closestCell()


# solar.imageCapture(count)
# # time.sleep(1)
# print("moving by velocity vx=" + str(vx) + ", vy=" + str(vy) + ", yaw=90")
# client.moveByVelocityZAsync(0, 4, z, 10, airsim.DrivetrainType.MaxDegreeOfFreedom,
#                             airsim.YawMode(False, 90), vehicle_name="Drone1")
# solar.imageCapture(count)
# # time.sleep(1)
# print("moving by velocity vx=" + str(vx) + ", vy=" + str(vy) + ", yaw=180")
# client.moveByVelocityZAsync(-4, 0, z, 9, airsim.DrivetrainType.MaxDegreeOfFreedom,
#                             airsim.YawMode(False, 180), vehicle_name="Drone1")
# #solar.imageCapture(count)
# # time.sleep(1)
# print("moving by velocity vx=" + str(vx) + ", vy=" + str(vy) + ", yaw=90")
# client.moveByVelocityZAsync(0, 4, z, 12, airsim.DrivetrainType.MaxDegreeOfFreedom,
#                             airsim.YawMode(False, 90), vehicle_name="Drone1")
# count = 180
# #solar.imageCapture(count)
# time.sleep(1)


# vehicle_name="Drone1"
# f1 = prefly(vehicle_name)
# vehicle_name="Drone2"
# f2 = prefly(vehicle_name)
# vehicle_name="Drone3"
# f3 = prefly(vehicle_name)
# vehicle_name="Drone4"
# f4 = prefly(vehicle_name)
# vehicle_name="Drone5"
# f5 = prefly(vehicle_name)
# vehicle_name="Drone6"
# f6 = prefly(vehicle_name)
# f1.join()
# f2.join()
# f3.join()
# f4.join()
# f5.join()
# f6.join()
