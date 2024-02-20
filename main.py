#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import Robotiranyit

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

#főprogram
robotom = Robotiranyit.Robotiranyit()

'''
#főprogram
# A két motort együttesen mozgató osztaly példányosítása
robot = DriveBase(jm, bm, 45, 142)'''


# Write your program here.
robotom.fordula()




#pybricks.com/ev3-micropython