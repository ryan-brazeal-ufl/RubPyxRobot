#!/usr/bin/python

from driver import PWM

# Initialise the PWM device using the default address
pwm = PWM(0x40)
pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
pwm.softwareReset()
