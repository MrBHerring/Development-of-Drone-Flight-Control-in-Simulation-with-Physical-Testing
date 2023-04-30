import setup_path
import airsim
import keyboard
import math
import time

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True, "Drone1")
client.enableApiControl(True, "Drone2")
client.enableApiControl(True, "Drone3")
client.enableApiControl(True, "Drone4")
client.enableApiControl(True, "Drone5")
client.enableApiControl(True, "Drone6")


def preflight():
    # airsim.wait_key('Press any key to takeoff')
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

    # solar.imageCapture(count)

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

    # solar.imageCapture(count)

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


    #                             airsim.YawMode(False, 90), vehicle_name="Drone6")
    # count = 50
    # solar.imageCapture(count)

    f1.join()
    f2.join()
    f3.join()
    f4.join()
    f5.join()
    f6.join()


preflight()
time.sleep(5)


# cleaning cell process
cleaned_cells = []

# Hold all the home solar base
solar_cell_base = []
objects = client.simListSceneObjects()
solar_cells_base_list = []

for object_name in objects:
    if 'Solarbase' in object_name:
        # Add the name of the solar cell object to the list
        solar_cell_base.append(object_name)
for solar_cell_pose in solar_cell_base:
    solar_cell_pose = client.simGetObjectPose(solar_cell_pose)
    solar_cell_location = solar_cell_pose.position
    x, y, z = solar_cell_location.x_val, solar_cell_location.y_val, solar_cell_location.z_val
    solar_cells_base_list.append((x, y))

# Saves all the solar cell names
solar_cell_names = []
objects = client.simListSceneObjects()
solar_cells_list = []
for object_name in objects:
    if 'SolarCells' in object_name:
        # Add the name of the solar cell object to the list
        solar_cell_names.append(object_name)
for solar_cell_pose in solar_cell_names:
    solar_cell_pose = client.simGetObjectPose(solar_cell_pose)
    solar_cell_location = solar_cell_pose.position
    x, y, z = solar_cell_location.x_val, solar_cell_location.y_val, solar_cell_location.z_val
    solar_cells_list.append((x, y))

# change orentiaon
pitch = 0
roll = 80
yaw = 0

# Convert the Euler angles to a quaternion
quat = airsim.to_quaternion(math.radians(pitch), math.radians(roll), math.radians(yaw))


def solar_pick(cell,currentDrone,currentPoint):
    while True:
        drone_position = client.getMultirotorState(vehicle_name=currentDrone).kinematics_estimated.position
        drone_x = drone_position.x_val
        drone_y = drone_position.y_val
        drone_z = drone_position.z_val + 3

        # Keep solar cell from falling below a certain z
        if abs(drone_x - currentPoint.x_val) <= 3 and abs(drone_y - currentPoint.y_val) <= 3:
            client.simSetObjectPose(cell, airsim.Pose(
                airsim.Vector3r(currentPoint.x_val, currentPoint.y_val, - 1), quat))
            break
        # if drone_z < -5:
        #     client.simSetObjectPose(cell, airsim.Pose(airsim.Vector3r(drone_x, drone_y, drone_z), quat, ))

        client.simSetObjectPose(cell, airsim.Pose(airsim.Vector3r(drone_x, drone_y, - 2), quat))
    #time.sleep(3)

    # Move the drone slightly away from the cell's position
    client.moveByVelocityAsync(1, 0, 0, 1, vehicle_name=currentDrone)
    time.sleep(1)



def next_to_clean(currentDrone):
    global cleaned_cells



    for cell in solar_cell_names:
        if cell in cleaned_cells:
            continue  # Skip cells that have already been cleaned
        if currentDrone == "Drone1":
            nextDrone = "Drone2"

            firstPoint = "SolarPoint"
            secondPoint = "SolarPoint2"

        elif currentDrone == "Drone2":
            currentDrone = "Drone3"
            nextDrone = "Drone4"

            firstPoint = "SolarPoint3"
            secondPoint = "SolarPoint4"




        elif currentDrone == "Drone4":
            currentDrone = "Drone5"
            nextDrone = "Drone6"

            firstPoint = "SolarPoint5"
            secondPoint = "SolarPoint6"


        else:
            currentDrone = "Drone1"
            nextDrone = "Drone2"

            firstPoint = "SolarPoint"
            secondPoint = "SolarPoint2"


        # Get the pose of Solar Point
        solar_point_name = firstPoint
        solar_point_pose = client.simGetObjectPose(solar_point_name)
        if solar_point_pose.position != (None, None, None):
            # Get the position of Solar Point6
            solar_point_position = solar_point_pose.position
            # Subtract 2 from the z value of Solar Point6
            solar_point_position.x_val += 4
            solar_point_position.z_val -= 10
        else:
            print(f"{solar_point_name} does not have a valid position")

        # Get the pose of next Solar Point
        solar_point_name2 = secondPoint
        solar_point_pose2 = client.simGetObjectPose(solar_point_name2)
        if solar_point_pose2.position != (None, None, None):
            # Get the position of Solar Point6
            solar_point_position2 = solar_point_pose2.position
            # Subtract 2 from the z value of Solar Point6
            solar_point_position2.x_val += 4
            solar_point_position2.z_val -= 10
        else:
            print(f"{solar_point_name2} does not have a valid position")


        client.moveToPositionAsync(client.simGetObjectPose(cell).position.x_val + 1,
                                   client.simGetObjectPose(cell).position.y_val - 2, - 6, velocity=10,
                                   vehicle_name=currentDrone).join()

        #time.sleep(5)
        client.moveToPositionAsync(solar_point_position.x_val, solar_point_position.y_val, solar_point_position.z_val, velocity=10, vehicle_name=currentDrone)
        currentPoint = solar_point_position
        solar_pick(cell,currentDrone,currentPoint)

        cleaned_cells.append(cell)
        #time.sleep(2)
        if len(cleaned_cells) == len(solar_cell_names):
            print("All solar cells are cleaned.")
            return

        # switch to the other drone to pick up the next cell
        next_to_pick = solar_cell_names[len(cleaned_cells)]

        client.moveToPositionAsync(client.simGetObjectPose(next_to_pick).position.x_val + 1,
                                   client.simGetObjectPose(next_to_pick).position.y_val - 2, - 6, velocity=10,
                                   vehicle_name=nextDrone).join()

        #time.sleep(5)
        client.moveToPositionAsync(solar_point_position2.x_val, solar_point_position2.y_val, solar_point_position2.z_val, velocity=10, vehicle_name=nextDrone)
        currentPoint = solar_point_position2
        solar_pick(next_to_pick, nextDrone,currentPoint)

        cleaned_cells.append(next_to_pick)
        currentDrone = nextDrone
        #time.sleep(2)

    #print("we're done cleaning")


currentDrone = "Drone1"
next_to_clean(currentDrone)
