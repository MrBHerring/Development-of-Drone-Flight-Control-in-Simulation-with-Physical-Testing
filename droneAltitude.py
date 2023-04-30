import setup_path
import airsim
import numpy as np
import math
import keyboard
import KeyboardControl as kc
import time
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)

def flightMovement():
    x = 0
    print("Working")
    if x != 1:
        # set target altitude to -5 meters
        target_altitude = -5

        # move drone to target altitude
        client.moveToZAsync(target_altitude, velocity=1).join()

        # set the drone's velocity in the x direction (forward)
        vx = 4

        # set the duration of the movement in seconds
        duration = 20

        # move the drone in the forward direction for the specified duration
        client.moveByVelocityAsync(vx, 0, 0, duration).join()
        time.sleep(3)

        x+=1



flightMovement()