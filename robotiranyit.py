from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here.
ev3 = EV3Brick()

#motorok kezelése
jm = Motor(Port.B)
bm = Motor(Port.C)
km = Motor(Port.A)

#szenzorok
us = UltrasonicSensor(Port.S4)
ts = TouchSensor(Port.S1)
cs = ColorSensor(Port.S3)
gs = GyroSensor(Port.S2)
robot = DriveBase(jm, bm, 55, 142)

class Robotiranyit():

    def __init__(self):
        # Create your objects here.
        self.ev3 = EV3Brick()

        #motorok kezelése
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)

        #szenzorok
        self.us = UltrasonicSensor(Port.S4)
        self.ts = TouchSensor(Port.S1)
        self.cs = ColorSensor(Port.S3)
        self.gs = GyroSensor(Port.S2)
        self.robot = DriveBase(self.jm, self.bm, 55, 142)

    def fordula(self):
        #mindkét motor azonos sebességgel megy
        self.robot.turn(360)
        self.ev3.speaker.beep()

    def fordulb(self):
        #ellentétes irányba mozognak a motorok
        self.robot.turn(360)
    
    def fordulc(self):
        #egy irányba más sebességgel mozognak a motorok
        self.jm.drive(100)
        self.jm.turn(90)
        wait(1)
        self.bm.drive(100)
        self.bm.turn(90)
        

