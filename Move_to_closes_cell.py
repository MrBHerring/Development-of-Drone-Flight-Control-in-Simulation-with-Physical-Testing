import setup_path
import airsim
import numpy as np
import math


# Connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)

#Makes drone take off
client.takeoffAsync().join()

# Assuming you have a list of solar cells called "solar_cells_list"
solar_cell_names = []
objects = client.simListSceneObjects()
solar_cells_list=[]
for object_name in objects:
    if 'SolarCells' in object_name:
        # Add the name of the solar cell object to the list
        solar_cell_names.append(object_name)

        
# Retrieve the locations of all solar cells
for solar_cell_pose in solar_cell_names:
    solar_cell_pose = client.simGetObjectPose(solar_cell_pose)
    solar_cell_location = solar_cell_pose.position
    x, y, z = solar_cell_location.x_val, solar_cell_location.y_val, solar_cell_location.z_val
    solar_cells_list.append((x, y))
    
closest_solar_cell = None
closest_distance = math.inf

# Get the drone's current position
drone_position = client.getMultirotorState().kinematics_estimated.position
drone_x, drone_y, drone_z = drone_position.x_val, drone_position.y_val, drone_position.z_val

#Calculates closest cell
for solar_cell in solar_cells_list:
    solar_cell_x, solar_cell_y = solar_cell
    distance = math.sqrt((solar_cell_x - drone_x)**2 + (solar_cell_y - drone_y)**2)
    if distance < closest_distance:
        closest_distance = distance
        closest_solar_cell = solar_cell


# Move the drone to the closest solar cell
target_x, target_y = closest_solar_cell
target_z=-8
print(f"Moving to closest solar cell at ({target_x}, {target_y})")
client.moveToPositionAsync(target_x, target_y, target_z, velocity=10).join()



