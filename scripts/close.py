#!/usr/bin/python

# RubpyxRobot Close Fingers Script
# By: Ryan Brazeal (and the I2C Club)
# Date: Started - Circa 2017


from driver import PWM
import os
import time

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Set frequency to 60 Hz
pwm.setPWMFreq(60)

#Hardware Definition Parameters 
whiteClamp = 0
whiteTwist = 1
blueClamp = 2
blueTwist = 3
yellowClamp = 4
yellowTwist = 5
redClamp = 6
redTwist = 7

#Calibration Parameters
whiteClampClosed = 0
whiteClampOpen = 0
whiteTwistNeutral = 0
whiteTwistCCW = 0
whiteTwistCW = 0
blueClampClosed = 0
blueClampOpen = 0
blueTwistNeutral = 0
blueTwistCCW = 0
blueTwistCW = 0
yellowClampClosed = 0
yellowClampOpen = 0
yellowTwistNeutral = 0
yellowTwistCCW = 0
yellowTwistCW = 0
redClampClosed = 0
redClampOpen = 0
redTwistNeutral = 0
redTwistCCW = 0
redTwistCW = 0

params = []
if os.path.isfile("calibration.txt"):
    with open("calibration.txt",'r') as cal_params:
        for param in cal_params:
            params.append(int(param.strip('\n')))

    if len(params) == 20:
        whiteClampClosed = params[0]
        whiteClampOpen = params[1]
        whiteTwistNeutral = params[2]
        whiteTwistCCW = params[3]
        whiteTwistCW = params[4]
        blueClampClosed = params[5]
        blueClampOpen = params[6]
        blueTwistNeutral = params[7]
        blueTwistCCW = params[8]
        blueTwistCW = params[9]
        yellowClampClosed = params[10]
        yellowClampOpen = params[11]
        yellowTwistNeutral = params[12]
        yellowTwistCCW = params[13]
        yellowTwistCW = params[14]
        redClampClosed = params[15]
        redClampOpen = params[16]
        redTwistNeutral = params[17]
        redTwistCCW = params[18]
        redTwistCW = params[19]
        
        pwm.setPWM(whiteClamp,0,whiteClampClosed)
        time.sleep(0.35)
        pwm.setPWM(blueClamp,0,blueClampClosed)
        time.sleep(0.35)
        pwm.setPWM(yellowClamp,0,yellowClampClosed)
        time.sleep(0.35)
        pwm.setPWM(redClamp,0,redClampClosed)
        time.sleep(0.35)
        
else:
    print("\rMissing Calibration File, run calibrate.py first")
    
pwm.softwareReset()
