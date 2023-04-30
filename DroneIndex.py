import multiprocessing
import subprocess

def run_script1():
    # replace the command with the command to run script 1
    cmd = 'python DroneOne.py'
    subprocess.call(cmd, shell=True)

def run_script2():
    # replace the command with the command to run script 2
    cmd = 'python Drone2.py'
    subprocess.call(cmd, shell=True)

if __name__ == '__main__':
    # create two processes for running script 1 and script 2
    p1 = multiprocessing.Process(target=run_script1)
    p2 = multiprocessing.Process(target=run_script2)

    # start both processes
    p1.start()
    p2.start()

    # wait for both processes to complete
    p1.join()
    p2.join()

    print('Both scripts have completed.')
