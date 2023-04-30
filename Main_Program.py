import setup_path
import airsim
import keyboard
import math
# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.takeoffAsync().join()

print("Press '1' to go to solar base\nPress '2' to go to home base\nPress '3' to go to cleaning base\nPress '4' to go to pick up closes solar cell")

def Solar_pickup():
    print("You are now picking up solar cell press 'enter' to drop")
#Homebase program
def Home_base():
    print("Now returning back to the home base\n")
    print("**You must manually land**")
    # get the current position of the drone
    current_pos = client.getMultirotorState().kinematics_estimated.position
    # set the target position to the base location
    base_pos = airsim.Vector3r(-10, 10, 10)
    target_pos = airsim.Vector3r(base_pos.x_val, base_pos.y_val, current_pos.z_val + 5) # increase altitude by 5 meters
    # move the drone to the target position
    velocity = 10 # meters per second
    client.moveToPositionAsync(target_pos.x_val, target_pos.y_val, target_pos.z_val, velocity).join()
    print("Press 5 to land when returned to base")

def Clean_base():
    print("Heading to the cleaning station")
    # set the target position/ angle
    target_pos = airsim.Vector3r(-190, 80, -5)
    # move the drone to the specific (x,y) target position 
    velocity = 10  # meters per second
    client.moveToPositionAsync(target_pos.x_val, target_pos.y_val, target_pos.z_val, velocity).join()
    
def Move_closes_cell():
    target_x, target_y = closes_cell()
    target_z=-3
    print(f"Moving to closest solar cell at ({target_x}, {target_y})")  
    client.moveToPositionAsync(target_x, target_y, target_z, velocity=10).join()

    
def Land_drone():
    # land the drone at the base location
    client.armDisarm(True)
    #Gets current postion
    drone_pos = client.getMultirotorState().kinematics_estimated.position
    z_position=drone_pos.z_val
    y_position= drone_pos.y_val
    x_position=drone_pos.x_val
    # set the base position
    base_pos = airsim.Vector3r(-10, 10, 0)
    landed = client.getMultirotorState().landed_state
    if landed == airsim.LandedState.Landed:
        print("already landed...")
    else:
        print("Now landing...")
        while True:
            # check if drone is above ground level
            if z_position <= base_pos.z_val:
                break
            # reduce altitude and velocity during landing procedure
            altitude = z_position - 2
            velocity = 2 # meters per second
            client.moveToPositionAsync(x_position, y_position, altitude, velocity).join()
            # update the current position of the drone
            drone_pos = client.getMultirotorState().kinematics_estimated.position
            z_position=drone_pos.z_val
            y_position= drone_pos.y_val
            x_position=drone_pos.x_val
        
        # land the drone
        client.landAsync().join()
    client.armDisarm(False)
    
def closes_cell():
    # Assuming you have a list of solar cells called "solar_cells_list"
    solar_cell_names = []
    objects = client.simListSceneObjects()
    solar_cells_list=[]
    for object_name in objects:
        if 'SolarCells' in object_name:
            # Add the name of the solar cell object to the list
            solar_cell_names.append(object_name)      
    # Retrieve the locations of all solar cells
    for solar_cell_pose in solar_cell_names:
        solar_cell_pose = client.simGetObjectPose(solar_cell_pose)
        solar_cell_location = solar_cell_pose.position
        x, y, z = solar_cell_location.x_val, solar_cell_location.y_val, solar_cell_location.z_val
        solar_cells_list.append((x, y))  
    closest_solar_cell = None
    closest_distance = math.inf
    # Get the drone's current position
    drone_position = client.getMultirotorState().kinematics_estimated.position
    drone_x, drone_y, drone_z = drone_position.x_val, drone_position.y_val, drone_position.z_val
    #Calculates closest cell
    for solar_cell in solar_cells_list:
        solar_cell_x, solar_cell_y = solar_cell
        distance = math.sqrt((solar_cell_x - drone_x)**2 + (solar_cell_y - drone_y)**2)
        if distance < closest_distance:
            closest_distance = distance
            closest_solar_cell = solar_cell
        return closest_solar_cell






# Set up keyboard listeners
keyboard.add_hotkey('1', Move_closes_cell)
keyboard.add_hotkey('2', Home_base)
keyboard.add_hotkey('3', Clean_base)
keyboard.add_hotkey('4', Solar_pickup)
keyboard.add_hotkey('5', Land_drone)

# Start listening for key presses
keyboard.wait()
