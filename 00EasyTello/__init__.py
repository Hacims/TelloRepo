__title__ = 'easytello'
__author__ = 'Ezra Fielding'
__liscence__ = 'MIT'
__copyright__ = 'Copyright 2019 Ezra Fielding'
__version__ = '0.0.7'
__all__ = ['tello', 'stats']

#from .tello import Tello
#from .stats import Stats
#from easytello import tello
import tello
import time
my_drone = tello.Tello()

file_name = "command_1_DC8.txt"
f = open(file_name, "r")
commands = f.readlines()

for command in commands:
    if command != '' and command != '\n':
        command = command.rstrip()

        if command.find('delay') != -1:
            sec = float(command.partition('delay')[2])
            print ('delay %s' % sec)
            time.sleep(sec)
            pass
        elif command.find('command') != -1:
            my_drone.command()
        elif command.find('takeoff') != -1:
            my_drone.takeoff()
        elif command.find('land') != -1:
            my_drone.land()
        elif command.find('streamon') != -1:
            my_drone.streamon()
        elif command.find('streamoff') != -1:
            my_drone.streamoff()
        elif command.find('up') != -1:
            dist = int(command.partition('up')[2])
            my_drone.up(dist)
        elif command.find('down') != -1:
            dist = int(command.partition('down')[2])
            my_drone.down(dist)
        elif command.find('left') != -1:
            dist = int(command.partition('left')[2])
            my_drone.left(dist)
        elif command.find('right') != -1:
            dist = int(command.partition('right')[2])
            my_drone.right(dist)
        elif command.find('forward') != -1:
            dist = int(command.partition('forward')[2])
            my_drone.forward(dist)
        elif command.find('back') != -1:
            dist = int(command.partition('back')[2])
            my_drone.back(dist)
        elif command.find('cw') != -1:
            deg = int(command.partition('cw')[2])
            my_drone.cw(deg)
        elif command.find('ccw') != -1:
            dist = int(command.partition('ccw')[2])
            my_drone.ccw(dist)
        elif command.find('speed') != -1:
            speed = int(command.partition('speed')[2])
            my_drone.set_speed(speed)
        elif command.find('battery?') != -1:
            my_drone.get_battery()


# Turning on stream
#my_drone.streamon()



# my_drone.takeoff()
# time.sleep (5)
# my_drone.up(20)
# time.sleep(5)
# my_drone.set_speed(10)
# time.sleep(5)
# my_drone.forward(200)
# time.sleep(5)
# my_drone.cw(90)
# time.sleep(5)
# my_drone.forward(20)
# time.sleep(5)
# my_drone.cw(90)
# time.sleep(5)
# my_drone.forward(200)
# time.sleep(5)
# for i in range(4):
#     my_drone.forward(50)
#     my_drone.cw(90)

#my_drone.land()

# Turning off stream
#my_drone.streamoff()