import setup_path
import airsim
import cv2
import numpy as np
import pprint
import math

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)

client.armDisarm(True)
client.takeoffAsync().join()

# set camera name and image type to request images and detections
camera_name = "0"
image_type = airsim.ImageType.Scene

# set detection radius in [cm]
client.simSetDetectionFilterRadius(camera_name, image_type, 200 * 100)
# add desired object name to detect in wild card/regex format
client.simAddDetectionFilterMeshName(camera_name, image_type, "SolarCells*")


def distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1.x_val - p2.x_val) ** 2 + (p1.y_val - p2.y_val) ** 2 + (p1.z_val - p2.z_val) ** 2)
#
#




def imageCapture(endCount):
    i = 0
    end = endCount
    closest_distance = float('inf')
    closest_solar_cell = None
    solar_cells_list = []  # create an empty list to store detected solar cells
    while i < end:
        rawImage = client.simGetImage(camera_name, image_type)
        if not rawImage:
            continue
        png = cv2.imdecode(airsim.string_to_uint8_array(rawImage), cv2.IMREAD_UNCHANGED)
        solarCells = client.simGetDetections(camera_name, image_type)
        if solarCells:
            for solarCell in solarCells:

                #s = pprint.pformat(solarCell)
                #print("SolarCell: %s" % s)

                cv2.rectangle(png, (int(solarCell.box2D.min.x_val), int(solarCell.box2D.min.y_val)),
                              (int(solarCell.box2D.max.x_val), int(solarCell.box2D.max.y_val)), (255, 0, 0), 2)
                cv2.putText(png, solarCell.name, (int(solarCell.box2D.min.x_val), int(solarCell.box2D.min.y_val - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36, 255, 12))

                # append detected solar cell to the list
                solar_cells_list.append(solarCell)

                # Calculate distance from drone to solar cell
                solar_cell_centroid = airsim.Vector3r((solarCell.box2D.min.x_val + solarCell.box2D.max.x_val) / 2,
                                                      (solarCell.box2D.min.y_val + solarCell.box2D.max.y_val) / 2,
                                                      0)
                drone_pos = client.simGetVehiclePose().position
                d = distance(solar_cell_centroid, drone_pos)
                if d < closest_distance:
                    closest_distance = d
                    closest_solar_cell = solarCell

            # Print the closest solar cell and its distance from the drone
            # if closest_solar_cell is not None:
            #     print(f"Closest solar cell: {closest_solar_cell.name}")
            #     print(f"Distance: {closest_distance} meters")



        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif cv2.waitKey(1) & 0xFF == ord('c'):
            client.simClearDetectionMeshNames(camera_name, image_type)
        elif cv2.waitKey(1) & 0xFF == ord('a'):
            client.simAddDetectionFilterMeshName(camera_name, image_type, "solarCell*")
    # cv2.destroyAllWindows()

        cv2.imshow("AirSim", png)
        i += 1
        if i== end:
            break
    cv2.destroyAllWindows()
    print(f"Closest solar cell: {closest_solar_cell.name}")
    print(f"Distance: {closest_distance} meters")
    return closest_solar_cell


imageCapture(20)
    # cv2.destroyAllWindows()
#print(imageCapture(20))

solarNavigate = imageCapture(20)



# set the drone's speed
speed = 5

# navigate the drone towards the solar cell
while True:
    # get the current location of the drone
    drone_pos = client.getMultirotorState().kinematics_estimated.position

    # get the location of the closest solar cell
    solar_cell_pos = solarNavigate.geo_point

    # calculate the direction vector from the drone to the solar cell
    dir_vec = airsim.Vector3r(solar_cell_pos.x_val - drone_pos.x_val, solar_cell_pos.y_val - drone_pos.y_val, solar_cell_pos.z_val - drone_pos.z_val)

    # calculate the distance to the solar cell
    dist = dir_vec.get_length()

    # break out of the loop if the drone has reached the solar cell
    if dist < 1:
        break

    # normalize the direction vector
    dir_vec = dir_vec / dist

    # calculate the velocity vector
    vel_vec = dir_vec * speed

    # set the drone's velocity
    if dist > 2:
        client.moveByVelocityAsync(vel_vec.x_val, vel_vec.y_val, vel_vec.z_val, 0.1)
    else:
        client.moveByVelocityAsync(0, 0, 0, 0.1)

    # wait for a short time before the next iteration
    airsim.time.sleep(0.1)

# stop the drone
client.hoverAsync()

# Get the current drone position
#current_pos = client.simGetVehiclePose().position

# Calculate the direction vector towards the solar cell
# solar_cell_pos = airsim.Vector3r(solarNavigate.box2D.min.x_val + solarNavigate.box2D.max.x_val / 2,
#                                  solarNavigate.box2D.min.y_val + solarNavigate.box2D.max.y_val / 2, 0)
# direction = np.array(solar_cell_pos - current_pos)
# if direction == airsim.Vector3r(0, 0, 0):
#     direction = direction / airsim.utils.norm(direction)
#
# # Calculate the target position at a distance of 87.59 meters from the current position
# target_pos = current_pos + direction * 87.59
# #print(current_pos)
# print('\n')
#print(target_pos)
# set the drone's mode to "GUIDED"
#client.armDisarm(True)
#client.moveToPositionAsync(current_pos.x_val, current_pos.y_val, current_pos.z_val, 2).join()


# Navigate to the target position
#This will crash the engine for some reason
#client.moveToPositionAsync(target_pos.x_val, target_pos.y_val, target_pos.z_val, 10).join()
# Hover at the target position
#client.hoverAsync().join()

# release the API control
#client.enableApiControl(False)