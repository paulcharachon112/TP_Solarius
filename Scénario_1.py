#!/usr/bin/python3
#  -*- coding: utf-8 -*-

# Date: Fri 25 MAY 2021 15:00:50 UTC+1
# Author: Paul CHARACHON
# Description: Scénario 1: Faire un arc de cercle
# avec un panneau solaire, en s'arretant toute les 0.5 secondes
# Last Modified : Tue 1 June 2021 15:50
# Python Version 3.9
# Used https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-
# raspberry-pi/using-the-adafruit-library
import time
from adafruit_motor import servo
from adafruit_servokit import ServoKit
kit = ServoKit(channels=13)
"""defining the total number of pins on my microcontroller """


def servo_horizontale(position):
    """ defining the horizontal left movement, takes the new value at the start
    of each iteration"""

    kit.servo[0].angle = position
    time.sleep(0, 5)


def servo_verticale_montée(position):
    """ defining the vertial up movement, takes the new value at the start
    of each iteration"""

    kit.servo[1].angle = position
    time.sleep(0, 5)


def servo_verticale_descente(position):
    """ defining the vertical down movement, takes the new value at the start of
    each iteration"""

    kit.servo[1].angle = position
    time.sleep(0, 5)


def scénario_1():
    """ definfing the first scenario, setting up key point values, so at the
        beginning and at the middle"""

    position_actuelle_horizontale_sunrise = 0
    position_actuelle_verticale_sunrise = 0
    position_actuelle_horizontale_sundown = 90
    position_actuelle_verticale_sundown = 90

    While position_actuelle_verticale_sunrise < 90:
    """ Rise of the solar panel, until the peak at midday/sunrise"""

        servo_horizontale(position_actuelle_horizontale_sunrise)
        servo_verticale_montée(position_actuelle_verticale_sunrise)
        """increments both position variables to update the position"""
        position_actuelle_horizontale_sunrise = +=5
        position_actuelle_horizontale_sunrise = +=5

    While position_actuelle_verticale_sundown > 0:
    """sundown = afternoon, the panel continues to rotate to the left but 
        goes down"""
        servo_horizontale(position_actuelle_horizontale_sundown)
        servo_verticale_descente(position_actuelle_verticale_sundown)
        """increments both position variables to update the position"""
        position_actuelle_horizontale_sundown = +=5
        position_actuelle_verticale_sundown = -=5
