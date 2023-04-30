import setup_path
import airsim
import numpy as np
import math
import keyboard
import KeyboardControl as kc
import time
import sys

currentDrone = "Drone4"
currentPoint = "SolarPoint5"

client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True, currentDrone)

client.takeoffAsync(currentDrone).join()
#client.hoverAsync("Drone1").join()
# client.hoverAsync("Drone2").join()

print(currentDrone, currentPoint)
# print("Before the code crashes")
#
# print("This is working")
# time.sleep(5)


# set target altitude to -5 meters


target_altitude = -5

# move drone to target altitude
client.moveToZAsync(target_altitude, velocity=1, vehicle_name=currentDrone).join()

# # set the drone's velocity in the x direction (forward)
# vx = 4
#
# # set the duration of the movement in seconds
# duration = 20
#
# # move the drone in the forward direction for the specified duration
# client.moveByVelocityAsync(vx, 0, 0, duration).join()


# Get the pose of Solar Point6
solar_point_name = currentPoint
solar_point_pose = client.simGetObjectPose(solar_point_name)
if solar_point_pose.position != (None, None, None):
    # Get the position of Solar Point6
    solar_point_position = solar_point_pose.position
    # Subtract 2 from the z value of Solar Point6
    solar_point_position.x_val += 4
    solar_point_position.z_val -= 10
else:
    print(f"{solar_point_name} does not have a valid position")

# Move the drone to the position of Solar Point6
print(f"Moving to {currentPoint} at ({solar_point_position.x_val}, {solar_point_position.y_val}, {solar_point_position.z_val})")
client.moveToPositionAsync(solar_point_position.x_val + 1, solar_point_position.y_val, solar_point_position.z_val,
                           velocity=5, vehicle_name=currentDrone).join()

time.sleep(5)







