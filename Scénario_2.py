#!/usr/bin/python3
#  -*- coding: utf-8 -*-

# Date: Fri 25 MAY 2021 15:00:50 UTC+1
# Author: Paul CHARACHON
# Description: Scénario 1: Faire un arc de cercle
# avec un panneau solaire, en s'arretant toute les 0.5 secondes
# Last Modified : Tue 25 MAY 2021 18:50
# Python Version 3.9
# Used https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/using-the-adafruit-library
import time
from adafruit_motor import servo
from adafruit_servokit import ServoKit
kit = ServoKit(channels=13)
"""defining the total number of pins on my microcontroller """
def servo_horizontale(position_start, position_final, sens):

""" defining the horizontal movement"""

while position < position_final:
    position = position_start
    kit.servo[0].angle = position_start
    position = position + int(sens) * 5
""" updating the new value of the angle of the servo"""
    time.sleep(0, 5)
    break

def servo_verticale(position_start, position_final, sens):

""" defining the horizontal movement"""

while position < position_final:
    position_2 = position_start
    kit.servo[0].angle = position_2
    position_2 = position_2 + int(sens) * 5
    """ updating the new value of the angle of the servo"""
    time.sleep(0, 5)
    break


def scénario_1():
	""" definfing the first scenario"""
    While position_2 < 90:
    """ sets a condition for vertical position and also sunrise"""
        servo_horizontale(0, 90, 1)
        servo_verticale(0, 90, 1)

    While position_2 > 0:
    """sundown = afternoon"""
        servo_horizontale(90, 180, 1)
        servo_verticale(90, 0, -1)
