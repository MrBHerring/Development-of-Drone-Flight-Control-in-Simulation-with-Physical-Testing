import setup_path
import airsim
import numpy as np
import math
import keyboard
import KeyboardControl as kc
import time
import subprocess
import threading


# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.enableApiControl(True)
#Makes drone take off
#client.takeoffAsync().join()
client.simEnableWeather(True)
client.confirmConnection()
print("You have picked up the solar cell!!!\n")
print("to drop solar cell press 'q' key")

def update_current_solar_cell_index():
    # Create an empty list to store the names of the solar cell objects
    solar_cell_names = []
    objects = client.simListSceneObjects()

    # Loop through the objects and find any solar cell objects
    for object_name in objects:
        if 'SolarCells' in object_name:
            # Add the name of the solar cell object to the list
            solar_cell_names.append(object_name)

    # Calculate the Euclidean distance between the drone and each solar cell object
    drone_position = client.getMultirotorState().kinematics_estimated.position
    distances = []
    for name in solar_cell_names:
        cell_pose = client.simGetObjectPose(name)
        cell_position = cell_pose.position
        distance = math.sqrt((drone_position.x_val - cell_position.x_val)**2 +
                             (drone_position.y_val - cell_position.y_val)**2 +
                             (drone_position.z_val - cell_position.z_val)**2)
        distances.append(distance)

    # Find the closest solar cell object that is within a certain distance threshold
    min_distance = float('inf')
    closest_cell_index = None
    for i, distance in enumerate(distances):
        if distance <= 5:  # threshold distance of 5 meters
            if distance < min_distance:
                min_distance = distance
                closest_cell_index = i

    # Return the name of the closest solar cell object
    if closest_cell_index is not None:
        closest_cell_name = solar_cell_names[closest_cell_index]
        return closest_cell_name
    else:
        return None

# Set the thread flag to indicate whether the drone altitude thread is running or not
drone_altitude_thread_running = False
x = 0
# Define a function to run the drone altitude subprocess in a separate thread
def run_drone_altitude_thread():
    global drone_altitude_thread_running
    drone_altitude_thread_running = True
    subprocess.call(["python", "C:\\Users\\frost\\Desktop\\airsim_api\\AirSim\\PythonClient\\multirotor\\droneAltitude.py"])
    #drone_altitude_thread_running = False
    global x
    x = 20



# Define a function to move the solar cell
def move_solar_cell(solar_cell_name, solar_cell_pose, solar_cell_position):
    pitch = 0
    roll = 0
    yaw = 0

    # Convert the Euler angles to a quaternion
    quat = airsim.to_quaternion(math.radians(pitch), math.radians(roll), math.radians(yaw))

    # get the initial orientation of the solar cell
    init_quat = solar_cell_pose.orientation

    while True:
        drone_position = client.getMultirotorState().kinematics_estimated.position
        drone_x = drone_position.x_val
        drone_y = drone_position.y_val
        drone_z = drone_position.z_val + 3

        # Start the drone altitude thread if it's not already running
        if not drone_altitude_thread_running:
            drone_altitude_thread = threading.Thread(target=run_drone_altitude_thread)
            drone_altitude_thread.start()


        # Adjust the z coordinate based on the calculated drop height
        drop_height = solar_cell_position.z_val - 2.0
        if drone_z > drop_height:
            drone_z = drop_height

        # set the solar cell pose with the initial orientation
        client.simSetObjectPose(solar_cell_name, airsim.Pose(airsim.Vector3r(drone_x, drone_y, drone_z), init_quat))

        if x == 20:
            # get the drone's current orientation
            drone_orient = client.simGetVehiclePose().orientation

            # Drop the solar cell with the current orientation
            client.simSetObjectPose(solar_cell_name, airsim.Pose(airsim.Vector3r(drone_x, drone_y, drone_z), drone_orient))
            time.sleep(0.1)
            drone_z = solar_cell_position.z_val
            client.simSetObjectPose(solar_cell_name, airsim.Pose(airsim.Vector3r(drone_x, drone_y, drone_z), drone_orient))
            break

current_solar = update_current_solar_cell_index()
print(current_solar)
solar_cell_name = str(current_solar)
solar_cell_pose = client.simGetObjectPose(solar_cell_name)
solar_cell_position = solar_cell_pose.position
move_solar_cell(solar_cell_name, solar_cell_pose, solar_cell_position)


