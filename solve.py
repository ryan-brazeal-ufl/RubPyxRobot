#!/usr/bin/python

# RubpyxRobot Solve the Rubik's Cube and run the machine script
# By: Ryan Brazeal (and the I2C Club)
# Date: Started - Circa 2017

from driver import PWM
import time
import sys
import os

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
foundCalibration = False

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
        foundCalibration = True


def whiteClosed():
   pwm.setPWM(whiteClamp,0,whiteClampClosed-25)
   time.sleep(0.35)
   pwm.setPWM(whiteClamp,0,whiteClampClosed)


def blueClosed():
   pwm.setPWM(blueClamp,0,blueClampClosed-25)
   time.sleep(0.35)
   pwm.setPWM(blueClamp,0,blueClampClosed)


def yellowClosed():
   pwm.setPWM(yellowClamp,0,yellowClampClosed-25)
   time.sleep(0.35)
   pwm.setPWM(yellowClamp,0,yellowClampClosed)


def redClosed():
   pwm.setPWM(redClamp,0,redClampClosed-25)
   time.sleep(0.35)
   pwm.setPWM(redClamp,0,redClampClosed)


def whiteOpen():
   pwm.setPWM(whiteClamp,0,whiteClampOpen+25)
   time.sleep(0.1)
   pwm.setPWM(whiteClamp,0,whiteClampOpen)
   time.sleep(0.35)
   pwm.setPWM(whiteClamp,0,whiteClampOpen+25)
   time.sleep(0.1)
   pwm.setPWM(whiteClamp,0,whiteClampOpen)


def blueOpen():
   pwm.setPWM(blueClamp,0,blueClampOpen+25)
   time.sleep(0.1)
   pwm.setPWM(blueClamp,0,blueClampOpen)
   time.sleep(0.35)
   pwm.setPWM(blueClamp,0,blueClampOpen+25)
   time.sleep(0.1)
   pwm.setPWM(blueClamp,0,blueClampOpen)


def yellowOpen():
   pwm.setPWM(yellowClamp,0,yellowClampOpen+25)
   time.sleep(0.1)
   pwm.setPWM(yellowClamp,0,yellowClampOpen)
   time.sleep(0.35)
   pwm.setPWM(yellowClamp,0,yellowClampOpen+25)
   time.sleep(0.1)
   pwm.setPWM(yellowClamp,0,yellowClampOpen)


def redOpen():
   pwm.setPWM(redClamp,0,redClampOpen+25)
   time.sleep(0.1)
   pwm.setPWM(redClamp,0,redClampOpen)
   time.sleep(0.35)
   pwm.setPWM(redClamp,0,redClampOpen+25)
   time.sleep(0.1)
   pwm.setPWM(redClamp,0,redClampOpen)


def slowGrab():
   for i in range(whiteClampOpen,whiteClampClosed,-1):
      pwm.setPWM(whiteClamp,0,i)
      time.sleep(0.005)

   for i in range(yellowClampOpen,yellowClampClosed,-1):
      pwm.setPWM(yellowClamp,0,i)
      time.sleep(0.005)

   for i in range(blueClampOpen,blueClampClosed,-1):
      pwm.setPWM(blueClamp,0,i)
      time.sleep(0.005)

   for i in range(redClampOpen,redClampClosed,-1):
      pwm.setPWM(redClamp,0,i)
      time.sleep(0.005)


def allOpen():
   
   whiteDiff = whiteClampOpen - whiteClampClosed
   blueDiff = blueClampOpen - blueClampClosed
   yellowDiff = yellowClampOpen - yellowClampClosed
   redDiff = redClampOpen - redClampClosed

   whiteInterval = whiteDiff // 20
   blueInterval = blueDiff // 20
   yellowInterval = yellowDiff // 20
   redInterval = redDiff // 20

   for i in range(1,20):
      pwm.setPWM(whiteClamp,0,whiteClampClosed + whiteInterval * i)
      pwm.setPWM(blueClamp,0,blueClampClosed + blueInterval * i)
      pwm.setPWM(yellowClamp,0,yellowClampClosed + yellowInterval * i)
      pwm.setPWM(redClamp,0,redClampClosed + redInterval * i)
      time.sleep(0.002)


def whiteYellowOpen():

   whiteDiff = whiteClampOpen - whiteClampClosed
   yellowDiff = yellowClampOpen - yellowClampClosed

   whiteInterval = whiteDiff // 20
   yellowInterval = yellowDiff // 20

   for i in range(1,20):
      pwm.setPWM(whiteClamp,0,whiteClampClosed + whiteInterval * i)
      pwm.setPWM(yellowClamp,0,yellowClampClosed + yellowInterval * i)
      # time.sleep(0.002)


def blueRedOpen():
   
   blueDiff = blueClampOpen - blueClampClosed
   redDiff = redClampOpen - redClampClosed

   blueInterval = blueDiff // 20
   redInterval = redDiff // 20

   for i in range(1,20):
      pwm.setPWM(blueClamp,0,blueClampClosed + blueInterval * i)
      pwm.setPWM(redClamp,0,redClampClosed + redInterval * i)
      # time.sleep(0.002)


def whiteYellowOpenAllTheWay():
    
   whiteDiff = whiteClampOpen - whiteClampClosed
   yellowDiff = yellowClampOpen - yellowClampClosed

   whiteInterval = whiteDiff // 20
   yellowInterval = yellowDiff // 20

   for i in range(1,20):
      pwm.setPWM(whiteClamp,0,whiteClampClosed + whiteInterval * i)
      pwm.setPWM(yellowClamp,0,yellowClampClosed + yellowInterval * i)
      # time.sleep(0.002)


def blueRedOpenAllTheWay():
    
   blueDiff = blueClampOpen - blueClampClosed
   redDiff = redClampOpen - redClampClosed

   blueInterval = blueDiff // 20
   redInterval = redDiff // 20

   for i in range(1,20):
      pwm.setPWM(blueClamp,0,blueClampClosed + blueInterval * i)
      pwm.setPWM(redClamp,0,redClampClosed + redInterval * i)
      # time.sleep(0.002)


def whiteYellowClosed():
   lowest = 4096
   highest = -1

   if whiteClampClosed < lowest:
      lowest = whiteClampClosed
   if yellowClampClosed < lowest:
      lowest = yellowClampClosed

   if whiteClampOpen > highest:
      highest = whiteClampOpen
   if yellowClampOpen > highest:
      highest = yellowClampOpen

   for i in range(highest-200,lowest,-5):
      pwm.setPWM(whiteClamp,0,i)
      pwm.setPWM(yellowClamp,0,i)
   whiteClosed()
   yellowClosed()


def blueRedClosed():
   lowest = 4096
   highest = -1

   if blueClampClosed < lowest:
      lowest = blueClampClosed
   if redClampClosed < lowest:
      lowest = redClampClosed

   if blueClampOpen > highest:
      highest = blueClampOpen
   if redClampOpen > highest:
      highest = redClampOpen

   for i in range(highest-200,lowest,-5):
      pwm.setPWM(blueClamp,0,i)
      pwm.setPWM(redClamp,0,i)
   blueClosed()
   redClosed()


def whiteCCW():
   newClamp = whiteClampClosed + 20
   pwm.setPWM(whiteTwist,0,whiteTwistCCW)
   time.sleep(0.5)
   for i in range(whiteTwistCCW+24,whiteTwistCCW+124,2):
      pwm.setPWM(whiteClamp,0,newClamp)
      time.sleep(0.005)
      newClamp += 3
      pwm.setPWM(whiteTwist,0,i)
      time.sleep(0.005)
   pwm.setPWM(whiteTwist,0,whiteTwistNeutral)
   whiteClosed()
   pwm.setPWM(whiteTwist,0,whiteTwistNeutral-20)
   time.sleep(0.1)
   pwm.setPWM(whiteClamp,0,whiteClampClosed+20)
   time.sleep(0.1)
   pwm.setPWM(whiteTwist,0,whiteTwistNeutral)
   time.sleep(0.1)
   whiteClosed()


def whiteCW():
   newClamp = whiteClampClosed + 20
   pwm.setPWM(whiteTwist,0,whiteTwistCW)
   time.sleep(0.5)
   for i in range(whiteTwistCW-24,whiteTwistCW-124,-2):
      pwm.setPWM(whiteClamp,0,newClamp)
      time.sleep(0.005)
      newClamp += 3
      pwm.setPWM(whiteTwist,0,i)
      time.sleep(0.005)
   pwm.setPWM(whiteTwist,0,whiteTwistNeutral)
   whiteClosed()
   pwm.setPWM(whiteTwist,0,whiteTwistNeutral+12)
   time.sleep(0.1)
   pwm.setPWM(whiteClamp,0,whiteClampClosed+20)
   time.sleep(0.1)
   pwm.setPWM(whiteTwist,0,whiteTwistNeutral)
   time.sleep(0.1)
   whiteClosed()


def blueCCW():
   newClamp = blueClampClosed + 20
   pwm.setPWM(blueTwist,0,blueTwistCCW)
   time.sleep(0.5)
   for i in range(blueTwistCCW+24,blueTwistCCW+124,2):
      pwm.setPWM(blueClamp,0,newClamp)
      time.sleep(0.005)
      newClamp += 3
      pwm.setPWM(blueTwist,0,i)
      time.sleep(0.005)
   pwm.setPWM(blueTwist,0,blueTwistNeutral)
   blueClosed()
   pwm.setPWM(blueTwist,0,blueTwistNeutral-16)
   time.sleep(0.1)
   pwm.setPWM(blueClamp,0,blueClampClosed+20)
   time.sleep(0.1)
   pwm.setPWM(blueTwist,0,blueTwistNeutral)
   time.sleep(0.1)
   blueClosed()


def blueCW():
   newClamp = blueClampClosed + 20
   pwm.setPWM(blueTwist,0,blueTwistCW)
   time.sleep(0.5)
   for i in range(blueTwistCW-24,blueTwistCW-124,-2):
      pwm.setPWM(blueClamp,0,newClamp)
      time.sleep(0.005)
      newClamp += 3
      pwm.setPWM(blueTwist,0,i)
      time.sleep(0.005)
   pwm.setPWM(blueTwist,0,blueTwistNeutral)
   blueClosed()
   pwm.setPWM(blueTwist,0,blueTwistNeutral+16)
   time.sleep(0.1)
   pwm.setPWM(blueClamp,0,blueClampClosed+20)
   time.sleep(0.1)
   pwm.setPWM(blueTwist,0,blueTwistNeutral)
   time.sleep(0.1)
   blueClosed()


def yellowCCW():
   newClamp = yellowClampClosed + 20
   pwm.setPWM(yellowTwist,0,yellowTwistCCW)
   time.sleep(0.5)
   for i in range(yellowTwistCCW+24,yellowTwistCCW+124,2):
      pwm.setPWM(yellowClamp,0,newClamp)
      time.sleep(0.005)
      newClamp += 3
      pwm.setPWM(yellowTwist,0,i)
      time.sleep(0.005)
   pwm.setPWM(yellowTwist,0,yellowTwistNeutral)
   yellowClosed()
   pwm.setPWM(yellowTwist,0,yellowTwistNeutral-20)
   time.sleep(0.1)
   pwm.setPWM(yellowClamp,0,yellowClampClosed+20)
   time.sleep(0.1)
   pwm.setPWM(yellowTwist,0,yellowTwistNeutral)
   time.sleep(0.1)
   yellowClosed()


def yellowCW():
   newClamp = yellowClampClosed + 20
   pwm.setPWM(yellowTwist,0,yellowTwistCW)
   time.sleep(0.5)
   for i in range(yellowTwistCW-24,yellowTwistCW-124,-2):
      pwm.setPWM(yellowClamp,0,newClamp)
      time.sleep(0.005)
      newClamp += 3
      pwm.setPWM(yellowTwist,0,i)
      time.sleep(0.005)
   pwm.setPWM(yellowTwist,0,yellowTwistNeutral)
   yellowClosed()
   pwm.setPWM(yellowTwist,0,yellowTwistNeutral+12)
   time.sleep(0.1)
   pwm.setPWM(yellowClamp,0,yellowClampClosed+20)
   time.sleep(0.1)
   pwm.setPWM(yellowTwist,0,yellowTwistNeutral)
   time.sleep(0.1)
   yellowClosed()


def redCCW():
   newClamp = redClampClosed + 20
   pwm.setPWM(redTwist,0,redTwistCCW)
   time.sleep(0.5)
   for i in range(redTwistCCW+24,redTwistCCW+124,2):
      pwm.setPWM(redClamp,0,newClamp)
      time.sleep(0.005)
      newClamp += 3
      pwm.setPWM(redTwist,0,i)
      time.sleep(0.005)
   pwm.setPWM(redTwist,0,redTwistNeutral)
   redClosed()
   pwm.setPWM(redTwist,0,redTwistNeutral-16)
   time.sleep(0.1)
   pwm.setPWM(redClamp,0,redClampClosed+20)
   time.sleep(0.1)
   pwm.setPWM(redTwist,0,redTwistNeutral)
   time.sleep(0.1)
   redClosed()


def redCW():
   newClamp = redClampClosed + 20
   pwm.setPWM(redTwist,0,redTwistCW)
   time.sleep(0.5)
   for i in range(redTwistCW-24,redTwistCW-124,-2):
      pwm.setPWM(redClamp,0,newClamp)
      time.sleep(0.005)
      newClamp += 3
      pwm.setPWM(redTwist,0,i)
      time.sleep(0.005)
   pwm.setPWM(redTwist,0,redTwistNeutral)
   redClosed()
   pwm.setPWM(redTwist,0,redTwistNeutral+16)
   time.sleep(0.1)
   pwm.setPWM(redClamp,0,redClampClosed+20)
   time.sleep(0.1)
   pwm.setPWM(redTwist,0,redTwistNeutral)
   time.sleep(0.1)
   redClosed()


def blueCCWredCW():
   whiteYellowOpen()
   time.sleep(0.2)
   newClampB = blueClampClosed + 20
   newClampR = redClampClosed + 20
   for i in range(0,250,2):
      if blueTwistNeutral-i >= blueTwistCCW-5:
         pwm.setPWM(blueTwist,0,blueTwistNeutral-i)
      if redTwistNeutral+i <= redTwistCW+5:
         pwm.setPWM(redTwist,0,redTwistNeutral+i)
   time.sleep(0.1)
   whiteYellowClosed()
   time.sleep(0.1)
   for i in range(0,100,2):
      pwm.setPWM(blueClamp,0,newClampB)
      pwm.setPWM(redClamp,0,newClampR)
      time.sleep(0.005)
      newClampB += 3
      newClampR += 3
      pwm.setPWM(blueTwist,0,blueTwistCCW+24+i)
      pwm.setPWM(redTwist,0,redTwistCW-24-i)
      time.sleep(0.005)
   pwm.setPWM(blueTwist,0,blueTwistNeutral)
   pwm.setPWM(redTwist,0,redTwistNeutral)
   blueClosed()
   redClosed()
   pwm.setPWM(redTwist,0,redTwistNeutral+16)
   pwm.setPWM(blueTwist,0,blueTwistNeutral-16)
   time.sleep(0.1)
   pwm.setPWM(redClamp,0,redClampClosed+20)
   pwm.setPWM(blueClamp,0,blueClampClosed+20)
   time.sleep(0.1)
   pwm.setPWM(redTwist,0,redTwistNeutral)
   pwm.setPWM(blueTwist,0,blueTwistNeutral)
   time.sleep(0.1)
   blueClosed()
   redClosed()


def blueCWredCCW():
   whiteYellowOpen()
   time.sleep(0.2)
   newClampB = blueClampClosed + 20
   newClampR = redClampClosed + 20
   for i in range(0,250,2):
      if blueTwistNeutral+i <= blueTwistCW+5:
         pwm.setPWM(blueTwist,0,blueTwistNeutral+i)
      if redTwistNeutral-i >= redTwistCCW-5:
         pwm.setPWM(redTwist,0,redTwistNeutral-i)
   time.sleep(0.1)
   whiteYellowClosed()
   time.sleep(0.1)
   for i in range(0,100,2):
      pwm.setPWM(blueClamp,0,newClampB)
      pwm.setPWM(redClamp,0,newClampR)
      time.sleep(0.005)
      newClampB += 3
      newClampR += 3
      pwm.setPWM(blueTwist,0,blueTwistCW-24-i)
      pwm.setPWM(redTwist,0,redTwistCCW+24+i)
      time.sleep(0.005)
   pwm.setPWM(blueTwist,0,blueTwistNeutral)
   pwm.setPWM(redTwist,0,redTwistNeutral)
   blueClosed()
   redClosed()
   pwm.setPWM(redTwist,0,redTwistNeutral-16)
   pwm.setPWM(blueTwist,0,blueTwistNeutral+16)
   time.sleep(0.1)
   pwm.setPWM(redClamp,0,redClampClosed+20)
   pwm.setPWM(blueClamp,0,blueClampClosed+20)
   time.sleep(0.1)
   pwm.setPWM(redTwist,0,redTwistNeutral)
   pwm.setPWM(blueTwist,0,blueTwistNeutral)
   time.sleep(0.1)
   blueClosed()
   redClosed()


def whiteCCWyellowCW():
   blueRedOpen()
   time.sleep(0.2)
   newClampW = whiteClampClosed + 20
   newClampY = yellowClampClosed + 20
   for i in range(0,250,2):
      if whiteTwistNeutral-i >= whiteTwistCCW-5:
         pwm.setPWM(whiteTwist,0,whiteTwistNeutral-i)
      if yellowTwistNeutral+i <= yellowTwistCW+5:
         pwm.setPWM(yellowTwist,0,yellowTwistNeutral+i)
   time.sleep(0.1)
   blueRedClosed()
   time.sleep(0.1)
   for i in range(0,100,2):
      pwm.setPWM(whiteClamp,0,newClampW)
      pwm.setPWM(yellowClamp,0,newClampY)
      time.sleep(0.005)
      newClampW += 3
      newClampY += 3
      pwm.setPWM(whiteTwist,0,whiteTwistCCW+24+i)
      pwm.setPWM(yellowTwist,0,yellowTwistCW-24-i)
      time.sleep(0.005)
   pwm.setPWM(whiteTwist,0,whiteTwistNeutral)
   pwm.setPWM(yellowTwist,0,yellowTwistNeutral)
   whiteClosed()
   yellowClosed()
   pwm.setPWM(yellowTwist,0,yellowTwistNeutral+12)
   pwm.setPWM(whiteTwist,0,whiteTwistNeutral-20)
   time.sleep(0.1)
   pwm.setPWM(yellowClamp,0,yellowClampClosed+20)
   pwm.setPWM(whiteClamp,0,whiteClampClosed+20)
   time.sleep(0.1)
   pwm.setPWM(yellowTwist,0,yellowTwistNeutral)
   pwm.setPWM(whiteTwist,0,whiteTwistNeutral)
   time.sleep(0.1)
   whiteClosed()
   yellowClosed()


def whiteCWyellowCCW():
   blueRedOpen()
   time.sleep(0.2)
   newClampW = whiteClampClosed + 20
   newClampY = yellowClampClosed + 20
   for i in range(0,250,2):
      if whiteTwistNeutral+i <= whiteTwistCW+5:
         pwm.setPWM(whiteTwist,0,whiteTwistNeutral+i)
      if yellowTwistNeutral-i >= yellowTwistCCW-5:
         pwm.setPWM(yellowTwist,0,yellowTwistNeutral-i)
   time.sleep(0.1)
   blueRedClosed()
   time.sleep(0.1)
   for i in range(0,100,2):
      pwm.setPWM(whiteClamp,0,newClampW)
      pwm.setPWM(yellowClamp,0,newClampY)
      time.sleep(0.005)
      newClampW += 3
      newClampY += 3
      pwm.setPWM(whiteTwist,0,whiteTwistCW-24-i)
      pwm.setPWM(yellowTwist,0,yellowTwistCCW+24+i)
      time.sleep(0.005)
   pwm.setPWM(whiteTwist,0,whiteTwistNeutral)
   pwm.setPWM(yellowTwist,0,yellowTwistNeutral)
   whiteClosed()
   yellowClosed()
   pwm.setPWM(yellowTwist,0,yellowTwistNeutral-20)
   pwm.setPWM(whiteTwist,0,whiteTwistNeutral+12)
   time.sleep(0.1)
   pwm.setPWM(yellowClamp,0,yellowClampClosed+20)
   pwm.setPWM(whiteClamp,0,whiteClampClosed+20)
   time.sleep(0.1)
   pwm.setPWM(yellowTwist,0,yellowTwistNeutral)
   pwm.setPWM(whiteTwist,0,whiteTwistNeutral)
   time.sleep(0.1)
   whiteClosed()
   yellowClosed()


def Fplus():
   whiteCW()
   time.sleep(0.05)


def Fminus():
   whiteCCW()
   time.sleep(0.05)


def Rplus():
   redCW()
   time.sleep(0.05)


def Rminus():
   redCCW()
   time.sleep(0.05)


def Kplus():
   yellowCW()
   time.sleep(0.05)


def Kminus():
   yellowCCW()
   time.sleep(0.05)


def Lplus():
   blueCW()
   time.sleep(0.05)


def Lminus():
   blueCCW()
   time.sleep(0.05)


def Tplus():
   blueCWredCCW()
   time.sleep(0.05)
   whiteCW()
   time.sleep(0.05)


def Tminus():
   blueCWredCCW()
   time.sleep(0.05)
   whiteCCW()
   time.sleep(0.05)


def Bplus():
   blueCWredCCW()
   time.sleep(0.05)
   yellowCW()
   time.sleep(0.05)


def Bminus():
   blueCWredCCW()
   time.sleep(0.05)
   yellowCCW()
   time.sleep(0.05)


def getStartingColours():
   #NOTE: All pictures will be taken with the cube face in the correct orientation w.r.t the top of the image

   #take picture = Bottom Layer middle and corners
   whiteYellowOpenAllTheWay()
   time.sleep(1)
   #take picture = Bottom layer top/bottom edges
   whiteYellowClosed()
   time.sleep(1)
   blueRedOpenAllTheWay()
   time.sleep(1)
   #take picture = Bottom layer side edges
   blueRedClosed()
   time.sleep(1)

   blueCWredCCW()
   #take picture = Front Layer middle and corners
   whiteYellowOpenAllTheWay()
   time.sleep(1)
   #take picture = Front layer top/bottom edges
   whiteYellowClosed()
   time.sleep(1)
   blueRedOpenAllTheWay()
   time.sleep(1)
   #take picture = Front layer side edges
   blueRedClosed()
   time.sleep(1)

   whiteCWyellowCCW()
   #take picture = Left Layer middle and corners
   whiteYellowOpenAllTheWay()
   time.sleep(1)
   #take picture = Left layer top/bottom edges
   whiteYellowClosed()
   time.sleep(1)
   blueRedOpenAllTheWay()
   time.sleep(1)
   #take picture = Left layer side edges
   blueRedClosed()
   time.sleep(1)

   whiteCWyellowCCW()
   #take picture = Back Layer middle and corners
   whiteYellowOpenAllTheWay()
   time.sleep(1)
   #take picture = Back layer top/bottom edges
   whiteYellowClosed()
   time.sleep(1)
   blueRedOpenAllTheWay()
   time.sleep(1)
   #take picture = Back layer side edges
   blueRedClosed()
   time.sleep(1)

   whiteCWyellowCCW()
   #take picture = Right Layer middle and corners
   whiteYellowOpenAllTheWay()
   time.sleep(1)
   #take picture = Right layer top/bottom edges
   whiteYellowClosed()
   time.sleep(1)
   blueRedOpenAllTheWay()
   time.sleep(1)
   #take picture = Right layer side edges
   blueRedClosed()
   time.sleep(1)

   whiteCWyellowCCW()
   blueCWredCCW()
   #take picture = Top Layer middle and corners
   whiteYellowOpenAllTheWay()
   time.sleep(1)
   #take picture = Top layer top/bottom edges
   whiteYellowClosed()
   time.sleep(1)
   blueRedOpenAllTheWay()
   time.sleep(1)
   #take picture = Top layer side edges
   blueRedClosed()
   time.sleep(1)


#Close arms then set neutral twist positions and then open arms
def initialize():
   whiteClosed()
   time.sleep(0.25)
   blueClosed()
   time.sleep(0.25)
   yellowClosed()
   time.sleep(0.25)
   redClosed()
   time.sleep(0.25)
   pwm.setPWM(whiteTwist,0,whiteTwistNeutral)
   time.sleep(0.25)
   pwm.setPWM(blueTwist,0,blueTwistNeutral)
   time.sleep(0.25)
   pwm.setPWM(yellowTwist,0,yellowTwistNeutral)
   time.sleep(0.25)
   pwm.setPWM(redTwist,0,redTwistNeutral)
   time.sleep(0.25)
   redOpen()
   time.sleep(0.25)
   yellowOpen()
   time.sleep(0.25)
   blueOpen()
   time.sleep(0.25)
   whiteOpen()
   time.sleep(0.25)


############### RUBIK'S CUBE BEGINEER SOLUTION #################

#cube faces input (top left = 0, top centre = 1, top right = 2 ...
#... middle left = 3, middle centre = 4, middle right = 5 ...
#... bottom left = 6, bottom centre = 7, bottom right = 8)

#Top face orientation is arbitrary (free selection)
#Front face orientation follows that Front0 adjoins Top6
#Right face orientation follows that Right0 adjoins Front2
#Left face orientation follows that Left2 adjoins Front0
#Back face orientation follows that Back0 adjoins Right2
#Bottom face orientation follows that Bottom0 adjoins Front6

w = 'w'
g = 'g'
r = 'r'
b = 'b'
o = 'o'
y = 'y'

Top_Edges_Complete = 0

Solved_Cube = ((w,w,w,w,w,w,w,w,w),(b,b,b,b,b,b,b,b,b),(o,o,o,o,o,o,o,o,o),(g,g,g,g,g,g,g,g,g),(r,r,r,r,r,r,r,r,r),(y,y,y,y,y,y,y,y,y))
Cube = Solved_Cube

Solution_Sequence = []


def check_input_count():
    solution = True
    if len(Cube[0]) != 9 or len(Cube[1]) != 9 or len(Cube[2]) != 9 or len(Cube[3]) != 9 or len(Cube[4]) != 9 or len(Cube[5]) != 9:
        solution = False

    w_count = 0
    g_count = 0
    r_count = 0
    b_count = 0
    o_count = 0
    y_count = 0
    
    for i in range(0,6):
        for j in range(0,9):
            if Cube[i][j] == 'w':
                w_count += 1
            if Cube[i][j] == 'g':
                g_count += 1
            if Cube[i][j] == 'r':
                r_count += 1
            if Cube[i][j] == 'b':
                b_count += 1
            if Cube[i][j] == 'o':
                o_count += 1
            if Cube[i][j] == 'y':
                y_count += 1

    if w_count != 9 or g_count != 9 or r_count != 9 or b_count != 9 or o_count != 9 or y_count != 9:
        solution = False
        print("White " + str(w_count) + " Green " + str(g_count) + " Red " + str(r_count) + " Blue " + str(b_count) + " Orange " + str(o_count) + " Yellow " + str(y_count))

    return solution

#prints cube faces to screen
def print_cube(indivCube):
    print "Top"
    print indivCube[0][0] + " " + indivCube[0][1] + " " + indivCube[0][2]
    print indivCube[0][3] + " " + indivCube[0][4] + " " + indivCube[0][5]
    print indivCube[0][6] + " " + indivCube[0][7] + " " + indivCube[0][8]
    print ""
    print "Front"
    print indivCube[1][0] + " " + indivCube[1][1] + " " + indivCube[1][2]
    print indivCube[1][3] + " " + indivCube[1][4] + " " + indivCube[1][5]
    print indivCube[1][6] + " " + indivCube[1][7] + " " + indivCube[1][8]
    print ""
    print "Right"
    print indivCube[2][0] + " " + indivCube[2][1] + " " + indivCube[2][2]
    print indivCube[2][3] + " " + indivCube[2][4] + " " + indivCube[2][5]
    print indivCube[2][6] + " " + indivCube[2][7] + " " + indivCube[2][8]
    print ""
    print "Back"
    print indivCube[3][0] + " " + indivCube[3][1] + " " + indivCube[3][2]
    print indivCube[3][3] + " " + indivCube[3][4] + " " + indivCube[3][5]
    print indivCube[3][6] + " " + indivCube[3][7] + " " + indivCube[3][8]
    print ""
    print "Left"
    print indivCube[4][0] + " " + indivCube[4][1] + " " + indivCube[4][2]
    print indivCube[4][3] + " " + indivCube[4][4] + " " + indivCube[4][5]
    print indivCube[4][6] + " " + indivCube[4][7] + " " + indivCube[4][8]
    print ""
    print "Bottom"
    print indivCube[5][0] + " " + indivCube[5][1] + " " + indivCube[5][2]
    print indivCube[5][3] + " " + indivCube[5][4] + " " + indivCube[5][5]
    print indivCube[5][6] + " " + indivCube[5][7] + " " + indivCube[5][8]
    print "--------------------------------"


#writes cube faces to LOG file
def write_cube(fileObj, indivCube):
    fileObj.write( "Top" + "\n")
    fileObj.write( indivCube[0][0] + " " + indivCube[0][1] + " " + indivCube[0][2] + "\n")
    fileObj.write( indivCube[0][3] + " " + indivCube[0][4] + " " + indivCube[0][5] + "\n")
    fileObj.write( indivCube[0][6] + " " + indivCube[0][7] + " " + indivCube[0][8] + "\n")
    fileObj.write( "\n")
    fileObj.write( "Front" + "\n")
    fileObj.write( indivCube[1][0] + " " + indivCube[1][1] + " " + indivCube[1][2] + "\n")
    fileObj.write( indivCube[1][3] + " " + indivCube[1][4] + " " + indivCube[1][5] + "\n")
    fileObj.write( indivCube[1][6] + " " + indivCube[1][7] + " " + indivCube[1][8] + "\n")
    fileObj.write( "\n")
    fileObj.write( "Right" + "\n")
    fileObj.write( indivCube[2][0] + " " + indivCube[2][1] + " " + indivCube[2][2] + "\n")
    fileObj.write( indivCube[2][3] + " " + indivCube[2][4] + " " + indivCube[2][5] + "\n")
    fileObj.write( indivCube[2][6] + " " + indivCube[2][7] + " " + indivCube[2][8] + "\n")
    fileObj.write( "\n")
    fileObj.write( "Back" + "\n")
    fileObj.write( indivCube[3][0] + " " + indivCube[3][1] + " " + indivCube[3][2] + "\n")
    fileObj.write( indivCube[3][3] + " " + indivCube[3][4] + " " + indivCube[3][5] + "\n")
    fileObj.write( indivCube[3][6] + " " + indivCube[3][7] + " " + indivCube[3][8] + "\n")
    fileObj.write( "\n")
    fileObj.write( "Left" + "\n")
    fileObj.write( indivCube[4][0] + " " + indivCube[4][1] + " " + indivCube[4][2] + "\n")
    fileObj.write( indivCube[4][3] + " " + indivCube[4][4] + " " + indivCube[4][5] + "\n")
    fileObj.write( indivCube[4][6] + " " + indivCube[4][7] + " " + indivCube[4][8] + "\n")
    fileObj.write( "\n")
    fileObj.write( "Bottom" + "\n")
    fileObj.write( indivCube[5][0] + " " + indivCube[5][1] + " " + indivCube[5][2] + "\n")
    fileObj.write( indivCube[5][3] + " " + indivCube[5][4] + " " + indivCube[5][5] + "\n")
    fileObj.write( indivCube[5][6] + " " + indivCube[5][7] + " " + indivCube[5][8] + "\n")
    fileObj.write( "--------------------------------" + "\n")


def compareCubes(cube1, cube2):
    solution = True
    for i in range(0,6):
        for j in range(0,9):
            if cube1[i][j] != cube2[i][j]:
                solution = False
    return solution


def clean_sequence():
    global Solution_Sequence

    while True:
        cleanIteration = True
        shouldContinue = True
        
        blanksList = []
        for i in range(0,len(Solution_Sequence)):
            if Solution_Sequence[i] == "":
                blanksList.append(i)

        blanksList.reverse()
        for i in range(0,len(blanksList)):
            Solution_Sequence.pop(blanksList[i])

        while shouldContinue:
            shouldContinue = False
            popList = []
            counter = 0
            while counter < len(Solution_Sequence) - 1:
                turn1 = Solution_Sequence[counter]
                turn2 = Solution_Sequence[counter + 1]
                if turn1[:1] == turn2[:1]:
                    if (turn1[1:] == "+" and turn2[1:] == "-") or (turn1[1:] == "-" and turn2[1:] == "+"):
                        popList.append(counter)
                        counter += 2
                        shouldContinue = True
                        cleanIteration = False
                    else:
                        counter += 1
                else:
                    counter += 1

            popList.reverse()
            for i in range(0,len(popList)):
                Solution_Sequence.pop(popList[i])
                Solution_Sequence.pop(popList[i])

        shouldContinue = True

        while shouldContinue:
            shouldContinue = False
            popList = []
            newCommandList = []
            counter = 0
            while counter < len(Solution_Sequence) - 2:
                if Solution_Sequence[counter] == Solution_Sequence[counter + 1] and Solution_Sequence[counter + 1] == Solution_Sequence[counter + 2]:
                    face = Solution_Sequence[counter][:1]
                    rotation = Solution_Sequence[counter][1:]
                    if rotation == "+":
                        rotation = "-"
                    else:
                        rotation = "+"
                    move = face + rotation
                    newCommandList.append(move)
                    popList.append(counter)
                    counter += 3
                    shouldContinue = True
                    cleanIteration = False
                else:
                    counter += 1

            popList.reverse()
            newCommandList.reverse()
            for i in range(0,len(popList)):
                Solution_Sequence.pop(popList[i])
                Solution_Sequence.pop(popList[i])
                Solution_Sequence.pop(popList[i])
                Solution_Sequence.insert(popList[i],newCommandList[i])

        if cleanIteration:
            break


#creates a more efficient sequence for the machine
def trans_sequence():
   global Solution_Sequence
   Machine_Sequence = []
   temp_sequence = []

   position = 0
   for k in range(0,len(Solution_Sequence)):
     if Solution_Sequence[k] != 'X+':
       temp_sequence.append(Solution_Sequence[k])
     else:
       position = k
       break

   for m in range(position+2,len(Solution_Sequence)):
     if Solution_Sequence[m] == 'T+':
       temp_sequence.append('B+')
     elif Solution_Sequence[m] == 'T-':
       temp_sequence.append('B-')
     elif Solution_Sequence[m] == 'B+':
       temp_sequence.append('T+')
     elif Solution_Sequence[m] == 'B-':
       temp_sequence.append('T-')
     elif Solution_Sequence[m] == 'F+':
       temp_sequence.append('K+')
     elif Solution_Sequence[m] == 'F-':
       temp_sequence.append('K-')
     elif Solution_Sequence[m] == 'K+':
       temp_sequence.append('F+')
     elif Solution_Sequence[m] == 'K-':
       temp_sequence.append('F-')
     elif Solution_Sequence[m] != 'X+':
       temp_sequence.append(Solution_Sequence[m])

   #print("intermediate solution")
   #print_sequence(temp_sequence)

   for j in range(0,len(temp_sequence)):
     currentMove = temp_sequence[j]
     Machine_Sequence.append(currentMove)
     if currentMove == 'T+' or currentMove == 'T-' or currentMove == 'B+' or currentMove == 'B-':
       for i in range(j+1, len(temp_sequence)):
          if temp_sequence[i] == 'T+':
             temp_sequence[i] = 'F+'
          elif temp_sequence[i] == 'T-':
             temp_sequence[i] = 'F-'
          elif temp_sequence[i] == 'F+':
             temp_sequence[i] = 'B+'
          elif temp_sequence[i] == 'F-':
             temp_sequence[i] = 'B-'
          elif temp_sequence[i] == 'K+':
             temp_sequence[i] = 'T+'
          elif temp_sequence[i] == 'K-':
             temp_sequence[i] = 'T-'
          elif temp_sequence[i] == 'B+':
             temp_sequence[i] = 'K+'
          elif temp_sequence[i] == 'B-':
             temp_sequence[i] = 'K-'

   return Machine_Sequence


def check_sequence(o_cube):
    global Cube
    Cube = o_cube
    for i in range(0, len(Solution_Sequence)):
        if Solution_Sequence[i] == 'T+':
            T_plus(0)
        elif Solution_Sequence[i] == 'T-':
            T_minus(0)
        elif Solution_Sequence[i] == 'F+':
            F_plus(0)
        elif Solution_Sequence[i] == 'F-':
            F_minus(0)
        elif Solution_Sequence[i] == 'R+':
            R_plus(0)
        elif Solution_Sequence[i] == 'R-':
            R_minus(0)
        elif Solution_Sequence[i] == 'K+':
            K_plus(0)
        elif Solution_Sequence[i] == 'K-':
            K_minus(0)
        elif Solution_Sequence[i] == 'L+':
            L_plus(0)
        elif Solution_Sequence[i] == 'L-':
            L_minus(0)
        elif Solution_Sequence[i] == 'B+':
            B_plus(0)
        elif Solution_Sequence[i] == 'B-':
            B_minus(0)
        elif Solution_Sequence[i] == 'X+':
            X_plus(0)

    result = False
    #check for solved cube
    if Cube[5] == (Cube[5][4],Cube[5][4],Cube[5][4],Cube[5][4],Cube[5][4],Cube[5][4],Cube[5][4],Cube[5][4],Cube[5][4]) and \
        Cube[4] == (Cube[4][4],Cube[4][4],Cube[4][4],Cube[4][4],Cube[4][4],Cube[4][4],Cube[4][4],Cube[4][4],Cube[4][4]) and \
        Cube[3] == (Cube[3][4],Cube[3][4],Cube[3][4],Cube[3][4],Cube[3][4],Cube[3][4],Cube[3][4],Cube[3][4],Cube[3][4]) and \
        Cube[2] == (Cube[2][4],Cube[2][4],Cube[2][4],Cube[2][4],Cube[2][4],Cube[2][4],Cube[2][4],Cube[2][4],Cube[2][4]) and \
        Cube[1] == (Cube[1][4],Cube[1][4],Cube[1][4],Cube[1][4],Cube[1][4],Cube[1][4],Cube[1][4],Cube[1][4],Cube[1][4]) and \
        Cube[0] == (Cube[0][4],Cube[0][4],Cube[0][4],Cube[0][4],Cube[0][4],Cube[0][4],Cube[0][4],Cube[0][4],Cube[0][4]):
        result = True
        
    return result


def print_sequence(seq):
    for i in range(0,len(seq)):
        print str(seq[i])
    print("\n")


def write_sequence(fileObj,seq):
    for i in range(0,len(seq)):
        fileObj.write(str(seq[i] + "\n"))
    fileObj.write("\n")


def scrambleCube():
    global Cube, Solution_Sequence
    Solution_Sequence = []
    Cube = Solved_Cube
    #print_cube(Cube)
    previousNum = 0
    i = 0
    scramble_seq = []
    
    while i < 24:
        turnNum = random.randrange(1,13)

        if turnNum == 1:
            if previousNum != 2:
                T_plus(0)
                scramble_seq.append("T+")
                previousNum = turnNum
                i += 1
        elif turnNum == 2:
            if previousNum != 1:
                T_minus(0)
                scramble_seq.append("T-")
                previousNum = turnNum
                i += 1
        elif turnNum == 3:
            if previousNum != 4:
                F_plus(0)
                scramble_seq.append("F+")
                previousNum = turnNum
                i += 1
        elif turnNum == 4:
            if previousNum != 3:
                F_minus(0)
                scramble_seq.append("F-")
                previousNum = turnNum
                i += 1
        elif turnNum == 5:
            if previousNum != 6:
                R_plus(0)
                scramble_seq.append("R+")
                previousNum = turnNum
                i += 1
        elif turnNum == 6:
            if previousNum != 5:
                R_minus(0)
                scramble_seq.append("R-")
                previousNum = turnNum
                i += 1
        elif turnNum == 7:
            if previousNum != 8:
                K_plus(0)
                scramble_seq.append("K+")
                previousNum = turnNum
                i += 1
        elif turnNum == 8:
            if previousNum != 7:
                K_minus(0)
                scramble_seq.append("K-")
                previousNum = turnNum
                i += 1
        elif turnNum == 9:
            if previousNum != 10:
                L_plus(0)
                scramble_seq.append("L+")
                previousNum = turnNum
                i += 1
        elif turnNum == 10:
            if previousNum != 11:
                L_minus(0)
                scramble_seq.append("L-")
                previousNum = turnNum
                i += 1
        elif turnNum == 11:
            if previousNum != 12:
                B_plus(0)
                scramble_seq.append("B+")
                previousNum = turnNum
                i += 1
        else:
            if previousNum != 11:
                B_minus(0)
                scramble_seq.append("B-")
                previousNum = turnNum
                i += 1
    return scramble_seq


def T_plus(write=1):
    global Cube, Solution_Sequence
    new_Top = (Cube[0][6],Cube[0][3],Cube[0][0],Cube[0][7],Cube[0][4],Cube[0][1],Cube[0][8],Cube[0][5],Cube[0][2])
    new_Front = (Cube[2][0],Cube[2][1],Cube[2][2],Cube[1][3],Cube[1][4],Cube[1][5],Cube[1][6],Cube[1][7],Cube[1][8])
    new_Right = (Cube[3][0],Cube[3][1],Cube[3][2],Cube[2][3],Cube[2][4],Cube[2][5],Cube[2][6],Cube[2][7],Cube[2][8])
    new_Back = (Cube[4][0],Cube[4][1],Cube[4][2],Cube[3][3],Cube[3][4],Cube[3][5],Cube[3][6],Cube[3][7],Cube[3][8])
    new_Left = (Cube[1][0],Cube[1][1],Cube[1][2],Cube[4][3],Cube[4][4],Cube[4][5],Cube[4][6],Cube[4][7],Cube[4][8])
    new_Bottom = Cube[5]
    Cube = (new_Top, new_Front, new_Right, new_Back, new_Left, new_Bottom)
    if write == 1:
        Solution_Sequence.append("T+")
   
     
def T_minus(write=1):
    global Cube, Solution_Sequence
    new_Top = (Cube[0][2],Cube[0][5],Cube[0][8],Cube[0][1],Cube[0][4],Cube[0][7],Cube[0][0],Cube[0][3],Cube[0][6])
    new_Front = (Cube[4][0],Cube[4][1],Cube[4][2],Cube[1][3],Cube[1][4],Cube[1][5],Cube[1][6],Cube[1][7],Cube[1][8])
    new_Right = (Cube[1][0],Cube[1][1],Cube[1][2],Cube[2][3],Cube[2][4],Cube[2][5],Cube[2][6],Cube[2][7],Cube[2][8])
    new_Back = (Cube[2][0],Cube[2][1],Cube[2][2],Cube[3][3],Cube[3][4],Cube[3][5],Cube[3][6],Cube[3][7],Cube[3][8])
    new_Left = (Cube[3][0],Cube[3][1],Cube[3][2],Cube[4][3],Cube[4][4],Cube[4][5],Cube[4][6],Cube[4][7],Cube[4][8])
    new_Bottom = Cube[5]
    Cube = (new_Top, new_Front, new_Right, new_Back, new_Left, new_Bottom)
    if write == 1:
        Solution_Sequence.append("T-")
    
    
def F_plus(write=1):
    global Cube, Solution_Sequence
    new_Top = (Cube[0][0],Cube[0][1],Cube[0][2],Cube[0][3],Cube[0][4],Cube[0][5],Cube[4][8],Cube[4][5],Cube[4][2])
    new_Front = (Cube[1][6],Cube[1][3],Cube[1][0],Cube[1][7],Cube[1][4],Cube[1][1],Cube[1][8],Cube[1][5],Cube[1][2])
    new_Right = (Cube[0][6],Cube[2][1],Cube[2][2],Cube[0][7],Cube[2][4],Cube[2][5],Cube[0][8],Cube[2][7],Cube[2][8])
    new_Back = Cube[3]
    new_Left = (Cube[4][0],Cube[4][1],Cube[5][0],Cube[4][3],Cube[4][4],Cube[5][1],Cube[4][6],Cube[4][7],Cube[5][2])
    new_Bottom = (Cube[2][6],Cube[2][3],Cube[2][0],Cube[5][3],Cube[5][4],Cube[5][5],Cube[5][6],Cube[5][7],Cube[5][8])
    Cube = (new_Top, new_Front, new_Right, new_Back, new_Left, new_Bottom)
    if write == 1:
        Solution_Sequence.append("F+")
       
        
def F_minus(write=1):
    global Cube, Solution_Sequence
    new_Top = (Cube[0][0],Cube[0][1],Cube[0][2],Cube[0][3],Cube[0][4],Cube[0][5],Cube[2][0],Cube[2][3],Cube[2][6])
    new_Front = (Cube[1][2],Cube[1][5],Cube[1][8],Cube[1][1],Cube[1][4],Cube[1][7],Cube[1][0],Cube[1][3],Cube[1][6])
    new_Right = (Cube[5][2],Cube[2][1],Cube[2][2],Cube[5][1],Cube[2][4],Cube[2][5],Cube[5][0],Cube[2][7],Cube[2][8])
    new_Back = Cube[3]
    new_Left = (Cube[4][0],Cube[4][1],Cube[0][8],Cube[4][3],Cube[4][4],Cube[0][7],Cube[4][6],Cube[4][7],Cube[0][6])
    new_Bottom = (Cube[4][2],Cube[4][5],Cube[4][8],Cube[5][3],Cube[5][4],Cube[5][5],Cube[5][6],Cube[5][7],Cube[5][8])
    Cube = (new_Top, new_Front, new_Right, new_Back, new_Left, new_Bottom)
    if write == 1:
        Solution_Sequence.append("F-")
      
        
def R_plus(write=1):
    global Cube, Solution_Sequence
    new_Top = (Cube[0][0],Cube[0][1],Cube[1][2],Cube[0][3],Cube[0][4],Cube[1][5],Cube[0][6],Cube[0][7],Cube[1][8])
    new_Front = (Cube[1][0],Cube[1][1],Cube[5][2],Cube[1][3],Cube[1][4],Cube[5][5],Cube[1][6],Cube[1][7],Cube[5][8])
    new_Right = (Cube[2][6],Cube[2][3],Cube[2][0],Cube[2][7],Cube[2][4],Cube[2][1],Cube[2][8],Cube[2][5],Cube[2][2])
    new_Back = (Cube[0][8],Cube[3][1],Cube[3][2],Cube[0][5],Cube[3][4],Cube[3][5],Cube[0][2],Cube[3][7],Cube[3][8])
    new_Left = Cube[4]
    new_Bottom = (Cube[5][0],Cube[5][1],Cube[3][6],Cube[5][3],Cube[5][4],Cube[3][3],Cube[5][6],Cube[5][7],Cube[3][0])
    Cube = (new_Top, new_Front, new_Right, new_Back, new_Left, new_Bottom)
    if write == 1:
        Solution_Sequence.append("R+")
        
        
def R_minus(write=1):
    global Cube, Solution_Sequence
    new_Top = (Cube[0][0],Cube[0][1],Cube[3][6],Cube[0][3],Cube[0][4],Cube[3][3],Cube[0][6],Cube[0][7],Cube[3][0])
    new_Front = (Cube[1][0],Cube[1][1],Cube[0][2],Cube[1][3],Cube[1][4],Cube[0][5],Cube[1][6],Cube[1][7],Cube[0][8])
    new_Right = (Cube[2][2],Cube[2][5],Cube[2][8],Cube[2][1],Cube[2][4],Cube[2][7],Cube[2][0],Cube[2][3],Cube[2][6])
    new_Back = (Cube[5][8],Cube[3][1],Cube[3][2],Cube[5][5],Cube[3][4],Cube[3][5],Cube[5][2],Cube[3][7],Cube[3][8])
    new_Left = Cube[4]
    new_Bottom = (Cube[5][0],Cube[5][1],Cube[1][2],Cube[5][3],Cube[5][4],Cube[1][5],Cube[5][6],Cube[5][7],Cube[1][8])
    Cube = (new_Top, new_Front, new_Right, new_Back, new_Left, new_Bottom)
    if write == 1:
        Solution_Sequence.append("R-")
      
        
def K_plus(write=1):
    global Cube, Solution_Sequence
    new_Top = (Cube[2][2],Cube[2][5],Cube[2][8],Cube[0][3],Cube[0][4],Cube[0][5],Cube[0][6],Cube[0][7],Cube[0][8])
    new_Front = Cube[1]
    new_Right = (Cube[2][0],Cube[2][1],Cube[5][8],Cube[2][3],Cube[2][4],Cube[5][7],Cube[2][6],Cube[2][7],Cube[5][6])
    new_Back = (Cube[3][6],Cube[3][3],Cube[3][0],Cube[3][7],Cube[3][4],Cube[3][1],Cube[3][8],Cube[3][5],Cube[3][2])
    new_Left = (Cube[0][2],Cube[4][1],Cube[4][2],Cube[0][1],Cube[4][4],Cube[4][5],Cube[0][0],Cube[4][7],Cube[4][8])
    new_Bottom = (Cube[5][0],Cube[5][1],Cube[5][2],Cube[5][3],Cube[5][4],Cube[5][5],Cube[4][0],Cube[4][3],Cube[4][6])
    Cube = (new_Top, new_Front, new_Right, new_Back, new_Left, new_Bottom)
    if write == 1:
        Solution_Sequence.append("K+")
      
        
def K_minus(write=1):
    global Cube, Solution_Sequence
    new_Top = (Cube[4][6],Cube[4][3],Cube[4][0],Cube[0][3],Cube[0][4],Cube[0][5],Cube[0][6],Cube[0][7],Cube[0][8])
    new_Front = Cube[1]
    new_Right = (Cube[2][0],Cube[2][1],Cube[0][0],Cube[2][3],Cube[2][4],Cube[0][1],Cube[2][6],Cube[2][7],Cube[0][2])
    new_Back = (Cube[3][2],Cube[3][5],Cube[3][8],Cube[3][1],Cube[3][4],Cube[3][7],Cube[3][0],Cube[3][3],Cube[3][6])
    new_Left = (Cube[5][6],Cube[4][1],Cube[4][2],Cube[5][7],Cube[4][4],Cube[4][5],Cube[5][8],Cube[4][7],Cube[4][8])
    new_Bottom = (Cube[5][0],Cube[5][1],Cube[5][2],Cube[5][3],Cube[5][4],Cube[5][5],Cube[2][8],Cube[2][5],Cube[2][2])
    Cube = (new_Top, new_Front, new_Right, new_Back, new_Left, new_Bottom)
    if write == 1:
        Solution_Sequence.append("K-")
     
        
def L_plus(write=1):
    global Cube, Solution_Sequence
    new_Top = (Cube[3][8],Cube[0][1],Cube[0][2],Cube[3][5],Cube[0][4],Cube[0][5],Cube[3][2],Cube[0][7],Cube[0][8])
    new_Front = (Cube[0][0],Cube[1][1],Cube[1][2],Cube[0][3],Cube[1][4],Cube[1][5],Cube[0][6],Cube[1][7],Cube[1][8])
    new_Right = Cube[2]
    new_Back = (Cube[3][0],Cube[3][1],Cube[5][6],Cube[3][3],Cube[3][4],Cube[5][3],Cube[3][6],Cube[3][7],Cube[5][0])
    new_Left = (Cube[4][6],Cube[4][3],Cube[4][0],Cube[4][7],Cube[4][4],Cube[4][1],Cube[4][8],Cube[4][5],Cube[4][2])
    new_Bottom = (Cube[1][0],Cube[5][1],Cube[5][2],Cube[1][3],Cube[5][4],Cube[5][5],Cube[1][6],Cube[5][7],Cube[5][8])
    Cube = (new_Top, new_Front, new_Right, new_Back, new_Left, new_Bottom)
    if write == 1:
        Solution_Sequence.append("L+")
      
        
def L_minus(write=1):
    global Cube, Solution_Sequence
    new_Top = (Cube[1][0],Cube[0][1],Cube[0][2],Cube[1][3],Cube[0][4],Cube[0][5],Cube[1][6],Cube[0][7],Cube[0][8])
    new_Front = (Cube[5][0],Cube[1][1],Cube[1][2],Cube[5][3],Cube[1][4],Cube[1][5],Cube[5][6],Cube[1][7],Cube[1][8])
    new_Right = Cube[2]
    new_Back = (Cube[3][0],Cube[3][1],Cube[0][6],Cube[3][3],Cube[3][4],Cube[0][3],Cube[3][6],Cube[3][7],Cube[0][0])
    new_Left = (Cube[4][2],Cube[4][5],Cube[4][8],Cube[4][1],Cube[4][4],Cube[4][7],Cube[4][0],Cube[4][3],Cube[4][6])
    new_Bottom = (Cube[3][8],Cube[5][1],Cube[5][2],Cube[3][5],Cube[5][4],Cube[5][5],Cube[3][2],Cube[5][7],Cube[5][8])
    Cube = (new_Top, new_Front, new_Right, new_Back, new_Left, new_Bottom)
    if write == 1:
        Solution_Sequence.append("L-")
      
        
def B_plus(write=1):
    global Cube, Solution_Sequence
    new_Top = Cube[0]
    new_Front = (Cube[1][0],Cube[1][1],Cube[1][2],Cube[1][3],Cube[1][4],Cube[1][5],Cube[4][6],Cube[4][7],Cube[4][8])
    new_Right = (Cube[2][0],Cube[2][1],Cube[2][2],Cube[2][3],Cube[2][4],Cube[2][5],Cube[1][6],Cube[1][7],Cube[1][8])
    new_Back = (Cube[3][0],Cube[3][1],Cube[3][2],Cube[3][3],Cube[3][4],Cube[3][5],Cube[2][6],Cube[2][7],Cube[2][8])
    new_Left = (Cube[4][0],Cube[4][1],Cube[4][2],Cube[4][3],Cube[4][4],Cube[4][5],Cube[3][6],Cube[3][7],Cube[3][8])
    new_Bottom = (Cube[5][6],Cube[5][3],Cube[5][0],Cube[5][7],Cube[5][4],Cube[5][1],Cube[5][8],Cube[5][5],Cube[5][2])
    Cube = (new_Top, new_Front, new_Right, new_Back, new_Left, new_Bottom)
    if write == 1:
        Solution_Sequence.append("B+")
      
        
def B_minus(write=1):
    global Cube, Solution_Sequence
    new_Top = Cube[0]
    new_Front = (Cube[1][0],Cube[1][1],Cube[1][2],Cube[1][3],Cube[1][4],Cube[1][5],Cube[2][6],Cube[2][7],Cube[2][8])
    new_Right = (Cube[2][0],Cube[2][1],Cube[2][2],Cube[2][3],Cube[2][4],Cube[2][5],Cube[3][6],Cube[3][7],Cube[3][8])
    new_Back = (Cube[3][0],Cube[3][1],Cube[3][2],Cube[3][3],Cube[3][4],Cube[3][5],Cube[4][6],Cube[4][7],Cube[4][8])
    new_Left = (Cube[4][0],Cube[4][1],Cube[4][2],Cube[4][3],Cube[4][4],Cube[4][5],Cube[1][6],Cube[1][7],Cube[1][8])
    new_Bottom = (Cube[5][2],Cube[5][5],Cube[5][8],Cube[5][1],Cube[5][4],Cube[5][7],Cube[5][0],Cube[5][3],Cube[5][6])
    Cube = (new_Top, new_Front, new_Right, new_Back, new_Left, new_Bottom)
    if write == 1:
        Solution_Sequence.append("B-")
      
        
# The following cube move rotate the entire cube and follow the right hand rule for rotations within a right handed
# coordinate system with the X axis coming from the centre of the cube through the right face 
def X_plus(write=1):
    global Cube, Solution_Sequence
    new_Top = (Cube[0][0],Cube[3][7],Cube[0][2],Cube[0][3],Cube[3][4],Cube[0][5],Cube[0][6],Cube[3][1],Cube[0][8])
    new_Front = (Cube[1][0],Cube[0][1],Cube[1][2],Cube[1][3],Cube[0][4],Cube[1][5],Cube[1][6],Cube[0][7],Cube[1][8])
    new_Right = Cube[2]
    new_Back = (Cube[3][0],Cube[5][7],Cube[3][2],Cube[3][3],Cube[5][4],Cube[3][5],Cube[3][6],Cube[5][1],Cube[3][8])
    new_Left = Cube[4]
    new_Bottom = (Cube[5][0],Cube[1][1],Cube[5][2],Cube[5][3],Cube[1][4],Cube[5][5],Cube[5][6],Cube[1][7],Cube[5][8])
    Cube = (new_Top, new_Front, new_Right, new_Back, new_Left, new_Bottom)
    R_minus(0)
    L_plus(0)
    if write == 1:
        Solution_Sequence.append("X+")    


def find_edge(colour1, colour2):
#returns edge piece with face of colour1 and position of colour2
    pos = []
    if Cube[0][1] == colour1 and Cube[3][1] == colour2:
        pos.append(0)
        pos.append(1)        
    elif Cube[0][1] == colour2 and Cube[3][1] == colour1:
        pos.append(3)
        pos.append(1)
    elif Cube[0][3] == colour1 and Cube[4][1] == colour2:
        pos.append(0)
        pos.append(3)
    elif Cube[0][3] == colour2 and Cube[4][1] == colour1:
        pos.append(4)
        pos.append(1)
    elif Cube[0][5] == colour1 and Cube[2][1] == colour2:
        pos.append(0)
        pos.append(5)
    elif Cube[0][5] == colour2 and Cube[2][1] == colour1:
        pos.append(2)
        pos.append(1)
    elif Cube[0][7] == colour1 and Cube[1][1] == colour2:
        pos.append(0)
        pos.append(7)
    elif Cube[0][7] == colour2 and Cube[1][1] == colour1:
        pos.append(1)
        pos.append(1)

    elif Cube[5][1] == colour1 and Cube[1][7] == colour2:
        pos.append(5)
        pos.append(1)        
    elif Cube[5][1] == colour2 and Cube[1][7] == colour1:
        pos.append(1)
        pos.append(7)
    elif Cube[5][3] == colour1 and Cube[4][7] == colour2:
        pos.append(5)
        pos.append(3)
    elif Cube[5][3] == colour2 and Cube[4][7] == colour1:
        pos.append(4)
        pos.append(7)
    elif Cube[5][5] == colour1 and Cube[2][7] == colour2:
        pos.append(5)
        pos.append(5)
    elif Cube[5][5] == colour2 and Cube[2][7] == colour1:
        pos.append(2)
        pos.append(7)
    elif Cube[5][7] == colour1 and Cube[3][7] == colour2:
        pos.append(5)
        pos.append(7)
    elif Cube[5][7] == colour2 and Cube[3][7] == colour1:
        pos.append(3)
        pos.append(7)

    elif Cube[1][3] == colour1 and Cube[4][5] == colour2:
        pos.append(1)
        pos.append(3)        
    elif Cube[1][3] == colour2 and Cube[4][5] == colour1:
        pos.append(4)
        pos.append(5)
    elif Cube[2][3] == colour1 and Cube[1][5] == colour2:
        pos.append(2)
        pos.append(3)
    elif Cube[2][3] == colour2 and Cube[1][5] == colour1:
        pos.append(1)
        pos.append(5)
    elif Cube[3][3] == colour1 and Cube[2][5] == colour2:
        pos.append(3)
        pos.append(3)
    elif Cube[3][3] == colour2 and Cube[2][5] == colour1:
        pos.append(2)
        pos.append(5)
    elif Cube[4][3] == colour1 and Cube[3][5] == colour2:
        pos.append(4)
        pos.append(3)
    elif Cube[4][3] == colour2 and Cube[3][5] == colour1:
        pos.append(3)
        pos.append(5)

    else:
        pos.append(-1)
        pos.append(-1)

    return pos


def find_corner(colour1, colour2, colour3):
    pos = []
    
    #Top Face Search
    if Cube[0][0] == colour1 and Cube[3][2] == colour2 and Cube[4][0] == colour3:
        pos.append(0)
        pos.append(0)
    elif Cube[0][0] == colour1 and Cube[3][2] == colour3 and Cube[4][0] == colour2:
        pos.append(0)
        pos.append(0)
    elif Cube[0][2] == colour1 and Cube[2][2] == colour2 and Cube[3][0] == colour3:
        pos.append(0)
        pos.append(2)
    elif Cube[0][2] == colour1 and Cube[2][2] == colour3 and Cube[3][0] == colour2:
        pos.append(0)
        pos.append(2)
    elif Cube[0][6] == colour1 and Cube[4][2] == colour2 and Cube[1][0] == colour3:
        pos.append(0)
        pos.append(6)
    elif Cube[0][6] == colour1 and Cube[4][2] == colour3 and Cube[1][0] == colour2:
        pos.append(0)
        pos.append(6)
    elif Cube[0][8] == colour1 and Cube[1][2] == colour2 and Cube[2][0] == colour3:
        pos.append(0)
        pos.append(8)
    elif Cube[0][8] == colour1 and Cube[1][2] == colour3 and Cube[2][0] == colour2:
        pos.append(0)
        pos.append(8)

    #Front Face Search
    elif Cube[1][0] == colour1 and Cube[0][6] == colour2 and Cube[4][2] == colour3:
        pos.append(1)
        pos.append(0)
    elif Cube[1][0] == colour1 and Cube[0][6] == colour3 and Cube[4][2] == colour2:
        pos.append(1)
        pos.append(0)
    elif Cube[1][2] == colour1 and Cube[0][8] == colour2 and Cube[2][0] == colour3:
        pos.append(1)
        pos.append(2)
    elif Cube[1][2] == colour1 and Cube[0][8] == colour3 and Cube[2][0] == colour2:
        pos.append(1)
        pos.append(2)
    elif Cube[1][6] == colour1 and Cube[5][0] == colour2 and Cube[4][8] == colour3:
        pos.append(1)
        pos.append(6)
    elif Cube[1][6] == colour1 and Cube[5][0] == colour3 and Cube[4][8] == colour2:
        pos.append(1)
        pos.append(6)
    elif Cube[1][8] == colour1 and Cube[5][2] == colour2 and Cube[2][6] == colour3:
        pos.append(1)
        pos.append(8)
    elif Cube[1][8] == colour1 and Cube[5][2] == colour3 and Cube[2][6] == colour2:
        pos.append(1)
        pos.append(8)

    #Right Face Search
    elif Cube[2][0] == colour1 and Cube[0][8] == colour2 and Cube[1][2] == colour3:
        pos.append(2)
        pos.append(0)
    elif Cube[2][0] == colour1 and Cube[0][8] == colour3 and Cube[1][2] == colour2:
        pos.append(2)
        pos.append(0)
    elif Cube[2][2] == colour1 and Cube[0][2] == colour2 and Cube[3][0] == colour3:
        pos.append(2)
        pos.append(2)
    elif Cube[2][2] == colour1 and Cube[0][2] == colour3 and Cube[3][0] == colour2:
        pos.append(2)
        pos.append(2)
    elif Cube[2][6] == colour1 and Cube[1][8] == colour2 and Cube[5][2] == colour3:
        pos.append(2)
        pos.append(6)
    elif Cube[2][6] == colour1 and Cube[1][8] == colour3 and Cube[5][2] == colour2:
        pos.append(2)
        pos.append(6)
    elif Cube[2][8] == colour1 and Cube[3][6] == colour2 and Cube[5][8] == colour3:
        pos.append(2)
        pos.append(8)
    elif Cube[2][8] == colour1 and Cube[3][6] == colour3 and Cube[5][8] == colour2:
        pos.append(2)
        pos.append(8)

    #Back Face Search
    elif Cube[3][0] == colour1 and Cube[0][2] == colour2 and Cube[2][2] == colour3:
        pos.append(3)
        pos.append(0)
    elif Cube[3][0] == colour1 and Cube[0][2] == colour3 and Cube[2][2] == colour2:
        pos.append(3)
        pos.append(0)
    elif Cube[3][2] == colour1 and Cube[0][0] == colour2 and Cube[4][0] == colour3:
        pos.append(3)
        pos.append(2)
    elif Cube[3][2] == colour1 and Cube[0][0] == colour3 and Cube[4][0] == colour2:
        pos.append(3)
        pos.append(2)
    elif Cube[3][6] == colour1 and Cube[2][8] == colour2 and Cube[5][8] == colour3:
        pos.append(3)
        pos.append(6)
    elif Cube[3][6] == colour1 and Cube[2][8] == colour3 and Cube[5][8] == colour2:
        pos.append(3)
        pos.append(6)
    elif Cube[3][8] == colour1 and Cube[4][6] == colour2 and Cube[5][6] == colour3:
        pos.append(3)
        pos.append(8)
    elif Cube[3][8] == colour1 and Cube[4][6] == colour3 and Cube[5][6] == colour2:
        pos.append(3)
        pos.append(8)

    #Left Face Search
    elif Cube[4][0] == colour1 and Cube[0][0] == colour2 and Cube[3][2] == colour3:
        pos.append(4)
        pos.append(0)
    elif Cube[4][0] == colour1 and Cube[0][0] == colour3 and Cube[3][2] == colour2:
        pos.append(4)
        pos.append(0)
    elif Cube[4][2] == colour1 and Cube[0][6] == colour2 and Cube[1][0] == colour3:
        pos.append(4)
        pos.append(2)
    elif Cube[4][2] == colour1 and Cube[0][6] == colour3 and Cube[1][0] == colour2:
        pos.append(4)
        pos.append(2)
    elif Cube[4][6] == colour1 and Cube[3][8] == colour2 and Cube[5][6] == colour3:
        pos.append(4)
        pos.append(6)
    elif Cube[4][6] == colour1 and Cube[3][8] == colour3 and Cube[5][6] == colour2:
        pos.append(4)
        pos.append(6)
    elif Cube[4][8] == colour1 and Cube[1][6] == colour2 and Cube[5][0] == colour3:
        pos.append(4)
        pos.append(8)
    elif Cube[4][8] == colour1 and Cube[1][6] == colour3 and Cube[5][0] == colour2:
        pos.append(4)
        pos.append(8)

    #Bottom Face Search
    elif Cube[5][0] == colour1 and Cube[1][6] == colour2 and Cube[4][8] == colour3:
        pos.append(5)
        pos.append(0)
    elif Cube[5][0] == colour1 and Cube[1][6] == colour3 and Cube[4][8] == colour2:
        pos.append(5)
        pos.append(0)
    elif Cube[5][2] == colour1 and Cube[1][8] == colour2 and Cube[2][6] == colour3:
        pos.append(5)
        pos.append(2)
    elif Cube[5][2] == colour1 and Cube[1][8] == colour3 and Cube[2][6] == colour2:
        pos.append(5)
        pos.append(2)
    elif Cube[5][6] == colour1 and Cube[3][8] == colour2 and Cube[4][6] == colour3:
        pos.append(5)
        pos.append(6)
    elif Cube[5][6] == colour1 and Cube[3][8] == colour3 and Cube[4][6] == colour2:
        pos.append(5)
        pos.append(6)
    elif Cube[5][8] == colour1 and Cube[2][8] == colour2 and Cube[3][6] == colour3:
        pos.append(5)
        pos.append(8)
    elif Cube[5][8] == colour1 and Cube[2][8] == colour3 and Cube[3][6] == colour2:
        pos.append(5)
        pos.append(8)

    return pos


def move_edge_top(pos):
    global Top_Edges_Complete, Solution_Sequence
    
    #Top Face moves
    if pos[0] == 0:
        if Top_Edges_Complete == 0:
            if pos[1] == 1:
                if Cube[3][1] == Cube[4][4]:
                    T_minus()
                elif Cube[3][1] == Cube[2][4]:
                    T_plus()
                elif Cube[3][1] == Cube[1][4]:
                    T_plus()
                    T_plus()
            elif pos[1] == 3:
                if Cube[4][1] == Cube[1][4]:
                    T_minus()
                elif Cube[4][1] == Cube[3][4]:
                    T_plus()
                elif Cube[4][1] == Cube[2][4]:
                    T_plus()
                    T_plus()
            elif pos[1] == 5:
                if Cube[2][1] == Cube[3][4]:
                    T_minus()
                elif Cube[2][1] == Cube[1][4]:
                    T_plus()
                elif Cube[2][1] == Cube[4][4]:
                    T_plus()
                    T_plus()
            else:
                if Cube[1][1] == Cube[2][4]:                    
                    T_minus()
                elif Cube[1][1] == Cube[4][4]:
                    T_plus()
                elif Cube[1][1] == Cube[3][4]:
                    T_plus()
                    T_plus()
            Top_Edges_Complete = 1
        else:
            if pos[1] == 1:
                if Cube[3][1] == Cube[4][4]:
                    K_plus()
                    T_plus()
                    K_minus()
                    T_minus()
                elif Cube[3][1] == Cube[2][4]:
                    K_plus()
                    T_minus()
                    K_minus()
                    T_plus()
                elif Cube[3][1] == Cube[1][4]:
                    K_plus()
                    T_minus()
                    T_minus()
                    K_minus()
                    T_plus()
                    T_plus()
            elif pos[1] == 3:
                if Cube[4][1] == Cube[1][4]:
                    L_plus()
                    T_plus()
                    L_minus()
                    T_minus()
                elif Cube[4][1] == Cube[3][4]:
                    L_plus()
                    T_minus()
                    L_minus()
                    T_plus()
                elif Cube[4][1] == Cube[2][4]:
                    L_plus()
                    T_minus()
                    T_minus()
                    L_minus()
                    T_plus()
                    T_plus()
            elif pos[1] == 5:
                if Cube[2][1] == Cube[3][4]:
                    R_plus()
                    T_plus()
                    R_minus()
                    T_minus()
                elif Cube[2][1] == Cube[1][4]:
                    R_plus()
                    T_minus()
                    R_minus()
                    T_plus()
                elif Cube[2][1] == Cube[4][4]:
                    R_plus()
                    T_minus()
                    T_minus()
                    R_minus()
                    T_plus()
                    T_plus()
            else:
                if Cube[1][1] == Cube[2][4]:
                    F_plus()
                    T_plus()
                    F_minus()
                    T_minus()
                elif Cube[1][1] == Cube[4][4]:
                    F_plus()
                    T_minus()
                    F_minus()
                    T_plus()
                elif Cube[1][1] == Cube[3][4]:
                    F_plus()
                    T_minus()
                    T_minus()
                    F_minus()
                    T_plus()
                    T_plus()
            Top_Edges_Complete += 1
            
    # Front Face moves
    elif pos[0] == 1:
        if Top_Edges_Complete == 0:
            if pos[1] == 1:
                if Cube[0][7] == Cube[1][4]:
                    F_plus()
                    R_plus()
                    T_plus()
                elif Cube[0][7] == Cube[2][4]:
                    F_plus()
                    R_plus()
                elif Cube[0][7] == Cube[3][4]:
                    F_plus()
                    R_plus()
                    T_minus()
                else:
                    F_minus()
                    L_minus()
            elif pos[1] == 3:
                if Cube[4][5] == Cube[1][4]:
                    L_minus()
                    T_minus()
                elif Cube[4][5] == Cube[2][4]:
                    L_minus()
                    T_minus()
                    T_minus()
                elif Cube[4][5] == Cube[3][4]:
                    L_minus()
                    T_plus()
                else:
                    L_minus()
            elif pos[1] == 5:
                if Cube[2][3] == Cube[1][4]:
                    R_plus()
                    T_plus()
                elif Cube[2][3] == Cube[2][4]:
                    R_plus()
                elif Cube[2][3] == Cube[3][4]:
                    R_plus()
                    T_minus()
                else:
                    R_plus()
                    T_plus()
                    T_plus()
            else:
                if Cube[5][1] == Cube[1][4]:
                    F_minus()
                    R_plus()
                    T_plus()
                elif Cube[5][1] == Cube[2][4]:
                    F_minus()
                    R_plus()
                elif Cube[5][1] == Cube[3][4]:
                    F_minus()
                    R_plus()
                    T_minus()
                else:
                    F_plus()
                    L_minus()
                    
            Top_Edges_Complete = 1
        else:
            if pos[1] == 1:
                if Cube[0][7] == Cube[1][4]:
                    F_plus()
                    T_minus()
                    R_plus()
                    T_plus()
                elif Cube[0][7] == Cube[2][4]:
                    F_plus()
                    R_plus()
                elif Cube[0][7] == Cube[3][4]:
                    F_plus()
                    T_plus()
                    R_plus()
                    T_minus()
                else:
                    F_minus()
                    L_minus()
            elif pos[1] == 3:
                if Cube[4][5] == Cube[1][4]:
                    T_plus()
                    L_minus()
                    T_minus()
                elif Cube[4][5] == Cube[2][4]:
                    T_plus()
                    T_plus()
                    L_minus()
                    T_minus()
                    T_minus()
                elif Cube[4][5] == Cube[3][4]:
                    T_minus()
                    L_minus()
                    T_plus()
                else:
                    L_minus()
            elif pos[1] == 5:
                if Cube[2][3] == Cube[1][4]:
                    T_minus()
                    R_plus()
                    T_plus()
                elif Cube[2][3] == Cube[2][4]:
                    R_plus()
                elif Cube[2][3] == Cube[3][4]:
                    T_plus()
                    R_plus()
                    T_minus()
                else:
                    T_minus()
                    T_minus()
                    R_plus()
                    T_plus()
                    T_plus()
            else:
                if Cube[5][1] == Cube[1][4]:
                    F_minus()
                    T_minus()
                    R_plus()
                    T_plus()
                elif Cube[5][1] == Cube[2][4]:
                    F_minus()
                    R_plus()
                    F_plus()
                elif Cube[5][1] == Cube[3][4]:
                    F_minus()
                    T_plus()
                    R_plus()
                    T_minus()
                    F_plus()
                else:
                    F_plus()
                    L_minus()
                    F_minus()
                    
            Top_Edges_Complete += 1

    #Right Face moves
    elif pos[0] == 2:
        if Top_Edges_Complete == 0:
            if pos[1] == 1:
                if Cube[0][5] == Cube[2][4]:
                    R_plus()
                    K_plus()
                    T_plus()
                elif Cube[0][5] == Cube[3][4]:
                    R_plus()
                    K_plus()
                elif Cube[0][5] == Cube[4][4]:
                    R_plus()
                    K_plus()
                    T_minus()
                else:
                    R_minus()
                    F_minus()
            elif pos[1] == 3:
                if Cube[1][5] == Cube[2][4]:
                    F_minus()
                    T_minus()
                elif Cube[1][5] == Cube[3][4]:
                    F_minus()
                    T_minus()
                    T_minus()
                elif Cube[1][5] == Cube[4][4]:
                    F_minus()
                    T_plus()
                else:
                    L_minus()
            elif pos[1] == 5:
                if Cube[3][3] == Cube[2][4]:
                    K_plus()
                    T_plus()
                elif Cube[3][3] == Cube[3][4]:
                    K_plus()
                elif Cube[3][3] == Cube[4][4]:
                    K_plus()
                    T_minus()
                else:
                    K_plus()
                    T_plus()
                    T_plus()
            else:
                if Cube[5][5] == Cube[2][4]:
                    R_minus()
                    K_plus()
                    T_plus()
                elif Cube[5][5] == Cube[3][4]:
                    R_minus()
                    K_plus()
                elif Cube[5][5] == Cube[4][4]:
                    R_minus()
                    K_plus()
                    T_minus()
                else:
                    R_plus()
                    F_minus()
                    
            Top_Edges_Complete = 1
        else:
            if pos[1] == 1:
                if Cube[0][5] == Cube[2][4]:
                    R_plus()
                    T_minus()
                    K_plus()
                    T_plus()
                elif Cube[0][5] == Cube[3][4]:
                    R_plus()
                    K_plus()
                elif Cube[0][5] == Cube[4][4]:
                    R_plus()
                    T_plus()
                    K_plus()
                    T_minus()
                else:
                    R_minus()
                    F_minus()
            elif pos[1] == 3:
                if Cube[1][5] == Cube[2][4]:
                    T_plus()
                    F_minus()
                    T_minus()
                elif Cube[1][5] == Cube[3][4]:
                    T_plus()
                    T_plus()
                    F_minus()
                    T_minus()
                    T_minus()
                elif Cube[1][5] == Cube[4][4]:
                    T_minus()
                    F_minus()
                    T_plus()
                else:
                    F_minus()
            elif pos[1] == 5:
                if Cube[3][3] == Cube[2][4]:
                    T_minus()
                    K_plus()
                    T_plus()
                elif Cube[3][3] == Cube[3][4]:
                    K_plus()
                elif Cube[3][3] == Cube[4][4]:
                    T_plus()
                    K_plus()
                    T_minus()
                else:
                    T_minus()
                    T_minus()
                    K_plus()
                    T_plus()
                    T_plus()
            else:
                if Cube[5][5] == Cube[2][4]:
                    R_minus()
                    T_minus()
                    K_plus()
                    T_plus()
                elif Cube[5][5] == Cube[3][4]:
                    R_minus()
                    K_plus()
                    R_plus()
                elif Cube[5][5] == Cube[4][4]:
                    R_minus()
                    T_plus()
                    K_plus()
                    T_minus()
                    R_plus()
                else:
                    R_plus()
                    F_minus()
                    R_minus()
                    
            Top_Edges_Complete += 1

    #Back Face moves
    elif pos[0] == 3:
        if Top_Edges_Complete == 0:
            if pos[1] == 1:
                if Cube[0][1] == Cube[3][4]:
                    K_plus()
                    L_plus()
                    T_plus()
                elif Cube[0][1] == Cube[4][4]:
                    K_plus()
                    L_plus()
                elif Cube[0][1] == Cube[1][4]:
                    K_plus()
                    L_plus()
                    T_minus()
                else:
                    K_minus()
                    R_minus()
            elif pos[1] == 3:
                if Cube[2][5] == Cube[3][4]:
                    R_minus()
                    T_minus()
                elif Cube[2][5] == Cube[4][4]:
                    R_minus()
                    T_minus()
                    T_minus()
                elif Cube[2][5] == Cube[1][4]:
                    R_minus()
                    T_plus()
                else:
                    R_minus()
            elif pos[1] == 5:
                if Cube[4][3] == Cube[3][4]:
                    L_plus()
                    T_plus()
                elif Cube[4][3] == Cube[4][4]:
                    L_plus()
                elif Cube[4][3] == Cube[1][4]:
                    L_plus()
                    T_minus()
                else:
                    L_plus()
                    T_plus()
                    T_plus()
            else:
                if Cube[5][7] == Cube[3][4]:
                    K_minus()
                    L_plus()
                    T_plus()
                elif Cube[5][7] == Cube[4][4]:
                    K_minus()
                    L_plus()
                elif Cube[5][7] == Cube[1][4]:
                    K_minus()
                    L_plus()
                    T_minus()
                else:
                    K_plus()
                    R_minus()
                    
            Top_Edges_Complete = 1
        else:
            if pos[1] == 1:
                if Cube[0][1] == Cube[3][4]:
                    K_plus()
                    T_minus()
                    L_plus()
                    T_plus()
                elif Cube[0][1] == Cube[4][4]:
                    K_plus()
                    L_plus()
                elif Cube[0][1] == Cube[1][4]:
                    K_plus()
                    T_plus()
                    L_plus()
                    T_minus()
                else:
                    K_minus()
                    R_minus()
            elif pos[1] == 3:
                if Cube[2][5] == Cube[3][4]:
                    T_plus()
                    R_minus()
                    T_minus()
                elif Cube[2][5] == Cube[4][4]:
                    T_plus()
                    T_plus()
                    R_minus()
                    T_minus()
                    T_minus()
                elif Cube[2][5] == Cube[1][4]:
                    T_minus()
                    R_minus()
                    T_plus()
                else:
                    R_minus()
            elif pos[1] == 5:
                if Cube[4][3] == Cube[3][4]:
                    T_minus()
                    L_plus()
                    T_plus()
                elif Cube[4][3] == Cube[4][4]:
                    L_plus()
                elif Cube[4][3] == Cube[1][4]:
                    T_plus()
                    L_plus()
                    T_minus()
                else:
                    T_minus()
                    T_minus()
                    L_plus()
                    T_plus()
                    T_plus()
            else:
                if Cube[5][7] == Cube[3][4]:
                    K_minus()
                    T_minus()
                    L_plus()
                    T_plus()
                elif Cube[5][7] == Cube[4][4]:
                    K_minus()
                    L_plus()
                    K_plus()
                elif Cube[5][7] == Cube[1][4]:
                    K_minus()
                    T_plus()
                    L_plus()
                    T_minus()
                    K_plus()
                else:
                    K_plus()
                    R_minus()
                    K_minus()
                    
            Top_Edges_Complete += 1

    #Left Face moves
    elif pos[0] == 4:
        if Top_Edges_Complete == 0:
            if pos[1] == 1:
                if Cube[0][3] == Cube[4][4]:
                    L_plus()
                    F_plus()
                    T_plus()
                elif Cube[0][3] == Cube[1][4]:
                    L_plus()
                    F_plus()
                elif Cube[0][3] == Cube[2][4]:
                    L_plus()
                    F_plus()
                    T_minus()
                else:
                    L_minus()
                    K_minus()
            elif pos[1] == 3:
                if Cube[3][5] == Cube[4][4]:
                    K_minus()
                    T_minus()
                elif Cube[3][5] == Cube[1][4]:
                    K_minus()
                    T_minus()
                    T_minus()
                elif Cube[3][5] == Cube[2][4]:
                    K_minus()
                    T_plus()
                else:
                    K_minus()
            elif pos[1] == 5:
                if Cube[1][3] == Cube[4][4]:
                    F_plus()
                    T_plus()
                elif Cube[1][3] == Cube[1][4]:
                    F_plus()
                elif Cube[1][3] == Cube[2][4]:
                    F_plus()
                    T_minus()
                else:
                    F_plus()
                    T_plus()
                    T_plus()
            else:
                if Cube[5][3] == Cube[4][4]:
                    L_minus()
                    F_plus()
                    T_plus()
                elif Cube[5][3] == Cube[1][4]:
                    L_minus()
                    F_plus()
                elif Cube[5][3] == Cube[2][4]:
                    L_minus()
                    F_plus()
                    T_minus()
                else:
                    L_plus()
                    K_minus()
                    
            Top_Edges_Complete = 1

        else:
            if pos[1] == 1:
                if Cube[0][3] == Cube[4][4]:
                    L_plus()
                    T_minus()
                    F_plus()
                    T_plus()
                elif Cube[0][3] == Cube[1][4]:
                    L_plus()
                    F_plus()
                elif Cube[0][3] == Cube[2][4]:
                    L_plus()
                    T_plus()
                    F_plus()
                    T_minus()
                else:
                    L_minus()
                    K_minus()
            elif pos[1] == 3:
                if Cube[3][5] == Cube[4][4]:
                    T_plus()
                    K_minus()
                    T_minus()
                elif Cube[3][5] == Cube[1][4]:
                    T_plus()
                    T_plus()
                    K_minus()
                    T_minus()
                    T_minus()
                elif Cube[3][5] == Cube[2][4]:
                    T_minus()
                    K_minus()
                    T_plus()
                else:
                    K_minus()
            elif pos[1] == 5:
                if Cube[1][3] == Cube[4][4]:
                    T_minus()
                    F_plus()
                    T_plus()
                elif Cube[1][3] == Cube[1][4]:
                    F_plus()
                elif Cube[1][3] == Cube[2][4]:
                    T_plus()
                    F_plus()
                    T_minus()
                else:
                    T_minus()
                    T_minus()
                    F_plus()
                    T_plus()
                    T_plus()
            else:
                if Cube[5][3] == Cube[4][4]:
                    L_minus()
                    T_minus()
                    F_plus()
                    T_plus()
                elif Cube[5][3] == Cube[1][4]:
                    L_minus()
                    F_plus()
                    L_plus()
                elif Cube[5][3] == Cube[2][4]:
                    L_minus()
                    T_plus()
                    F_plus()
                    T_minus()
                    L_plus()
                else:
                    L_plus()
                    K_minus()
                    L_minus()
                    
            Top_Edges_Complete += 1

    #Bottom Face moves
    else:
        if pos[1] == 1:
            if Cube[1][7] == Cube[1][4]:
                F_plus()
                F_plus()
            elif Cube[1][7] == Cube[2][4]:
                B_plus()
                R_plus()
                R_plus()
            elif Cube[1][7] == Cube[3][4]:
                B_plus()
                B_plus()
                K_plus()
                K_plus()
            else:
                B_minus()
                L_plus()
                L_plus()
        elif pos[1] == 3:
            if Cube[4][7] == Cube[1][4]:
                B_plus()
                F_plus()
                F_plus()
            elif Cube[4][7] == Cube[2][4]:
                B_plus()
                B_plus()
                R_plus()
                R_plus()
            elif Cube[4][7] == Cube[3][4]:
                B_minus()
                K_plus()
                K_plus()
            else:
                L_plus()
                L_plus()
        elif pos[1] == 5:
            if Cube[2][7] == Cube[1][4]:
                B_minus()
                F_plus()
                F_plus()
            elif Cube[2][7] == Cube[2][4]:
                R_plus()
                R_plus()
            elif Cube[2][7] == Cube[3][4]:
                B_plus()
                K_plus()
                K_plus()
            else:
                B_plus()
                B_plus()
                L_plus()
                L_plus()
        else:
            if Cube[3][7] == Cube[1][4]:
                B_plus()
                B_plus()
                F_plus()
                F_plus()
            elif Cube[3][7] == Cube[2][4]:
                B_minus()
                R_plus()
                R_plus()
            elif Cube[3][7] == Cube[3][4]:
                K_plus()
                K_plus()
            else:
                B_plus()
                L_plus()
                L_plus()
                
        Top_Edges_Complete += 1


def move_corner_top(pos):
    global Solution_Sequence

    #Top face moves
    if pos[0] == 0:
        if pos[1] == 0:
            if Cube[3][2] == Cube[1][4]:
                K_plus()
                B_minus()
                B_minus()
                K_minus()
                R_minus()
                B_minus()
                R_plus()
            elif Cube[3][2] == Cube[2][4]:
                L_minus()
                B_minus()
                L_plus()
                B_minus()
                K_minus()
                B_plus()
                K_plus()
            elif Cube[3][2] == Cube[4][4]:
                K_plus()
                B_plus()
                K_minus()
                F_minus()
                B_minus()
                F_plus()
                
        elif pos[1] == 2:
            if Cube[2][2] == Cube[1][4]:
                K_minus()
                B_minus()
                K_plus()
                B_minus()
                R_minus()
                B_plus()
                R_plus()
            elif Cube[2][2] == Cube[3][4]:
                R_plus()
                B_plus()
                R_minus()
                L_minus()
                B_minus()
                L_plus()
            elif Cube[2][2] == Cube[4][4]:
                R_plus()
                B_minus()
                B_minus()
                R_minus()
                F_minus()
                B_minus()
                F_plus()

        elif pos[1] == 6:
            if Cube[4][2] == Cube[1][4]:
                L_plus()
                B_plus()
                L_minus()
                R_minus()
                B_minus()
                R_plus()
            elif Cube[4][2] == Cube[2][4]:
                L_plus()
                B_plus()
                B_plus()
                L_minus()
                K_minus()
                B_minus()
                K_plus()
            elif Cube[4][2] == Cube[3][4]:
                F_minus()
                B_minus()
                F_plus()
                B_minus()
                L_minus()
                B_plus()
                L_plus()
                
        elif pos[1] == 8:
            if Cube[1][2] == Cube[2][4]:
                F_plus()
                B_plus()
                F_minus()
                K_minus()
                B_minus()
                K_plus()
                
            elif Cube[1][2] == Cube[3][4]:
                F_plus()
                B_plus()
                B_plus()
                F_minus()
                L_minus()
                B_minus()
                L_plus()
                
            elif Cube[1][2] == Cube[4][4]:
                R_minus()
                B_minus()
                R_plus()
                B_minus()
                F_minus()
                B_plus()
                F_plus()

    #Front face moves
    elif pos[0] == 1:
        if pos[1] == 0:
            if Cube[0][6] == Cube[1][4]:
                L_plus()
                B_minus()
                L_minus()
                B_plus()
                R_minus()
                B_minus()
                R_plus()

            elif Cube[0][6] == Cube[2][4]:
                F_minus()
                B_plus()
                B_plus()
                F_plus()
                K_minus()
                B_minus()
                K_plus()
                

            elif Cube[0][6] == Cube[3][4]:
                F_minus()
                K_plus()
                B_minus()
                K_minus()
                F_plus()

            elif Cube[0][6] == Cube[4][4]:
                L_plus()
                B_minus()
                L_minus()
                B_plus()
                L_plus()
                B_minus()
                L_minus()

        elif pos[1] == 2:
            if Cube[0][8] == Cube[1][4]:
                R_minus()
                B_plus()
                R_plus()
                B_minus()
                L_plus()
                B_plus()
                L_minus()

            elif Cube[0][8] == Cube[2][4]:
                R_minus()
                B_plus()
                R_plus()
                B_minus()
                R_minus()
                B_plus()
                R_plus()
                                         
            elif Cube[0][8] == Cube[3][4]:
                F_plus()
                K_minus()
                B_plus()
                K_plus()
                F_minus()

            elif Cube[0][8] == Cube[4][4]:
                F_plus()
                B_minus()
                B_minus()
                F_minus()
                K_plus()
                B_plus()
                K_minus()
                                         
        elif pos[1] == 6:
            if Cube[5][0] == Cube[1][4]:
                B_plus()
                L_plus()
                B_minus()
                L_minus()

            elif Cube[5][0] == Cube[2][4]:
                B_minus()
                F_plus()
                B_plus()
                B_plus()
                F_minus()

            elif Cube[5][0] == Cube[3][4]:
                R_plus()
                B_plus()
                B_plus()
                R_minus()

            elif Cube[5][0] == Cube[4][4]:
                K_plus()
                B_minus()
                K_minus()

        elif pos[1] == 8:
            if Cube[5][2] == Cube[1][4]:
                B_minus()
                R_minus()
                B_plus()
                R_plus()

            elif Cube[5][2] == Cube[2][4]:
                K_minus()
                B_plus()
                K_plus()

            elif Cube[5][2] == Cube[3][4]:
                L_minus()
                B_plus()
                B_plus()
                L_plus()

            elif Cube[5][2] == Cube[4][4]:
                B_plus()
                F_minus()
                B_minus()
                B_minus()
                F_plus()
                
    #Right face moves
    elif pos[0] == 2:
        if pos[1] == 0:
            if Cube[0][8] == Cube[1][4]:
                F_plus()
                B_minus()
                F_minus()
                R_minus()
                B_minus()
                R_plus()
                                         
            elif Cube[0][8] == Cube[2][4]:
                F_plus()
                B_minus()
                F_minus()
                B_plus()
                K_minus()
                B_minus()
                K_plus()

            elif Cube[0][8] == Cube[3][4]:
                R_minus()
                B_minus()
                R_plus()
                K_plus()
                B_minus()
                K_minus()

            elif Cube[0][8] == Cube[4][4]:
                R_minus()
                L_plus()
                B_minus()
                L_minus()
                R_plus()

        elif pos[1] == 2:
            if Cube[0][2] == Cube[1][4]:
                R_plus()
                B_plus()
                R_minus()
                F_minus()
                B_plus()
                F_plus()

            elif Cube[0][2] == Cube[2][4]:
                R_plus()
                B_plus()
                R_minus()
                R_minus()
                B_plus()
                B_plus()
                R_plus()

            elif Cube[0][2] == Cube[3][4]:
                R_plus()
                B_plus()
                R_minus()
                B_minus()
                B_minus()
                K_minus()
                B_plus()
                K_plus()

            elif Cube[0][2] == Cube[4][4]:
                R_plus()
                B_plus()
                R_minus()
                B_minus()
                L_minus()
                B_plus()
                L_plus()

        elif pos[1] == 6:
            if Cube[5][2] == Cube[1][4]:
                L_plus()
                B_minus()
                L_minus()

            elif Cube[5][2] == Cube[2][4]:
                R_minus()
                B_minus()
                R_plus()

            elif Cube[5][2] == Cube[3][4]:
                B_plus()
                K_minus()
                B_minus()
                K_plus()

            elif Cube[5][2] == Cube[4][4]:
                K_plus()
                B_plus()
                B_plus()
                K_minus()

        elif pos[1] == 8:
            if Cube[5][8] == Cube[1][4]:
                B_minus()
                B_minus()
                R_minus()
                B_plus()
                R_plus()

            elif Cube[5][8] == Cube[2][4]:
                B_minus()
                K_minus()
                B_plus()
                K_plus()

            elif Cube[5][8] == Cube[3][4]:
                L_minus()
                B_plus()
                L_plus()

            elif Cube[5][8] == Cube[4][4]:
                F_minus()
                B_minus()
                B_minus()
                F_plus()

    #Back face moves
    elif pos[0] == 3:
        if pos[1] == 0:
            if Cube[0][2] == Cube[1][4]:
                K_minus()
                F_plus()
                B_minus()
                F_minus()
                K_plus()

            elif Cube[0][2] == Cube[2][4]:
                K_minus()
                B_minus()
                K_plus()
                B_plus()
                K_minus()
                B_minus()
                K_plus()

            elif Cube[0][2] == Cube[3][4]:
                R_plus()
                B_minus()
                R_minus()
                B_plus()
                L_minus()
                B_minus()
                L_plus()

            elif Cube[0][2] == Cube[4][4]:
                K_minus()
                L_plus()
                B_minus()
                B_minus()
                L_minus()
                K_plus()

        elif pos[1] == 2:
            if Cube[0][0] == Cube[1][4]:
                K_plus()
                F_minus()
                B_plus()
                F_plus()
                K_minus()

            elif Cube[0][0] == Cube[2][4]:
                K_plus()
                R_minus()
                B_plus()
                B_plus()
                R_plus()
                K_minus()

            elif Cube[0][0] == Cube[3][4]:
                K_plus()
                B_plus()
                K_minus()
                K_minus()
                B_minus()
                B_minus()
                K_plus()

            elif Cube[0][0] == Cube[4][4]:
                L_minus()
                B_plus()
                L_plus()
                B_minus()
                L_minus()
                B_plus()
                L_plus()

        elif pos[1] == 6:
            if Cube[5][8] == Cube[1][4]:
                B_plus()
                B_plus()
                F_minus()
                B_minus()
                F_plus()

            elif Cube[5][8] == Cube[2][4]:
                F_plus()
                B_minus()
                F_minus()

            elif Cube[5][8] == Cube[3][4]:
                K_minus()
                B_minus()
                K_plus()

            elif Cube[5][8] == Cube[4][4]:
                B_plus()
                L_minus()
                B_minus()
                L_plus()

        elif pos[1] == 8:
            if Cube[5][6] == Cube[1][4]:
                R_minus()
                B_minus()
                B_minus()
                R_plus()

            elif Cube[5][6] == Cube[2][4]:
                B_plus()
                K_minus()
                B_minus()
                B_minus()
                K_plus()

            elif Cube[5][6] == Cube[3][4]:
                B_minus()
                L_minus()
                B_plus()
                L_plus()

            elif Cube[5][6] == Cube[4][4]:
                F_minus()
                B_plus()
                F_plus()

    #Left face moves
    elif pos[0] == 4:
        if pos[1] == 0:
            if Cube[0][0] == Cube[1][4]:
                F_plus()
                L_minus()
                B_plus()
                B_plus()
                L_plus()
                F_minus()

            elif Cube[0][0] == Cube[2][4]:
                L_minus()
                R_plus()
                B_minus()
                R_minus()
                L_plus()

            elif Cube[0][0] == Cube[3][4]:
                L_minus()
                B_minus()
                L_plus()
                B_plus()
                L_minus()
                B_minus()
                L_plus()

            elif Cube[0][0] == Cube[4][4]:
                L_minus()
                B_minus()
                L_plus()
                L_plus()
                B_plus()
                B_plus()
                L_minus()

        elif pos[1] == 2:
            if Cube[0][6] == Cube[1][4]:
                F_minus()
                B_plus()
                F_plus()
                B_minus()
                F_minus()
                B_plus()
                F_plus()

            elif Cube[0][6] == Cube[2][4]:
                L_plus()
                R_minus()
                B_plus()
                R_plus()
                L_minus()

            elif Cube[0][6] == Cube[3][4]:
                L_plus()
                K_minus()
                B_plus()
                B_plus()
                K_plus()
                L_minus()

            elif Cube[0][6] == Cube[4][4]:
                L_plus()
                B_plus()
                L_minus()
                L_minus()
                B_minus()
                B_minus()
                L_plus()

        elif pos[1] == 6:
            if Cube[5][6] == Cube[1][4]:
                B_plus()
                F_minus()
                B_minus()
                F_plus()

            elif Cube[5][6] == Cube[2][4]:
                F_plus()
                B_plus()
                B_plus()
                F_minus()

            elif Cube[5][6] == Cube[3][4]:
                R_plus()
                B_minus()
                R_minus()

            elif Cube[5][6] == Cube[4][4]:
                L_minus()
                B_minus()
                L_plus()
                
        elif pos[1] == 8:
            if Cube[5][0] == Cube[1][4]:
                R_minus()
                B_plus()
                R_plus()

            elif Cube[5][0] == Cube[2][4]:
                K_minus()
                B_plus()
                B_plus()
                K_plus()

            elif Cube[5][0] == Cube[3][4]:
                B_plus()
                L_minus()
                B_minus()
                B_minus()
                L_plus()

            elif Cube[5][0] == Cube[4][4]:
                B_minus()
                F_minus()
                B_plus()
                F_plus()

    #Bottom face moves
    elif pos[0] == 5:
        if pos[1] == 0:
            if Cube[1][6] == Cube[1][4]:
                B_plus()
                R_minus()
                B_plus()
                R_plus()
                F_plus()
                B_minus()
                B_minus()
                F_minus()

            elif Cube[1][6] == Cube[2][4]:
                B_minus()
                B_minus()
                K_minus()
                B_plus()
                K_plus()
                R_plus()
                B_minus()
                B_minus()
                R_minus()

            elif Cube[1][6] == Cube[3][4]:
                B_minus()
                L_minus()
                B_plus()
                L_plus()
                K_plus()
                B_minus()
                B_minus()
                K_minus()

            elif Cube[1][6] == Cube[4][4]:
                F_minus()
                B_plus()
                F_plus()
                L_plus()
                B_minus()
                B_minus()
                L_minus()

        elif pos[1] == 2:
            if Cube[2][6] == Cube[1][4]:
                R_minus()
                B_plus()
                R_plus()
                F_plus()
                B_minus()
                B_minus()
                F_minus()

            elif Cube[2][6] == Cube[2][4]:
                B_plus()
                K_minus()
                B_plus()
                K_plus()
                R_plus()
                B_minus()
                B_minus()
                R_minus()

            elif Cube[2][6] == Cube[3][4]:
                B_minus()
                B_minus()
                L_minus()
                B_plus()
                L_plus()
                K_plus()
                B_minus()
                B_minus()
                K_minus()

            elif Cube[2][6] == Cube[4][4]:
                B_minus()
                F_minus()
                B_plus()
                F_plus()
                L_plus()
                B_minus()
                B_minus()
                L_minus()

        elif pos[1] == 6:
            if Cube[4][6] == Cube[1][4]:
                R_minus()
                B_minus()
                R_plus()
                B_minus()
                R_minus()
                B_plus()
                R_plus()

            elif Cube[4][6] == Cube[2][4]:
                B_minus()
                K_minus()
                B_plus()
                K_plus()
                R_plus()
                B_minus()
                B_minus()
                R_minus()

            elif Cube[4][6] == Cube[3][4]:
                L_minus()
                B_plus()
                L_plus()
                K_plus()
                B_minus()
                B_minus()
                K_minus()

            elif Cube[4][6] == Cube[4][4]:
                B_plus()
                F_minus()
                B_plus()
                F_plus()
                L_plus()
                B_minus()
                B_minus()
                L_minus()

        elif pos[1] == 8:
            if Cube[3][6] == Cube[1][4]:
                B_minus()
                R_minus()
                B_plus()
                R_plus()
                F_plus()
                B_minus()
                B_minus()
                F_minus()

            elif Cube[3][6] == Cube[2][4]:
                K_minus()
                B_plus()
                K_plus()
                R_plus()
                B_minus()
                B_minus()
                R_minus()

            elif Cube[3][6] == Cube[3][4]:
                B_plus()
                L_minus()
                B_plus()
                L_plus()
                K_plus()
                B_minus()
                B_minus()
                K_minus()

            elif Cube[3][6] == Cube[4][4]:
                L_plus()
                B_plus()
                L_minus()
                B_plus()
                L_plus()
                B_minus()
                L_minus()


def find_mid_on_bot():
    pos = []
    if Cube[1][7] == Cube[1][4] and Cube[5][1] != Cube[5][4]:
        pos.append(1)
    elif Cube[2][7] == Cube[2][4] and Cube[5][5] != Cube[5][4]:
        pos.append(2)
    elif Cube[3][7] == Cube[3][4] and Cube[5][7] != Cube[5][4]:
        pos.append(3)
    elif Cube[4][7] == Cube[4][4] and Cube[5][3] != Cube[5][4]:
        pos.append(4)
    elif Cube[1][7] != Cube[5][4] and Cube[5][1] != Cube[5][4]:
        pos.append(1)
    elif Cube[2][7] != Cube[5][4] and Cube[5][5] != Cube[5][4]:
        pos.append(2)
    elif Cube[3][7] != Cube[5][4] and Cube[5][7] != Cube[5][4]:
        pos.append(3)
    elif Cube[4][7] != Cube[5][4] and Cube[5][3] != Cube[5][4]:
        pos.append(4)
    else:
        pos.append(-1)

    return pos


def set_mid_edge(face):
    global Solution_Sequence
    if face == 1:
        if Cube[5][1] == Cube[2][4]:
            B_minus()
            R_minus()
            B_plus()
            R_plus()
            B_plus()
            F_plus()
            B_minus()
            F_minus()
        else:
            B_plus()
            L_plus()
            B_minus()
            L_minus()
            B_minus()
            F_minus()
            B_plus()
            F_plus()
            
    elif face == 2:
        if Cube[5][5] == Cube[3][4]:
            B_minus()
            K_minus()
            B_plus()
            K_plus()
            B_plus()
            R_plus()
            B_minus()
            R_minus()
        else:
            B_plus()
            F_plus()
            B_minus()
            F_minus()
            B_minus()
            R_minus()
            B_plus()
            R_plus()
            
    elif face == 3:
        if Cube[5][7] == Cube[4][4]:
            B_minus()
            L_minus()
            B_plus()
            L_plus()
            B_plus()
            K_plus()
            B_minus()
            K_minus()
        else:
            B_plus()
            R_plus()
            B_minus()
            R_minus()
            B_minus()
            K_minus()
            B_plus()
            K_plus()
            
    else: #face == 4
        if Cube[5][3] == Cube[1][4]:
            B_minus()
            F_minus()
            B_plus()
            F_plus()
            B_plus()
            L_plus()
            B_minus()
            L_minus()
        else:
            B_plus()
            K_plus()
            B_minus()
            K_minus()
            B_minus()
            L_minus()
            B_plus()
            L_plus()


def top_edges():
    global Top_Edges_Complete, Solution_Sequence
    ToDoFaces = []
    
    if Cube[0][7] == Cube[0][4] and Cube[1][1] == Cube[1][4]:
        Top_Edges_Complete += 1
    else:
        ToDoFaces.append(1)

    if Cube[0][5] == Cube[0][4] and Cube[2][1] == Cube[2][4]:
        Top_Edges_Complete += 1
    else:
        ToDoFaces.append(2)

    if Cube[0][1] == Cube[0][4] and Cube[3][1] == Cube[3][4]:
        Top_Edges_Complete += 1
    else:
        ToDoFaces.append(3)

    if Cube[0][3] == Cube[0][4] and Cube[4][1] == Cube[4][4]:
        Top_Edges_Complete += 1
    else:
        ToDoFaces.append(4)

    for i in range(0,len(ToDoFaces)):
        pos = find_edge(Cube[0][4], Cube[ToDoFaces[i]][4])
        move_edge_top(pos)


def top_corners():
    global Solution_Sequence

    pos = find_corner(Cube[0][4], Cube[1][4], Cube[2][4])
    move_corner_top(pos)

    pos = find_corner(Cube[0][4], Cube[2][4], Cube[3][4])
    move_corner_top(pos)
    
    pos = find_corner(Cube[0][4], Cube[3][4], Cube[4][4])
    move_corner_top(pos)

    pos = find_corner(Cube[0][4], Cube[4][4], Cube[1][4])
    move_corner_top(pos)


def middle_edges():
    global Solution_Sequence
    counter = 0
    while True:
        counter += 1
        if counter > 30:
            print "\nMiddle Edges Loop Unsuccessful\n"
            break
        elif Cube[1][3] == Cube[1][4] and Cube[1][5] == Cube[1][4] and Cube[2][3] == Cube[2][4] and Cube[2][5] == Cube[2][4] and Cube[3][3] == Cube[3][4] and Cube[3][5] == Cube[3][4] and Cube[4][3] == Cube[4][4] and Cube[4][5] == Cube[4][4]:
            break
        else:
            pos = find_mid_on_bot()
            if pos[0] != -1:
                
                if pos[0] == 1:
                    if Cube[1][7] == Cube[1][4]:
                        set_mid_edge(1)
                    elif Cube[1][7] == Cube[2][4]:
                        B_plus()
                        set_mid_edge(2)
                    elif Cube[1][7] == Cube[3][4]:
                        B_plus()
                        B_plus()
                        set_mid_edge(3)
                    elif Cube[1][7] == Cube[4][4]:
                        B_minus()
                        set_mid_edge(4)

                elif pos[0] == 2:
                    if Cube[2][7] == Cube[1][4]:
                        B_minus()
                        set_mid_edge(1)
                    elif Cube[2][7] == Cube[2][4]:
                        set_mid_edge(2)
                    elif Cube[2][7] == Cube[3][4]:
                        B_plus()
                        set_mid_edge(3)
                    elif Cube[2][7] == Cube[4][4]:
                        B_plus()
                        B_plus()
                        set_mid_edge(4)

                elif pos[0] == 3:
                    if Cube[3][7] == Cube[1][4]:
                        B_plus()
                        B_plus()
                        set_mid_edge(1)
                    elif Cube[3][7] == Cube[2][4]:
                        B_minus()
                        set_mid_edge(2)
                    elif Cube[3][7] == Cube[3][4]:
                        set_mid_edge(3)
                    elif Cube[3][7] == Cube[4][4]:
                        B_plus()
                        set_mid_edge(4)

                else: #pos[0] == 4
                    if Cube[4][7] == Cube[1][4]:
                        B_plus()
                        set_mid_edge(1)
                    elif Cube[4][7] == Cube[2][4]:
                        B_plus()
                        B_plus()
                        set_mid_edge(2)
                    elif Cube[4][7] == Cube[3][4]:
                        B_minus()
                        set_mid_edge(3)
                    elif Cube[4][7] == Cube[4][4]:
                        set_mid_edge(4)
            else:
                #no more middle edge pieces found on the bottom layer but the middle layer is still not solved
                if Cube[1][3] != Cube[5][4] and Cube[4][5] != Cube[5][4] and (Cube[1][3] != Cube[1][4] or Cube[4][5] != Cube[4][4]):
                    L_plus()
                    B_minus()
                    L_minus()
                    B_minus()
                    F_minus()
                    B_plus()
                    F_plus()

                elif Cube[2][3] != Cube[5][4] and Cube[1][5] != Cube[5][4] and (Cube[2][3] != Cube[2][4] or Cube[1][5] != Cube[1][4]):
                    F_plus()
                    B_minus()
                    F_minus()
                    B_minus()
                    R_minus()
                    B_plus()
                    R_plus()

                elif Cube[3][3] != Cube[5][4] and Cube[2][5] != Cube[5][4] and (Cube[3][3] != Cube[3][4] or Cube[2][5] != Cube[2][4]):
                    R_plus()
                    B_minus()
                    R_minus()
                    B_minus()
                    K_minus()
                    B_plus()
                    K_plus()

                else: #Cube[4][3] != Cube[5][4] and Cube[3][5] != Cube[5][4] and (Cube[4][3] != Cube[4][4] or Cube[3][5] != Cube[3][4]):
                    K_plus()
                    B_minus()
                    K_minus()
                    B_minus()
                    L_minus()
                    B_plus()
                    L_plus()


def get_bottom_edges():
    #remember the initial bottom face has been flipped so it is now the top face

    if Cube[0][1] != Cube[0][4] and Cube[0][3] != Cube[0][4] and Cube[0][5] != Cube[0][4] and Cube[0][7] != Cube[0][4]:
        F_plus()
        R_plus()
        T_plus()
        R_minus()
        T_minus()
        F_minus()
        K_plus()
        T_plus()
        L_plus()
        T_minus()
        L_minus()
        K_minus()
        
    elif Cube[0][1] != Cube[0][4] and Cube[0][3] != Cube[0][4] and Cube[0][5] == Cube[0][4] and Cube[0][7] == Cube[0][4]:
        K_plus()
        T_plus()
        L_plus()
        T_minus()
        L_minus()
        K_minus()
        
    elif Cube[0][1] != Cube[0][4] and Cube[0][3] == Cube[0][4] and Cube[0][5] != Cube[0][4] and Cube[0][7] == Cube[0][4]:
        R_plus()
        T_plus()
        K_plus()
        T_minus()
        K_minus()
        R_minus()
        
    elif Cube[0][1] == Cube[0][4] and Cube[0][3] == Cube[0][4] and Cube[0][5] != Cube[0][4] and Cube[0][7] != Cube[0][4]:
        F_plus()
        T_plus()
        R_plus()
        T_minus()
        R_minus()
        F_minus()
        
    elif Cube[0][1] == Cube[0][4] and Cube[0][3] != Cube[0][4] and Cube[0][5] == Cube[0][4] and Cube[0][7] != Cube[0][4]:
        L_plus()
        T_plus()
        F_plus()
        T_minus()
        F_minus()
        L_minus()
        
    elif Cube[0][1] == Cube[0][4] and Cube[0][3] != Cube[0][4] and Cube[0][5] != Cube[0][4] and Cube[0][7] == Cube[0][4]:
        L_plus()
        F_plus()
        T_plus()
        F_minus()
        T_minus()
        L_minus()
        
    elif Cube[0][1] != Cube[0][4] and Cube[0][3] == Cube[0][4] and Cube[0][5] == Cube[0][4] and Cube[0][7] != Cube[0][4]:
        F_plus()
        R_plus()
        T_plus()
        R_minus()
        T_minus()
        F_minus()


def set_bottom_edges():
    stopCondition = False
    while stopCondition == False:
        count = 0
        Back = False
        Left = False
        Front = False
        Right = False

        if Cube[1][1] == Cube[1][4]:
            count +=1
            Front = True
        if Cube[2][1] == Cube[2][4]:
            count +=1
            Right = True
        if Cube[3][1] == Cube[3][4]:
            count +=1
            Back = True
        if Cube[4][1] == Cube[4][4]:
            count +=1
            Left = True

        if count == 0 or count == 1:
            T_plus()
        elif count == 2:
            if Front and Back:
                F_plus()
                T_plus()
                F_minus()
                T_plus()
                F_plus()
                T_plus()
                T_plus()
                F_minus()
                T_plus()
            elif Left and Right:
                R_plus()
                T_plus()
                R_minus()
                T_plus()
                R_plus()
                T_plus()
                T_plus()
                R_minus()
                T_plus()
            elif Front and Right:
                F_plus()
                T_plus()
                F_minus()
                T_plus()
                F_plus()
                T_plus()
                T_plus()
                F_minus()
                T_plus()
            elif Back and Right:
                R_plus()
                T_plus()
                R_minus()
                T_plus()
                R_plus()
                T_plus()
                T_plus()
                R_minus()
                T_plus()
            elif Left and Back:
                K_plus()
                T_plus()
                K_minus()
                T_plus()
                K_plus()
                T_plus()
                T_plus()
                K_minus()
                T_plus()
            elif Left and Front:
                L_plus()
                T_plus()
                L_minus()
                T_plus()
                L_plus()
                T_plus()
                T_plus()
                L_minus()
                T_plus()
        else: #the cross has been set
            stopCondition = True


def get_bottom_corners():
    stopCondition = False
    while stopCondition == False:
        count = 0
        FrontLeft = False
        FrontRight = False
        BackLeft = False
        BackRight = False

        FrontLeftStr = Cube[0][6] + Cube[4][2] + Cube[1][0]
        FrontRightStr = Cube[0][8] + Cube[1][2] + Cube[2][0]
        BackLeftStr = Cube[0][0] + Cube[3][2] + Cube[4][0]
        BackRightStr = Cube[0][2] + Cube[2][2] + Cube[3][0]

        if Cube[0][4] in FrontLeftStr and Cube[1][4] in FrontLeftStr and Cube[4][4] in FrontLeftStr:
            count +=1
            FrontLeft = True
        if Cube[0][4] in FrontRightStr and Cube[1][4] in FrontRightStr and Cube[2][4] in FrontRightStr:
            count +=1
            FrontRight = True
        if Cube[0][4] in BackLeftStr and Cube[3][4] in BackLeftStr and Cube[4][4] in BackLeftStr:
            count +=1
            BackLeft = True
        if Cube[0][4] in BackRightStr and Cube[3][4] in BackRightStr and Cube[2][4] in BackRightStr:
            count +=1
            BackRight = True

        if count == 0:
            T_plus()
            L_plus()
            T_minus()
            R_minus()
            T_plus()
            L_minus()
            T_minus()
            R_plus()
        elif count == 1:
            if FrontLeft:
                T_plus()
                F_plus()
                T_minus()
                K_minus()
                T_plus()
                F_minus()
                T_minus()
                K_plus()
            elif FrontRight:
                T_plus()
                R_plus()
                T_minus()
                L_minus()
                T_plus()
                R_minus()
                T_minus()
                L_plus()                
            elif BackLeft:
                T_plus()
                L_plus()
                T_minus()
                R_minus()
                T_plus()
                L_minus()
                T_minus()
                R_plus()                
            else: #BackRight
                T_plus()
                K_plus()
                T_minus()
                F_minus()
                T_plus()
                K_minus()
                T_minus()
                F_plus()                
        elif count == 4: #bottom corners are now positioned
            stopCondition = True


def set_bottom_corners():
    stopCondition = False
    while stopCondition == False:
        if Cube[0][0] == Cube[0][4] and Cube[0][2] == Cube[0][4] and Cube[0][6] == Cube[0][4] and Cube[0][8] == Cube[0][4]:
            stopCondition = True
        else:
            if Cube[0][8] == Cube[0][4]:
                T_plus()
            else:
                if Cube[1][2] == Cube[0][4]:
                    B_minus()
                    R_minus()
                    B_plus()
                    R_plus()
                    B_minus()
                    R_minus()
                    B_plus()
                    R_plus()
                else:
                    R_minus()
                    B_minus()
                    R_plus()
                    B_plus()
                    R_minus()
                    B_minus()
                    R_plus()
                    B_plus()

    stopCondition = False
    while stopCondition == False:
        if Cube[1][1] == Cube[1][4]:
            stopCondition = True
        else:
            T_plus()
  
    
def main():
    if foundCalibration:
        global Cube, Solution_Sequence
        
        #Face = (0,1,2,3,4,5,6,7,8)
        Top = (sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9])
        Front = (sys.argv[10],sys.argv[11],sys.argv[12],sys.argv[13],sys.argv[14],sys.argv[15],sys.argv[16],sys.argv[17],sys.argv[18])
        Right = (sys.argv[19],sys.argv[20],sys.argv[21],sys.argv[22],sys.argv[23],sys.argv[24],sys.argv[25],sys.argv[26],sys.argv[27])
        Back = (sys.argv[28],sys.argv[29],sys.argv[30],sys.argv[31],sys.argv[32],sys.argv[33],sys.argv[34],sys.argv[35],sys.argv[36])
        Left = (sys.argv[37],sys.argv[38],sys.argv[39],sys.argv[40],sys.argv[41],sys.argv[42],sys.argv[43],sys.argv[44],sys.argv[45])
        Bottom = (sys.argv[46],sys.argv[47],sys.argv[48],sys.argv[49],sys.argv[50],sys.argv[51],sys.argv[52],sys.argv[53],sys.argv[54])
    
        #        0     1      2      3     4      5
        Cube = (Top, Front, Right, Back, Left, Bottom)
        Original_Cube = Cube
        
        if check_input_count():
            f = open('log.txt','a')
            write_cube(f, Cube)
    
            top_edges()
            top_corners()
    
            middle_edges()
    
            #Flip bottom face to now be the top
            X_plus()
            X_plus()
    
            get_bottom_edges()
            set_bottom_edges()
            get_bottom_corners()
            set_bottom_corners()
    
            X_plus()
            X_plus()
            
            clean_sequence()
            test = check_sequence(Original_Cube)    #check that the cleaned sequence actually produces a solved cube
            
            if test:
                Machine_Sequence = trans_sequence()
                print("\rCube Solved")
                #print("Manual Sequence")
                #print_sequence(Solution_Sequence)
                write_sequence(f,Solution_Sequence)
                #print("Machine Sequence")
                #print_sequence(Machine_Sequence)
                write_sequence(f,Machine_Sequence)
                solNum = 0
                for i in range(0,len(Solution_Sequence)):
                   if Solution_Sequence[i] == 'T+' or Solution_Sequence[i] == 'T-' or Solution_Sequence[i] == 'B+' or Solution_Sequence[i] == 'B-':
                      solNum += 3
                   else:
                      solNum += 1
                macNum = 0
                for i in range(0,len(Machine_Sequence)):
                   if Machine_Sequence[i] == 'T+' or Machine_Sequence[i] == 'T-' or Machine_Sequence[i] == 'B+' or Machine_Sequence[i] == 'B-':
                      macNum += 2
                   else:
                      macNum += 1
                #print("Manual sequence length: " + str(solNum))
                print("\rMachine sequence length: " + str(macNum))
    
                #print_cube(Cube)
    
                runMachine = sys.argv[55]
    
                if runMachine == 'true':
                   initialize()
                   time.sleep(3)
                   slowGrab()
                   
                   #re-grip the hands
                   whiteOpen()
                   time.sleep(0.25)
                   whiteClosed()
                   yellowOpen()
                   time.sleep(0.25)
                   yellowClosed()
                   blueOpen()
                   time.sleep(0.25)
                   blueClosed()
                   redOpen()
                   time.sleep(0.25)
                   redClosed()
                   time.sleep(1)
                   
        #           getStartingColours()
    
                   for i in range(0,len(Machine_Sequence)):
                      move = Machine_Sequence[i]
                      if move == 'T+':
                         Tplus()
                      elif move == 'T-':
                         Tminus()
                      elif move == 'F+':
                         Fplus()
                      elif move == 'F-':
                         Fminus()
                      elif move == 'R+':
                         Rplus()
                      elif move == 'R-':
                         Rminus()
                      elif move == 'K+':
                         Kplus()
                      elif move == 'K-':
                         Kminus()
                      elif move == 'L+':
                         Lplus()
                      elif move == 'L-':
                         Lminus()
                      elif move == 'B+':
                         Bplus()
                      elif move == 'B-':
                         Bminus()
                   allOpen()
                   pwm.softwareReset()
            else:
                print "\rCube Not Solved"
                f.write("Cube Not Solved")
    
            f.write("********** LOG CLOSED **********\n\n")
            f.close()
        else:
            print "\rAn incorrect input of the cube colours has been detected"
    else:
        print("\rMissing Calibration File, run calibrate.py first")
       
        
if __name__ == '__main__':
    main()
