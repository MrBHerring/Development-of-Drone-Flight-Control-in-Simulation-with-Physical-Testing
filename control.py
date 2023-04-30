import setup_path
import airsim
import numpy as np
import os
import tempfile
import sys
import time
import pprint
import cv2
from Drone_Auto import image_proc_algorithm



#connect and take off drone
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
#client.armDisarm(True)
#client.takeoffAsync()


state = client.getMultirotorState()
s = pprint.pformat(state)
print("state: %s" % s)

imu_data = client.getImuData()
s = pprint.pformat(imu_data)
print("imu_data: %s" % s)

barometer_data = client.getBarometerData()
s = pprint.pformat(barometer_data)
print("barometer_data: %s" % s)

magnetometer_data = client.getMagnetometerData()
s = pprint.pformat(magnetometer_data)
print("magnetometer_data: %s" % s)

gps_data = client.getGpsData()
s = pprint.pformat(gps_data)
print("gps_data: %s" % s)


airsim.wait_key('Press any key to takeoff')
print("Taking off...")
client.armDisarm(True)
client.takeoffAsync().join()
# z of -20 is 20 meters above the original launch point.
z = -1


state = client.getMultirotorState()
print("state: %s" % pprint.pformat(state))

#airsim.wait_key('Press any key to move vehicle to (-10, 10, -10) at 5 m/s')
#client.moveToPositionAsync(-10, 10, -10, 5).join()

state = client.getMultirotorState()
print("state: %s" % pprint.pformat(state))

client.hoverAsync().join()



# Fly given velocity vector for 1 seconds
duration = 9
speed = 4

vx = speed
vy = 0

##client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
##                            airsim.YawMode(False, 0))







while True:
    key = input("choose: 4 Turn right,  6 Turn left ,8 backwards ,2 straight ,0 get position, 3 to take images, any key to quit: ")
    if float(key) == 4:
        vx = 0
        vy = -speed
        client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                                airsim.YawMode(False, 270))
    elif float(key)==2:
        vx = -speed
        vy = 0
        client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                                airsim.YawMode(False, 180))
    elif float(key) == 6:
        vx = 0
        vy = speed
        client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                                airsim.YawMode(False, 90))
    elif float(key) == 8:
        vx = speed
        vy = 0
        client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                         airsim.YawMode(False, 0))
    elif float(key) == 0:
        print(client.getMultirotorState().kinematics_estimated.position)

    elif float(key) == 3:
        responses = client.simGetImages([airsim.ImageRequest("0", airsim.ImageType.DepthVis),  #depth visualization image
            airsim.ImageRequest("1", airsim.ImageType.DepthPerspective, True), #depth in perspective projection
            airsim.ImageRequest("1", airsim.ImageType.Scene), #scene vision image in png format
            airsim.ImageRequest("1", airsim.ImageType.Scene, False, False)])  #scene vision image in uncompressed RGBA array
        print('Retrieved images: %d' % len(responses))

        tmp_dir = os.path.join(tempfile.gettempdir(), "airsim_drone")
        print ("Saving images to %s" % tmp_dir)
        try:
            os.makedirs(tmp_dir)
        except OSError:
            if not os.path.isdir(tmp_dir):
                raise

        for idx, response in enumerate(responses):

            filename = os.path.join(tmp_dir, str(idx))

            if response.pixels_as_float:
                print("Type %d, size %d" % (response.image_type, len(response.image_data_float)))
                airsim.write_pfm(os.path.normpath(filename + '.pfm'), airsim.get_pfm_array(response))
            elif response.compress: #png format
                print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
                airsim.write_file(os.path.normpath(filename + '.png'), response.image_data_uint8)
            else: #uncompressed array
                print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
                img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8) # get numpy array
                img_rgb = img1d.reshape(response.height, response.width, 3) # reshape array to 4 channel image array H X W X 3
                cv2.imwrite(os.path.normpath(filename + '.png'), img_rgb) # write to png
        
    else:
        break
        


        
    
airsim.wait_key('Press any key to reset to original state')
client.reset()
client.armDisarm(False)


# let's quit cleanly
client.enableApiControl(False)
