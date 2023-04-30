import setup_path
import airsim
import numpy as np
import math
import keyboard
import KeyboardControl as kc
import time
import subprocess
import threading
import sys

# connect to the AirSim simulator
client = airsim.MultirotorClient()
#client.enableApiControl(True, "Drone1")
client.enableApiControl(True, "Drone5")
#Makes drone take off

client.confirmConnection()
##print("You have picked up the solar cell!!!\n")
##print("to drop solar cell press 'q' key")

#client.takeoffAsync(vehicle_name="Drone1").join()
client.simEnableWeather(True)
#time.sleep(30)
client.takeoffAsync(vehicle_name="Drone5")



# Set the thread flag to indicate whether the drone altitude thread is running or not
drone_altitude_thread_running = False
x = "Processing"
# Define a function to run the drone altitude subprocess in a separate thread
def run_drone_altitude_thread(drone_name, target_point_name):
    global drone_altitude_thread_running
    drone_altitude_thread_running = True
    subprocess.call(["python", "C:\\Users\\frost\\Desktop\\airsim_api\\AirSim\\PythonClient\\multirotor\\Drone5CarryFly.py", drone_name, target_point_name])
    drone_altitude_thread_running = False
    global x
    x = "Done"

# Define a function to move the solar cell
def move_solar_cell(solar_cell_name, solar_cell_pose, solar_cell_position, current_drone, current_point):
    pitch = 0
    roll = 0
    yaw = 0
    print("Here is the current drone: " + current_drone)

    # Convert the Euler angles to a quaternion
    quat = airsim.to_quaternion(math.radians(pitch), math.radians(roll), math.radians(yaw))

    # get the initial orientation of the solar cell
    init_quat = solar_cell_pose.orientation

    while True:
        ##        client.armDisarm(False)
        drone_position = client.getMultirotorState(vehicle_name="Drone5").kinematics_estimated.position
        drone_x = drone_position.x_val + 3
        drone_y = drone_position.y_val - 2
        drone_z = drone_position.z_val + 5




        # Start the drone altitude thread if it's not already running
        if not drone_altitude_thread_running:
            drone_name = current_drone
            target_point_name = current_point
            drone_altitude_thread = threading.Thread(target=run_drone_altitude_thread, args=(drone_name, target_point_name))
            drone_altitude_thread.start()


        # Adjust the z coordinate based on the calculated drop height
        drop_height = solar_cell_position.z_val - 2.0
        if drone_z > drop_height:
            drone_z = drop_height

        # set the solar cell pose with the initial orientation
        client.simSetObjectPose(solar_cell_name, airsim.Pose(airsim.Vector3r(drone_x, drone_y, drone_z), init_quat))

        if x == "Done":
            # get the drone's current orientation
            drone_orient = client.simGetVehiclePose().orientation

            # Drop the solar cell with the current orientation
            client.simSetObjectPose(solar_cell_name, airsim.Pose(airsim.Vector3r(drone_x, drone_y, drone_z), drone_orient))
            time.sleep(0.1)
            drone_z = solar_cell_position.z_val
            client.simSetObjectPose(solar_cell_name, airsim.Pose(airsim.Vector3r(drone_x, drone_y, drone_z), drone_orient))
            break

time.sleep(2)
current_solar = "SolarCells3"
current_drone = "Drone5"
current_point = "SolarPoint3"
print(current_solar)
solar_cell_name = str(current_solar)
solar_cell_pose = client.simGetObjectPose(solar_cell_name)
solar_cell_position = solar_cell_pose.position
move_solar_cell(solar_cell_name, solar_cell_pose, solar_cell_position, current_drone, current_point)


client.landAsync(vehicle_name=current_drone).join()
client.armDisarm(False)
client.enableApiControl(False, current_drone)
