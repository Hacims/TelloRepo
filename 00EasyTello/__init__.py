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

# Turning on stream
my_drone.streamon()



my_drone.takeoff()

for i in range(4):
    my_drone.forward(50)
    my_drone.cw(90)

my_drone.land()

# Turning off stream
my_drone.streamoff()