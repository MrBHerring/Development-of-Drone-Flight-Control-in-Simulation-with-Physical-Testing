import setup_path
import airsim
import numpy as np
import math
import keyboard
import KeyboardControl as kc
import time


# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.enableApiControl(True)
client.simEnableWeather(True)
client.confirmConnection()
print("You have picked up the solar cell!!!\n")
print("to drop solar cell press 'esc' key")

# Create an empty list to store the names of the solar cell objects
solar_cell_names = []
objects = client.simListSceneObjects()


# Loop through the objects and find any solar cell objects
for object_name in objects:
    if 'SolarCells' in object_name:
        # Add the name of the solar cell object to the list
        solar_cell_names.append(object_name)


# get the pose of an object named
#This case is specifcally for first solar cell
First_solar = solar_cell_names[0]
solar_cell_name = str(solar_cell_names[0])
print(solar_cell_name)
solar_cell_pose = client.simGetObjectPose(solar_cell_name)
solar_cell_position = solar_cell_pose.position

# save the x,y, and z of the solar cells
#specifcally for first solar cell
solar_cell_x=  solar_cell_position.x_val
solar_cell_y=  solar_cell_position.y_val
solar_cell_z=  solar_cell_position.z_val


#change orentiaon
pitch = 0
roll = 40
yaw = 0


# Convert the Euler angles to a quaternion
quat = airsim.to_quaternion(math.radians(pitch), math.radians(roll), math.radians(yaw))


"""
# Set the new orientation of the object
client.simSetObjectPose(solar_cell_name, airsim.Pose(airsim.Vector3r(0, 0, 0), quat))
"""

while True:
    drone_position = client.getMultirotorState().kinematics_estimated.position
    drone_x = drone_position.x_val
    drone_y = drone_position.y_val
    drone_z = drone_position.z_val + 3
    client.simSetObjectPose(solar_cell_name,airsim.Pose(airsim.Vector3r(drone_x, drone_y, drone_z), quat))
    if keyboard.is_pressed('esc'):
        client.simSetObjectPose(solar_cell_name,airsim.Pose(airsim.Vector3r(drone_x, drone_y, -2), quat))
        break
    #time.sleep(1)  # add a delay to avoid flooding the console with messages












"""


# get current pose of solar cell
current_pose = client.simGetObjectPose(solar_cell_name)
current_orientation = current_pose.orientation
new_orientation = airsim.to_quaternion(current_orientation.x_val, current_orientation.y_val, current_orientation.z_val)
# Print the position of SolarCells6
#print("The position of", solar_cell_name, "is", solar_cell_position)



# Set the new position of SolarCells6
pose= airsim.Vector3r(3,2,1)


#print(solar_cell_x,"\n",solar_cell_y,"\n",solar_cell_z)

client.simSetObjectPose(solar_cell_name, pose, teleport= False)
print(solar_cell_position)

# Print the new position of SolarCells6
solar_cell_pose = client.simGetObjectPose('SolarCells6')
solar_cell_position = solar_cell_pose.position
print("The new position of SolarCells6 is", solar_cell_position) """
