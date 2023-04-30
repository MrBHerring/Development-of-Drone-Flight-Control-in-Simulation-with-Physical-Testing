import setup_path
import airsim
import time
import numpy as np
import os
import tempfile
import pprint
import cv2
import solarDetect as solar
#import closes_image as cell
#import Solar_pickupCoordinates as pickup




# connect to the AirSim simulator
# client = airsim.MultirotorClient()
# client.confirmConnection()
# client.enableApiControl(True)
#
#
# state = client.getMultirotorState()
# s = pprint.pformat(state)
# print("state: %s" % s)
#
# imu_data = client.getImuData()
# s = pprint.pformat(imu_data)
# print("imu_data: %s" % s)
#
# barometer_data = client.getBarometerData()
# s = pprint.pformat(barometer_data)
# print("barometer_data: %s" % s)
#
# magnetometer_data = client.getMagnetometerData()
# s = pprint.pformat(magnetometer_data)
# print("magnetometer_data: %s" % s)
#
# gps_data = client.getGpsData()
# s = pprint.pformat(gps_data)
# print("gps_data: %s" % s)
#
# airsim.wait_key('Press any key to takeoff')
# print("Taking off...")
# client.armDisarm(True)
#
# client.takeoffAsync().join()
#
#
#
# state = client.getMultirotorState()
# print("state: %s" % pprint.pformat(state))
#
# client.hoverAsync().join()








def prefly(drone):






    z = -1
    count = 110
    duration = 9
    speed = 4
    # straight
    vx = -speed
    vy = 0


    print("moving by velocity vx=" + str(vx) + ", vy=" + str(vy) + ", yaw=180")
    client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                airsim.YawMode(False, 180),drone)

    solar.imageCapture(count)
    #time.sleep(1)
    print("moving by velocity vx=" + str(vx) + ", vy=" + str(vy) + ", yaw=90")
    client.moveByVelocityZAsync(0, 4, z, 10, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                airsim.YawMode(False, 90),drone)
    solar.imageCapture(count)
    #time.sleep(1)
    print("moving by velocity vx=" + str(vx) + ", vy=" + str(vy) + ", yaw=180")
    client.moveByVelocityZAsync(-4, 0, z, 9, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                airsim.YawMode(False, 180),drone)
    solar.imageCapture(count)
    #time.sleep(1)
    print("moving by velocity vx=" + str(vx) + ", vy=" + str(vy) + ", yaw=90")
    client.moveByVelocityZAsync(0, 4, z, 12, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                airsim.YawMode(False, 90),drone)
    count = 180
    solar.imageCapture(count)
    time.sleep(1)
    #cell.closestObject()
    #time.sleep(1)
    #pickup.closestCell()
    #time.sleep(1)



    #time.sleep(10)

'''
if count == 1:
    duration = 10
    speed = 4
    vx = 0
    vy = speed
    # turn left
    print("moving by velocity vx=" + str(vx) + ", vy=" + str(vy) + ", yaw=90")
    client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                airsim.YawMode(False, 90))
    
    count += 1
    solar.imageCapture()
    #time.sleep(10)

if count == 2:
    # right
    duration = 9
    speed = 4
    vx = -speed
    vy = 0
    print("moving by velocity vx=" + str(vx) + ", vy=" + str(vy) + ", yaw=180")
    client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                airsim.YawMode(False, 180))
    count += 1
    solar.imageCapture()
    #time.sleep(10)

if count == 3:
    duration = 12
    speed = 4
    vx = 0
    vy = speed
    # turn left
    print("moving by velocity vx=" + str(vx) + ", vy=" + str(vy) + ", yaw=90")
    client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                airsim.YawMode(False, 90))
    count += 1
    solar.imageCapture()
    #time.sleep(10)
'''


#movementControl = 1
#begin = 0


#movementAlgorithm()






















#airsim.wait_key('Press any key to move vehicle')





'''
airsim.wait_key('Press any key to reset to original state')

client.reset()
client.armDisarm(False)

# that's enough fun for now. let's quit cleanly
client.enableApiControl(False)
'''

