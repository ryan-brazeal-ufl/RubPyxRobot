#!/usr/bin/python

# RubpyxRobot Calibration Script
# By: Ryan Brazeal (and the I2C Club)
# Date: Started - Circa 2017


from driver import PWM
import tty
import sys
import os
import termios


if __name__ == "__main__":
    
    orig_settings = termios.tcgetattr(sys.stdin)
    tty.setraw(sys.stdin)
    
    # Initialise the PWM device using the default address
    pwm = PWM(0x40)
    # Set frequency to 60 Hz
    pwm.setPWMFreq(60)
    
    #Hardware Definition Parameters 
    white_clamp = 0
    white_twist = 1
    blue_clamp = 2
    blue_twist = 3
    yellow_clamp = 4
    yellow_twist = 5
    red_clamp = 6
    red_twist = 7
    
    #Calibration Parameters
    white_clamp_closed = 350
    white_clamp_open = 350
    white_twist_neutral = 350
    white_twist_ccw = 350
    white_twist_cw = 350
    blue_clamp_closed = 350
    blue_clamp_open = 350
    blue_twist_neutral = 350
    blue_twist_ccw = 350
    blue_twist_cw = 350
    yellow_clamp_closed = 350
    yellow_clamp_open = 350
    yellow_twist_neutral = 350
    yellow_twist_ccw = 350
    yellow_twist_cw = 350
    red_clamp_closed = 350
    red_clamp_open = 350
    red_twist_neutral = 350
    red_twist_ccw = 350
    red_twist_cw = 350
    
    params = []
    if os.path.isfile("calibration.txt"):
        with open("calibration.txt",'r') as cal_params:
            for param in cal_params:
                params.append(int(param.strip('\n')))
    
        if len(params) == 20:
            white_clamp_closed = params[0]
            white_clamp_open = params[1]
            white_twist_neutral = params[2]
            white_twist_ccw = params[3]
            white_twist_cw = params[4]
            blue_clamp_closed = params[5]
            blue_clamp_open = params[6]
            blue_twist_neutral = params[7]
            blue_twist_ccw = params[8]
            blue_twist_cw = params[9]
            yellow_clamp_closed = params[10]
            yellow_clamp_open = params[11]
            yellow_twist_neutral = params[12]
            yellow_twist_ccw = params[13]
            yellow_twist_cw = params[14]
            red_clamp_closed = params[15]
            red_clamp_open = params[16]
            red_twist_neutral = params[17]
            red_twist_ccw = params[18]
            red_twist_cw = params[19]
    
    #control parameters
    input_key = 0
    latest_white_clamp_value = white_clamp_closed
    latest_white_twist_value = white_twist_neutral
    latest_blue_clamp_value = blue_clamp_closed
    latest_blue_twist_value = blue_twist_neutral
    latest_yellow_clamp_value = yellow_clamp_closed
    latest_yellow_twist_value = yellow_twist_neutral
    latest_red_clamp_value = red_clamp_closed
    latest_red_twist_value = red_twist_neutral

    current_clamp = white_clamp
    current_twist = white_twist
    current_clamp_value = latest_white_clamp_value
    current_twist_value = latest_white_twist_value

    print("\n\rStarting command and calibration loop, press Esc to end")
    count = 0
    while input_key != chr(27):
        input_key = sys.stdin.read(1)
            
        if input_key == '1':
            current_clamp = white_clamp
            current_twist = white_twist
            current_clamp_value = latest_white_clamp_value
            current_twist_value = latest_white_twist_value
            print("\rControl changed to White")
            
        elif input_key == '2':
            current_clamp = blue_clamp
            current_twist = blue_twist
            current_clamp_value = latest_blue_clamp_value
            current_twist_value = latest_blue_twist_value
            print("\rControl changed to Blue")

        elif input_key == '3':
            current_clamp = yellow_clamp
            current_twist = yellow_twist
            current_clamp_value = latest_yellow_clamp_value
            current_twist_value = latest_yellow_twist_value
            print("\rControl changed to Yellow")

        elif input_key == '4':
            current_clamp = red_clamp
            current_twist = red_twist
            current_clamp_value = latest_red_clamp_value
            current_twist_value = latest_red_twist_value            
            print("\rControl changed to Red")
            
        #movement commands
        elif input_key == 'a':
            current_twist_value -= 2
            pwm.setPWM(current_twist,0,current_twist_value)
            
        elif input_key == 'd':
            current_twist_value += 2
            pwm.setPWM(current_twist,0,current_twist_value)
        
        elif input_key == 'x':
            current_clamp_value -= 2
            pwm.setPWM(current_clamp,0,current_clamp_value)
            
        elif input_key == 'w':
            current_clamp_value += 2
            pwm.setPWM(current_clamp,0,current_clamp_value)

        elif input_key == 'f':
            if current_twist == 1:
                white_twist_ccw = current_twist_value
                print("\rWhite CCW set to " + str(white_twist_ccw))
            elif current_twist == 3:
                blue_twist_ccw = current_twist_value
                print("\rBlue CCW set to " + str(blue_twist_ccw))
            elif current_twist == 5:
                yellow_twist_ccw = current_twist_value
                print("\rYellow CCW set to " + str(yellow_twist_ccw))
            elif current_twist == 7:
                red_twist_ccw = current_twist_value
                print("\rRed CCW set to " + str(red_twist_ccw))
    
        elif input_key == 'h':
            if current_twist == 1:
                white_twist_cw = current_twist_value
                print("\rWhite CW set to " + str(white_twist_cw))
            elif current_twist == 3:
                blue_twist_cw = current_twist_value
                print("\rBlue CW set to " + str(blue_twist_cw))
            elif current_twist == 5:
                yellow_twist_cw = current_twist_value
                print("\rYellow CW set to " + str(yellow_twist_cw))
            elif current_twist == 7:
                red_twist_cw = current_twist_value
                print("\rRed CW set to " + str(red_twist_cw))
            
        elif input_key == 't':
            if current_clamp == 0:
                white_clamp_open = current_clamp_value
                print("\rWhite Open set to " + str(white_clamp_open))
            elif current_clamp == 2:
                blue_clamp_open = current_clamp_value
                print("\rBlue Open set to " + str(blue_clamp_open))
            elif current_clamp == 4:
                yellow_clamp_open = current_clamp_value
                print("\rYellow Open set to " + str(yellow_clamp_open))
            elif current_clamp == 6:
                red_clamp_open = current_clamp_value
                print("\rRed Open set to " + str(red_clamp_open))
                
        elif input_key == 'b':
            if current_clamp == 0:
                white_clamp_closed = current_clamp_value
                print("\rWhite Closed set to " + str(white_clamp_closed))
            elif current_clamp == 2:
                blue_clamp_closed = current_clamp_value
                print("\rBlue Closed set to " + str(blue_clamp_closed))
            elif current_clamp == 4:
                yellow_clamp_closed = current_clamp_value
                print("\rYellow Closed set to " + str(yellow_clamp_closed))
            elif current_clamp == 6:
                red_clamp_closed = current_clamp_value
                print("\rRed Closed set to " + str(red_clamp_closed))
    
        elif input_key == 'g':
            if current_twist == 1:
                white_twist_neutral = current_twist_value
                print("\rWhite Neutral set to " + str(white_twist_neutral))
            elif current_twist == 3:
                blue_twist_neutral = current_twist_value
                print("\rBlue Neutral set to " + str(blue_twist_neutral))
            elif current_twist == 5:
                yellow_twist_neutral = current_twist_value
                print("\rYellow Neutral set to " + str(yellow_twist_neutral))
            elif current_twist == 7:
                red_twist_neutral = current_twist_value
                print("\rRed Neutral set to " + str(red_twist_neutral))
                
        elif input_key == 'j':
            if current_twist == 1:
                pwm.setPWM(current_twist,0,white_twist_ccw)
                current_twist_value = white_twist_ccw
            elif current_twist == 3:
                pwm.setPWM(current_twist,0,blue_twist_ccw)
                current_twist_value = blue_twist_ccw
            elif current_twist == 5:
                pwm.setPWM(current_twist,0,yellow_twist_ccw)
                current_twist_value = yellow_twist_ccw
            elif current_twist == 7:
                pwm.setPWM(current_twist,0,red_twist_ccw)
                current_twist_value = red_twist_ccw
                
        elif input_key == 'l':
            if current_twist == 1:
                pwm.setPWM(current_twist,0,white_twist_cw)
                current_twist_value = white_twist_cw
            elif current_twist == 3:
                pwm.setPWM(current_twist,0,blue_twist_cw)
                current_twist_value = blue_twist_cw
            elif current_twist == 5:
                pwm.setPWM(current_twist,0,yellow_twist_cw)
                current_twist_value = yellow_twist_cw
            elif current_twist == 7:
                pwm.setPWM(current_twist,0,red_twist_cw)
                current_twist_value = red_twist_cw
                
        elif input_key == 'i':
            if current_clamp == 0:
                pwm.setPWM(current_clamp,0,white_clamp_open)
                current_clamp_value = white_clamp_open
            elif current_clamp == 2:
                pwm.setPWM(current_clamp,0,blue_clamp_open)
                current_clamp_value = blue_clamp_open
            elif current_clamp == 4:
                pwm.setPWM(current_clamp,0,yellow_clamp_open)
                current_clamp_value = yellow_clamp_open
            elif current_clamp == 6:
                pwm.setPWM(current_clamp,0,red_clamp_open)
                current_clamp_value = red_clamp_open
                
        elif input_key == ',':
            if current_clamp == 0:
                pwm.setPWM(current_clamp,0,white_clamp_closed)
                current_clamp_value = white_clamp_closed
            elif current_clamp == 2:
                pwm.setPWM(current_clamp,0,blue_clamp_closed)
                current_clamp_value = blue_clamp_closed
            elif current_clamp == 4:
                pwm.setPWM(current_clamp,0,yellow_clamp_closed)
                current_clamp_value = yellow_clamp_closed
            elif current_clamp == 6:
                pwm.setPWM(current_clamp,0,red_clamp_closed)
                current_clamp_value = red_clamp_closed
                
        elif input_key == 'k':
            if current_twist == 1:
                pwm.setPWM(current_twist,0,white_twist_neutral)
                current_twist_value = white_twist_neutral
            elif current_twist == 3:
                pwm.setPWM(current_twist,0,blue_twist_neutral)
                current_twist_value = blue_twist_neutral
            elif current_twist == 5:
                pwm.setPWM(current_twist,0,yellow_twist_neutral)
                current_twist_value = yellow_twist_neutral
            elif current_twist == 7:
                pwm.setPWM(current_twist,0,red_twist_neutral)
                current_twist_value = red_twist_neutral
            
        #spacebar press (saves calibration parameters to file)
        elif input_key == chr(32):
            with open("calibration.txt",'w') as cal_file:
                cal_file.write(str(white_clamp_closed) + "\n")
                cal_file.write(str(white_clamp_open) + "\n")
                cal_file.write(str(white_twist_neutral) + "\n")
                cal_file.write(str(white_twist_ccw) + "\n")
                cal_file.write(str(white_twist_cw) + "\n")
                cal_file.write(str(blue_clamp_closed) + "\n")
                cal_file.write(str(blue_clamp_open) + "\n")
                cal_file.write(str(blue_twist_neutral) + "\n")
                cal_file.write(str(blue_twist_ccw) + "\n")
                cal_file.write(str(blue_twist_cw) + "\n")
                cal_file.write(str(yellow_clamp_closed) + "\n")
                cal_file.write(str(yellow_clamp_open) + "\n")
                cal_file.write(str(yellow_twist_neutral) + "\n")
                cal_file.write(str(yellow_twist_ccw) + "\n")
                cal_file.write(str(yellow_twist_cw) + "\n")
                cal_file.write(str(red_clamp_closed) + "\n")
                cal_file.write(str(red_clamp_open) + "\n")
                cal_file.write(str(red_twist_neutral) + "\n")
                cal_file.write(str(red_twist_ccw) + "\n")
                cal_file.write(str(red_twist_cw) + "\n")
            print("\rParameters have to written to the calibration.txt file")
            
            
    #Just before exiting the script, the calibration parameters are printed to the screen
    print("\rWhite Closed : " + str(white_clamp_closed))
    print("\rWhite Open : " + str(white_clamp_open))
    print("\rWhite Neutral : " + str(white_twist_neutral))
    print("\rWhite CCW : " + str(white_twist_ccw))
    print("\rWhite CW : " + str(white_twist_cw))
    print("\rBlue Closed : " + str(blue_clamp_closed))
    print("\rBlue Open : " + str(blue_clamp_open))
    print("\rBlue Neutral : " + str(blue_twist_neutral))
    print("\rBlue CCW : " + str(blue_twist_ccw))
    print("\rBlue CW : " + str(blue_twist_cw))
    print("\rYellow Closed : " + str(yellow_clamp_closed))
    print("\rYellow Open : " + str(yellow_clamp_open))
    print("\rYellow Neutral : " + str(yellow_twist_neutral))
    print("\rYellow CCW : " + str(yellow_twist_ccw))
    print("\rYellow CW : " + str(yellow_twist_cw))
    print("\rRed Closed : " + str(red_clamp_closed))
    print("\rRed Open : " + str(red_clamp_open))
    print("\rRed Neutral : " + str(red_twist_neutral))
    print("\rRed CCW : " + str(red_twist_ccw))
    print("\rRed CW : " + str(red_twist_cw))
    
    
    
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings) 
    pwm.softwareReset()    
