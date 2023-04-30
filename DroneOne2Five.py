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
client.enableApiControl(True, "Drone1")
client.armDisarm(True, "Drone1")
client.enableApiControl(True, "Drone2")
client.armDisarm(True, "Drone2")
client.enableApiControl(True, "Drone3")
client.armDisarm(True, "Drone3")
client.enableApiControl(True, "Drone4")
client.armDisarm(True, "Drone4")
client.enableApiControl(True, "Drone5")
client.armDisarm(True, "Drone5")


def flytocell():
    # Connect to the AirSim simulator
    # client = airsim.MultirotorClient()
    # client.confirmConnection()
    # client.enableApiControl(True, "Drone1")

    f1 = client.takeoffAsync(vehicle_name="Drone1")
    f2 = client.takeoffAsync(vehicle_name="Drone2")
    f3 = client.takeoffAsync(vehicle_name="Drone3")
    f4 = client.takeoffAsync(vehicle_name="Drone4")
    f5 = client.takeoffAsync(vehicle_name="Drone5")



    f1.join()
    f2.join()
    f3.join()
    f4.join()
    f5.join()


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
    cell_width = 0.2  # width of the solar cell
    cell_center_x = solar_cell_location.x_val - 2
    cell_center_y = solar_cell_location.y_val - 2
    cell_center_z = (solar_cell_location.z_val - cell_width / 2) - 4
    # Move the drone to Solar Cell 6
    print(f"Moving to {solar_cell_name} at ({cell_center_x}, {cell_center_y}, {cell_center_z})")
    f1 = client.moveToPositionAsync(cell_center_x, cell_center_y, cell_center_z - 1, velocity=2,
                                    vehicle_name="Drone1")
    print("Reached Solar Cell 6. Hovering.")


    time.sleep(2)

    # Retrieve the pose of SolarCell4
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
    # Move the drone to Solar Cell 4
    print(f"Moving to Solar Cell 4 at ({cell_center_x}, {cell_center_y}, {cell_center_z})")

    f2 = client.moveToPositionAsync(cell_center_x + 1, cell_center_y, cell_center_z - 1, velocity=2,
                                    vehicle_name="Drone2")
    print("Reached Solar Cell 4. Hovering.")

    time.sleep(2)


    # Retrieve the pose of SolarCell2
    solar_cell_name = "SolarCells2_10"
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
    # Move the drone to Solar Cell 2
    print(f"Moving to Solar Cell 2 at ({cell_center_x}, {cell_center_y}, {cell_center_z})")

    f3 = client.moveToPositionAsync(cell_center_x - 3, cell_center_y, cell_center_z - 0, velocity=2,
                                    vehicle_name="Drone3")
    print("Reached Solar Cell 2. Hovering.")

    time.sleep(2)

    # Retrieve the pose of SolarCell5
    solar_cell_name = "SolarCells5"
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
    # Move the drone to Solar Cell 5
    print(f"Moving to Solar Cell 5 at ({cell_center_x}, {cell_center_y}, {cell_center_z})")

    f4 = client.moveToPositionAsync(cell_center_x + 2, cell_center_y, cell_center_z - 0, velocity=2,
                                    vehicle_name="Drone4")
    print("Reached Solar Cell 5. Hovering.")

    time.sleep(2)

    # Retrieve the pose of SolarCell3
    solar_cell_name = "SolarCells3"
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
    # Move the drone to Solar Cell 5
    print(f"Moving to Solar Cell 3 at ({cell_center_x}, {cell_center_y}, {cell_center_z})")

    f5 = client.moveToPositionAsync(cell_center_x - 1, cell_center_y, cell_center_z - 0, velocity=2,
                                    vehicle_name="Drone5")
    print("Reached Solar Cell 3. Hovering.")

    time.sleep(2)





    f1.join()
    f2.join()
    f3.join()
    f4.join()
    f5.join()


    time.sleep(5)

    a1 = client.landAsync(vehicle_name="Drone1")
    a2 = client.landAsync(vehicle_name="Drone2")
    a3 = client.landAsync(vehicle_name="Drone3")
    a4 = client.landAsync(vehicle_name="Drone4")
    a5 = client.landAsync(vehicle_name="Drone5")

    a1.join()
    a2.join()
    a3.join()
    a4.join()
    a5.join()

    # Disarm the drone
    # client.armDisarm(False)
    time.sleep(2)


def preflight():
    # airsim.wait_key('Press any key to takeoff')
    f1 = client.takeoffAsync(vehicle_name="Drone1")
    f2 = client.takeoffAsync(vehicle_name="Drone2")
    f3 = client.takeoffAsync(vehicle_name="Drone3")
    f4 = client.takeoffAsync(vehicle_name="Drone4")
    f5 = client.takeoffAsync(vehicle_name="Drone5")

    f1.join()
    f2.join()
    f3.join()
    f4.join()
    f5.join()


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

    f3 = client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                     airsim.YawMode(False, 180), vehicle_name="Drone3")

    f4 = client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                     airsim.YawMode(False, 180), vehicle_name="Drone4")

    f5 = client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                     airsim.YawMode(False, 180), vehicle_name="Drone5")

    # solar.imageCapture(count)

    f1.join()
    f2.join()
    f3.join()
    f4.join()
    f5.join()

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

    # solar.imageCapture(count)

    f1.join()
    f2.join()
    f3.join()
    f4.join()
    f5.join()

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

    # solar.imageCapture(count)

    f1.join()
    f2.join()
    f3.join()
    f4.join()
    f5.join()

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

    #                             airsim.YawMode(False, 90), vehicle_name="Drone6")
    # count = 50
    # solar.imageCapture(count)

    f1.join()
    f2.join()
    f3.join()
    f4.join()
    f5.join()


preflight()
time.sleep(2)

##nextDrone = "Drone1"
##nextCell = "SolarCells6"
##
##
##flytocell(nextDrone,nextCell)

flytocell()



def drone1_control():
    subprocess.call(["python", "C:\\Users\\frost\\Desktop\\airsim_api\\AirSim\\PythonClient\\multirotor\\Drone1CellPickUp.py"])

def drone2_control():
    subprocess.call(["python", "C:\\Users\\frost\\Desktop\\airsim_api\\AirSim\\PythonClient\\multirotor\\Drone2CellPickUp.py"])

def drone3_control():
    subprocess.call(["python", "C:\\Users\\frost\\Desktop\\airsim_api\\AirSim\\PythonClient\\multirotor\\Drone3CellPickUp.py"])

def drone4_control():
    subprocess.call(["python", "C:\\Users\\frost\\Desktop\\airsim_api\\AirSim\\PythonClient\\multirotor\\Drone4CellPickUp.py"])

def drone5_control():
    subprocess.call(["python", "C:\\Users\\frost\\Desktop\\airsim_api\\AirSim\\PythonClient\\multirotor\\Drone5CellPickUp.py"])

# Create the threads
t1 = threading.Thread(target=drone1_control)
t2 = threading.Thread(target=drone2_control)
t3 = threading.Thread(target=drone3_control)
t4 = threading.Thread(target=drone4_control)
t5 = threading.Thread(target=drone5_control)


# Start the threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()


# Wait for both threads to finish
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

