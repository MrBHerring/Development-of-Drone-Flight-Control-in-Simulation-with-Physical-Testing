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
import threading


# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True, "Drone2")
client.armDisarm(True, "Drone2")
client.simEnableWeather(True)

##client.enableApiControl(True, "Drone2")
##client.armDisarm(True, "Drone2")


def flytocell2():
    # Connect to the AirSim simulator
    # client = airsim.MultirotorClient()
    # client.confirmConnection()
    # client.enableApiControl(True, "Drone1")

    f1 = client.takeoffAsync(vehicle_name="Drone2")
    f1.join()

    # Retrieve the pose of SolarCell6
    solar_cell_name = "SolarCells4"
    solar_cell_pose = client.simGetObjectPose(solar_cell_name)
    if solar_cell_pose.position != (None, None, None):
        # Do something with solar cell pose
        pass
    else:
        print(f"{solar_cell_name} does not have a valid position")

    solar_cell_pose = client.simGetObjectPose(solar_cell_name)
    solar_cell_location = solar_cell_pose.position
    # Calculate center coordinates of the solar cell
    cell_width = 0.2  # width of the solar cell
    cell_center_x = solar_cell_location.x_val - 2
    cell_center_y = solar_cell_location.y_val - 2
    cell_center_z = (solar_cell_location.z_val - cell_width / 2) - 4
    # Move the drone to Solar Cell 6
    print(f"Moving to Solar Cell 4 at ({cell_center_x}, {cell_center_y}, {cell_center_z})")
    client.moveToPositionAsync(cell_center_x, cell_center_y, cell_center_z - 1, velocity=2,
                               vehicle_name="Drone2").join()

    # # Calculate distance to solar cell
    # distance = math.inf
    # while distance > 0.5:
    #     # Get drone position
    #     drone_position = client.getMultirotorState().kinematics_estimated.position
    #     drone_x, drone_y, drone_z = drone_position.x_val, drone_position.y_val, drone_position.z_val
    #
    #     # Calculate distance to solar cell
    #     distance = math.sqrt(
    #         (drone_x - cell_center_x) ** 2 + (drone_y - cell_center_y) ** 2 + (drone_z - cell_center_z) ** 2)
    #
    #     time.sleep(0.1)

    # Hover over the cell
    print("Reached Solar Cell 4. Hovering.")

    # Disarm the drone
##    client.armDisarm(False)




def preflight2():
    #airsim.wait_key('Press any key to takeoff')
    f1 = client.takeoffAsync(vehicle_name="Drone1")
    f2 = client.takeoffAsync(vehicle_name="Drone2")
    f1.join()
    f2.join()

    z = -2
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

    #solar.imageCapture(count)

    f1.join()
    f2.join()


    print("moving by velocity vx=" + str(vx) + ", vy=" + str(vy) + ", yaw=90")
    f1 = client.moveByVelocityZAsync(0, 4, z, 10, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                airsim.YawMode(False, 90), vehicle_name="Drone1")

    f2 = client.moveByVelocityZAsync(0, 4, z, 10, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 90), vehicle_name="Drone2")

    #solar.imageCapture(count)

    f1.join()
    f2.join()



    print("moving by velocity vx=" + str(vx) + ", vy=" + str(vy) + ", yaw=180")
    f1 = client.moveByVelocityZAsync(-4, 0, z, 9, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                airsim.YawMode(False, 180), vehicle_name="Drone1")

    f2 = client.moveByVelocityZAsync(-4, 0, z, 9, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 180), vehicle_name="Drone2")


    #solar.imageCapture(count)

    f1.join()
    f2.join()


    print("moving by velocity vx=" + str(vx) + ", vy=" + str(vy) + ", yaw=90")
    f1 = client.moveByVelocityZAsync(0, 4, z, 12, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                airsim.YawMode(False, 90), vehicle_name="Drone1")

    f2 = client.moveByVelocityZAsync(0, 4, z, 12, airsim.DrivetrainType.MaxDegreeOfFreedom,
                            airsim.YawMode(False, 90), vehicle_name="Drone2")




    #                             airsim.YawMode(False, 90), vehicle_name="Drone6")
    #count = 50
    #solar.imageCapture(count)


    f1.join()
    f2.join()

preflight2()
#after Drone 1
#time.sleep(6)

flytocell2()
time.sleep(5)

##client.hoverAsync().join()
#client.takeoffAsync(vehicle_name="Drone1").join()



client.takeoffAsync(vehicle_name="Drone2")

# Set the thread flag to indicate whether the drone altitude thread is running or not
drone_altitude_thread_running = False
x = "Processing"

# Define a function to run the drone altitude subprocess in a separate thread
def run_drone_altitude_thread2():
    global drone_altitude_thread_running
    drone_altitude_thread_running = True
    # Replace this with your file location
    subprocess.call(["python", "C:\\Users\\frost\\Desktop\\airsim_api\\AirSim\\PythonClient\\multirotor\\Drone2CarryFly.py"])
    #drone_altitude_thread_running = False
    global x
    x = "Done"



# Define a function to move the solar cell
def move_solar_cell2(solar_cell_name, solar_cell_pose, solar_cell_position):


    pitch = 0
    roll = 0
    yaw = 0

    # Convert the Euler angles to a quaternion
    quat = airsim.to_quaternion(math.radians(pitch), math.radians(roll), math.radians(yaw))

    # get the initial orientation of the solar cell
    init_quat = solar_cell_pose.orientation

    while True:
##        client.armDisarm(False)
        drone_position = client.getMultirotorState().kinematics_estimated.position
        drone_x = drone_position.x_val + 3
        drone_y = drone_position.y_val
        drone_z = drone_position.z_val + 4

        # Start the drone altitude thread if it's not already running
        if not drone_altitude_thread_running:
            drone_altitude_thread = threading.Thread(target=run_drone_altitude_thread2)
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


time.sleep(8)
current_solar = "SolarCells4"
print(current_solar)
solar_cell_name = str(current_solar)
solar_cell_pose = client.simGetObjectPose(solar_cell_name)
solar_cell_position = solar_cell_pose.position
move_solar_cell2(solar_cell_name, solar_cell_pose, solar_cell_position)





