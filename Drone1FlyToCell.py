import setup_path
import airsim
import numpy as np
import math
import time

# Connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True, "Drone1")

f1 = client.takeoffAsync(vehicle_name="Drone1")
f1.join()

# Retrieve the pose of SolarCell6
solar_cell_name = "SolarCells6"
solar_cell_pose = client.simGetObjectPose(solar_cell_name)
if solar_cell_pose.position != (None, None, None):
    # Do something with solar cell pose
    pass
else:
    print(f"{solar_cell_name} does not have a valid position")

solar_cell_pose = client.simGetObjectPose(solar_cell_name)
solar_cell_location = solar_cell_pose.position
# Calculate center coordinates of the solar cell
cell_width = 0.2 # width of the solar cell
cell_center_x = solar_cell_location.x_val - 2
cell_center_y = solar_cell_location.y_val - 2 
cell_center_z = (solar_cell_location.z_val - cell_width / 2) - 4
# Move the drone to Solar Cell 6
print(f"Moving to Solar Cell 6 at ({cell_center_x}, {cell_center_y}, {cell_center_z})")
client.moveToPositionAsync(cell_center_x, cell_center_y, cell_center_z - 1, velocity=2, vehicle_name ="Drone1").join()

# Hover over the cell
print("Reached Solar Cell 6. Hovering.")

# Disarm the drone
client.armDisarm(False)
