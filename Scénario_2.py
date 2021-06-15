#!/usr/bin/python3
#  -*- coding: utf-8 -*-

# Date: Fri 25 MAY 2021 15:00:50 UTC+1
# Author: Paul CHARACHON
# Description: Scénario 2: Suivre la source de lumière
# à l'aide d'un seul capteur de lumière
# Last Modified : Tue 31 MAY 2021 18:50
# Python Version 3.9
# Used https://learn.adafruit.com/adafruit-16-channel-servo-driver-with
# -raspberry-pi/using-the-adafruit-library
from adafruit_motor import servo
from adafruit_servokit import ServoKit
from adafruit_circuitplayground import cp
from time import time, sleep
kit = ServoKit(channels=13)


def lights():
    """ randomimizing movements to comprare 4 light values, and finds the
    biggest value"""
    """collecting light value for up"""
    servo_verticale(int(position_verticale) + 10)
    lights_up = cp.light  # collecting light data
    """collecting light value for down; -10 for other side (+ -10 to return to
    orignial spot) """
    servo_verticale(int(position_verticale) - 20)
    lights_down = cp.light  # collecting light data
    servo_verticale(int(position_verticale))  # returning to original position
    """collecting light value for gauche"""
    servo_horizontale(int(position_horizontale) + 10)
    lights_gauche = cp.light  # collecting light data
    """collecting light value for droite; -10 for other side (+-10 to return to
    orignial spot) """
    servo_horizontale(int(position_horizontale) - 10)
    lights_droite = cp.light  # collecting light data
    # returning to original position
    servo_horizontale(int(position_horizontale))
    """comparing all of the values and finding the biggest one, storing it in a
    new variable"""
    light_values = {'up': lights_up, 'down': lights_down,
                    'gauche': lights_gauche, 'droite': lights_droite}
    strongest_light = max(light_values, key=light_values.get)


def servo_horizontale(position):
    """ defining the horizontal left movement, takes the new value at the start
    of each iteration"""

    kit.servo[1].angle = position
    time.sleep(0, 5)


def servo_verticale(position):
    """ defining the vertial up movement, takes the new value at the start
    of each iteration"""

    kit.servo[4].angle = position
    time.sleep(0, 5)


def scénario_2():
    """ defining the second scenario, every 2 seconds it searches for the best
    value for light, then turns towards that light"""
    position_horizontale = 10
    position_verticale = 10
    while True:
        lights()
        sleep(2)
        if strongest_light = 'up':
            servo_verticale(position_verticale + 10)
            position_verticale = position_verticale + 10
        elif strongest_light = 'down':
            servo_verticale(position_verticale - 10)
            position_verticale = position_verticale - 10
        elif strongest_light = 'gauche':
            servo_horizontale(position_horizontale + 10)
            position_horizontale = position_horizontale + 10
        elif strongest_light = 'droite':
            servo_horizontale(position_horizontale - 10)
            position_horizontale = position_horizontale - 10
