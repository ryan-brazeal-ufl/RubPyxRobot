# Welcome to RubpyxRobot Project

An educational STEM open-source project from the [Innovation at Central Collegiate (I2C) Club](https://schools.prairiesouth.ca/centralcollegiate/) in Moose Jaw, Sask., Canada.

**Build your own Rubik's Cube Solving Machine from 3D printed parts, servo motors, a Raspberry Pi computer, and some nuts and bolts.**

<table style="border:0px;">
  <tr style="border:0px;">
   <td style="border:0px;"><img width="125px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/I2C.png"></td>
   <td style="border:0px;"><img width="450px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/finish_solve.gif"></td>
  </tr>
</table>

## 1. Getting Started

Though currently not the [fastest Rubik's Cube solving machine](https://youtu.be/o9hPXDKmV7I) out there (with an average solve time of around 5 mins), it sure is a fun machine to build, play with, program, and learn from! The entire machine (minus the motors and screws) is built out of 3D printed parts. The parts should be able to be printed on most desktop 3D printers, where the only limitation is if the printer has a printbed that is big enough to accommodate the *frame* part (see below). The 'algorithm' used to generate the sequence of cube turns is a beginner (layers-based) cube solving approach. On average, around 150 individual turns are required to solve any cube, hence it takes the machine a bit of time to perform these individual turns. 

***Below are lists of the components that need to be 3D printed and/or purchased in order to build your very own RubpyxRobot. If you don't have access to a 3D printer, check out [3D Hubs](https://www.3dhubs.com/) to find someone near you who can possibly help with the 3D printing.***

These instructions make use of a standard computer (Windows, Mac, Linux) and a cabled ethernet network (created using an inexpensive network router) to remote login to the Raspberry Pi computer and operate the RubpyxRobot. However, if a keyboard, mouse, and monitor are plugged directly into the Raspberry Pi computer, it can be logged into directly. **This is a potentially confusing part of the current project, but don't be alarmed as it's easily overcome with a little bit of reading and practice!**

**3D Model of the Rubik's Cube Machine**
1. Trimble SketchUp 2017 - [RubpyxRobot_3D_Model.skp](https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/3D_parts/RubpyxRobot_3D_Model.skp)

**3D Printed Parts List, click on a part to view its 3D model (print four of each part, recommended to use different colours for each, 32 total parts)**
1. [bottom_finger.stl](https://github.com/ryan-brazeal-ufl/RubpyxRobot/blob/master/3D_parts/bottom_finger.stl)
2. [top_finger.stl](https://github.com/ryan-brazeal-ufl/RubpyxRobot/blob/master/3D_parts/top_finger.stl)
3. [hand_bottom.stl](https://github.com/ryan-brazeal-ufl/RubpyxRobot/blob/master/3D_parts/hand_bottom.stl) - print with supports
4. [hand_top.stl](https://github.com/ryan-brazeal-ufl/RubpyxRobot/blob/master/3D_parts/hand_top.stl) - rotate the part 180 deg. about its X (or Y) axis before printing
5. [servo_pinion.stl](https://github.com/ryan-brazeal-ufl/RubpyxRobot/blob/master/3D_parts/servo_pinion.stl) - print with supports
6. [frame.stl](https://github.com/ryan-brazeal-ufl/RubpyxRobot/blob/master/3D_parts/frame.stl)
7. [frame_brace.stl](https://github.com/ryan-brazeal-ufl/RubpyxRobot/blob/master/3D_parts/frame_brace.stl)
8. [frame_brace_w_leg.stl](https://github.com/ryan-brazeal-ufl/RubpyxRobot/blob/master/3D_parts/frame_brace_w_leg.stl)
9. [DOWNLOAD ALL 3D PARTS (.zip archive)](https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/3D_parts/RubpyxRobot_3D_parts.zip)

**Electronics Parts List**
1. Raspberry Pi computer (2B/3B/3B+/4B)
2. microSD card (min. 4GB)
3. [Adafruit Servo Hat for Raspberry Pi](https://www.adafruit.com/product/2327)
4. [5 Volt power supply (5-10 Amps) with a 5.5mm plug connector](https://www.amazon.ca/BTF-LIGHTING-Plastic-Adapter-Transformer-WS2812B/dp/B01D8FM71S/ref=sr_1_7)
5. [Digital High Torque MG 996R Servo motor](https://www.amazon.ca/MG996R-Torque-Digital-SENHAI-Helicopter/dp/B0716V3WNH/ref=pd_day0_147_3/136-2894002-7736867) (Quanity 8)
6. [Servo wire extensions](https://www.amazon.ca/dp/B07RJSM469/ref=sspa_dk_detail_4)

**Miscellaneous Parts List**
1. Flat top wood screws, total length ~1/2"
2. Metric 3mm socket cap machine screws ~10mm threaded length
3. Metric 3mm nuts (optional)
4. Plastic zip-ties (optional)

## 2. Building the Machine

### i. Assembling the Hands

 1. The first five 3D printed parts listed above, two servo motors, two trimmed servo horns, and some hardware are needed to build a single Hand.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2164.jpeg">
 2. Find the counter-clockwise rotation limit.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2165.jpeg">
 3. Find the clockwise rotation limit.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2166.jpeg">
 4. Estimate the midpoint between the rotation limits.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2167.jpeg">
 5. Install a trimmed servo horn inline with the body of the servo motor (you will need to mark the hole locations and carefully drill holes in the servo horn). If your servo motors come with metal servo motor horns, it is strongly recommended to use them! Though trimming and drilling holes though the metal horns will require more work to complete, it is definitely worth the effort.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2168.jpeg">
 6. It's suggested to use some loctite on the servo horn bolt.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2169.jpeg">
 7. Twisting servo motor setup is now complete.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2170.jpeg">
 8. Position the twisting servo motor on the back-edge of the *hand_bottom* 3D printed part.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2171.jpeg">
 9. Use two metric 3mm machine bolts to attach the servo horn to the 3D printed part (if needed, nuts can be installed on the protruding bolts).<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2172.jpeg">
 10. Repeat steps 2-4 and then install the other servo horn perpendicular to the long direction of the servo motor body, then tighten the servo horn bolt (don't forget the loctite).<br>
     <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2173.jpeg">
 11. Position the *servo_pinion* 3D printed part on the servo horn so the part's notch is at the top.<br>
     <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2174.jpeg">
 12. Use two metric 3mm machine bolts to attach the servo horn to the *servo_pinion* 3D printed part.<br>
     <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2175.jpeg">
 13. Install the servo pinion (and servo motor) through the bottom-side of the *hand_bottom* 3D printed part.<br>
     <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2176.jpeg">
 14. Align the four holes in the mounting tabs on the servo motor with the pilot holes in the *hand_bottom* 3D printed part.<br>
     <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2177.jpeg">
 15. Use the four included metal screws to install the clamping servo motor.<br>
     <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2178.jpeg">
 16. Install the *bottom_finger* 3D printed part on the lower post of the *hand_bottom* part, see the next step for alignment information.<br>
     <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2179.jpeg">
 17. The single 'dot' on the *servo_pinion* part must be aligned between the double 'dots' on the *bottom_finger* part. <br>
     <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2180.jpeg">
 18. Install the *top_finger* 3D printed part on the upper post of the *hand_bottom* part. The *top_finger's* last gear cog must be on the OUTSIDE of the *bottom_finger's* last gear cog (pay close attention to the following image).<br>
     <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2181.jpeg">
 19. Install the *hand_top* 3D printed part onto the rest of the Hand assembly, align the holes with the posts and the servo pinion.<br>
     <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2182.jpeg">
 20. Use three 1/2" flat top wood screws to secure the *hand_top* part to the *hand_bottom* part.<br>
     <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2183.jpeg">
 21. An assembled Hand.<br>
     <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2184.jpeg">
 22. Gently open the fingers of the hand to check that they can fully open and then gently close the fingers to check that they can fully close. If the fingers do not fully open or fully close, then the position of the servo horn on the servo motor shaft needs to be adjusted. Lastly, install a soft pad on each 'fingertip' (foam or cork works well).<br>
     <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2185.jpeg">
 23. Repeat this process three more times in order to assemble all four Hands.<br>
     <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2186.jpeg">
     
### ii. Assembling the Frame

 1. The last three 3D printed parts listed above (four of each) and 24 wood screws are needed to build the Frame. It is recommended to put small foam pads on the bottom of each of the *frame_brace_w_leg* parts to help the RubpyxRobot remain rigid while in operation.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2187.jpeg">
 2. The rectangular servo hole in the *frame* 3D printed part is closer to the 'top' edge of part, so ensure all four parts are orientated the correct way. The *frame* parts are designed to interconnect and use two wood screws to secure them together at one of the outside edges.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2188.jpeg">
 3. The Frame interconnect at the outside edges only (notice the rectangular servo holes are closer to the top edge).<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2189.jpeg">
 4. Flip the Frame upside so it is laying on its top edge. Install the four *frame_brace* parts at each of the inside corners using two wood screws for each.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2190.jpeg">
 5. Install the four *frame_brace_w_leg* parts on the bottom inside corners of the Frame using two wood screws<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2191.jpeg">
    
### iii. Installing the Hands in the Frame
    
 1. Run the twisting servo motor's cable through the rectangular hole in the Frame and then carefully insert the servo motor's body through the hole. The cable needs to be on the top edge.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2192.jpeg">
 2. Push the servo motor into the Frame until the servo motor's four mounting holes align with the four pilot holes in the Frame.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2193.jpeg">
 3. Rotate the Hand about 90 deg. and then **carefully and slowly** tighten the top two servo mounting screws. Having a screwdriver with a longer shaft can help get a better angle for tightening the screws (be careful as the screws can easily become stripped).<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2194.jpeg">
 4. Rotate the Hand about 180 deg. from its current position and then **carefully and slowly** tighten the bottom two servo mounting screws.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2195.jpeg">
 5. Repeat steps 1-4 three more times in order to install all four Hands within the Frame. The RubpyxRobot software (discussed in an upcoming section) references the Hands by the colours (i.e., white, blue, yellow, and red). Regardless of the colour(s) you used to printed the Hands, the software always references the white and yellow Hands as being on opposite sides of the Frame, and likewise for the blue and red hands. In hindsight, the software should have used more generic Hand 1, 2, 3, and 4 object names.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2197.jpeg">
    
### iv. Connecting the servo motors to the Raspberry Pi
    
 1. Optionally, the Raspberry Pi computer can be mounted to the Frame at any one of the top corners. Notice that there are NO pilot holes within the Frame for mounting the Raspberry Pi computer, but using the 1/2" wood screws it is possible to easily secure the computer to the Frame.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2199.jpeg">
 2. Install the Adafruit Servo Hat onto the GPIO pins on the Raspberry Pi. It is likely that the Servo Hat will first need to be assembled by soldering the 40-pin header and the sixteen 3-pin servo motor connectors to the Hat (see the [Adafruit Tutorial](https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/) for more information). Notice, the following image shows a micro-USB cable soldered to the Servo Hat's GND and +5 solder pads and used to provide power to the Raspberry Pi 3B computer, this is an optional step as the Raspberry Pi can simply be powered using its own 5V power supply.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2200.jpeg">
 3. Depending on where the Raspberry Pi computer is mounted (or positioned beside the RubpyxRobot), servo wire extensions may need to be used to have the eight servo motors all connect to the Servo Hat. If the computer is mounted to the top edge of the Frame, it is recommended to use plastic zip-ties to hold the servo motor wires in place **(be careful not to tighten the zip-ties too much as you risk damaging/shorting the wires).**<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2201.jpeg">
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2203.jpeg">
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2205.jpeg">
 4. The servo motors are connected to the 3-pin servo connectors numbered 0-7 on the Adafruit Servo Hat, as follows:<br>
    a. white clamping servo to connector 0<br>
    b. white twisting servo to connector 1<br>
    c. blue clamping servo to connector 2<br>
    d. blue twisting servo to connector 3<br>
    e. yellow clamping servo to connector 4<br>
    f. yellow twisting servo to connector 5<br>
    g. red clamping servo to connector 6<br>
    h. red twisting servo to connector 7<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2210.jpeg">
 5. Congratulations, your RubpyxRobot is now fully assembled!!<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2208.jpeg">
  
## 3. Setting up the Raspberry Pi computer

### i. Installing the Raspberry Pi OS on a microSD card

 1. Download the latest [Raspberry Pi OS with Desktop image file](https://www.raspberrypi.org/downloads/raspberry-pi-os/) to a standard computer.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/raspberrypiOS.png">
 2. Write the Raspberry Pi OS image to the microSD card using either the [Raspberry Pi Imager software](https://www.raspberrypi.org/downloads/) or another suitable image file writing software (e.g., Apple Pi Baker for Mac).<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/ApplePi-Baker.png">
 3. Insert the microSD card back into the standard computer and follow these [instructions](https://linuxize.com/post/how-to-enable-ssh-on-raspberry-pi/) to enable a remote computer to login to the Raspberry Pi (this type of connection utilizes what is called a Secure Shell, SSH).<br> 
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/add_ssh_file.png">
 4. Install the microSD card into the Raspberry Pi computer, attach a network cable to the Raspberry Pi's ethernet jack and ensure it is connected to the same network as the one being used by the standard computer. Power up the Raspberry Pi computer and the Adafruit Servo Hat using a high current 5V power supply. Using the standard computer, open a command line window or terminal window and run the command `ping raspberrypi`. Hopefully the IP address of the Raspberry Pi computer should be returned to the window (in this example the returned IP address is 192.168.1.124).<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/ping_IP.png">
 5. If you are using a standard computer running Microsoft Windows, download and install the [Putty SSH client](https://www.putty.org/) and remote login to the Raspberry Pi computer at the IP address discovered in the previous step. For a standard computer running Mac OS or a Linux distro, open a terminal window and run the following command, `ssh pi@192.168.1.124` (use your specific IP address instead). **The default username/password for a Raspberry Pi computer is:** ***pi/raspberry***. If everything connects properly you should see a command line prompt as shown in the following image.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/ssh_login.png">
 6. The following steps need to be performed in order for the Raspberry Pi computer to have control over the servo motors. On the Raspberry Pi command prompt, run the command `sudo raspi-config` and the dialog shown below will appear. Using the down arrow on the keyboard, highlight the *Interfacing Options* line and press Enter.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/raspi_config1.png">
 7. Select the *I2C* line and press Enter.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/raspi_config2.png">
 8. Select the *Yes* option and press Enter.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/raspi_config3.png">
 9. A confirmation message should appear, press Enter to return to the main menu.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/raspi_config4.png">
10. Press the tab key on the keyboard and then select *Finish* and press Enter. You should now be back at the Raspberry Pi's command prompt.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/raspi_config5.png">
11. Run the command `sudo i2cdetect -y 1` and you should see a table-like message returned to the screen, as shown in the following image. This indicates that the Raspberry Pi computer has detected the Adafruit Servo Hat and servo control will now work properly.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/rpi_enable_i2c.png">
    
### ii. Installing the RubpyxRobot Python scripts

 1. On the Raspberry Pi command prompt, run the command <br> `wget https://github.com/ryan-brazeal-ufl/RubpyxRobot/archive/py.zip`<br>**This step requires that the Raspberry Pi (via the network it is on) is connected to the internet.**<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/wget_command.png">
 2. Next, run the command <br>`unzip py.zip && mv RubpyxRobot-py RubpyxRobot`<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/unzip_command.png">
 3. The RubpyxRobot Python scripts have now been downloaded to a directory within the pi user's home directory. Navigate into RubpyxRobot directory to access the Python scripts that control the machine by running the command `cd RubpyxRobot`<br> Followed by the command `chmod +x *.py`<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/scripts.png">
 4. The RubpyxRobot is now ready to be calibrated!
 
## 4. Calibrating the RubpyxRobot

**Please read ALL of the following instructions BEFORE beginning the calibration process!**

The final step before the RubpyxRobot can solve its first Rubik's Cube, is that the Hands of the machine need to be calibrated. Specifically for each of the Hands, the Fingers need to be calibrated to know when they are grabbing the cube (**closed**) or when they are not (**opened**), as well as the Wrist needs to be calibrated to know when it is rotated to the left (**counter-clockwise/CCW**), the right (**clockwise/CW**), or in the middle (**neutral**). Each of these **5 states** is recorded as a number and stored inside the *calibration.txt* file inside the RubpyxRobot directory on the Raspberry Pi. Rather than editting the *calibration.txt* file directly, a Python calibration script is provided that allows you to easily determine these calibration numbers by manually operating one Hand of the RubpyxRobot machine at a time, and maneuvering each Hand into its 5 states.
 
**IMPORTANT**

 - **The calibration procedure can be performed as often as you would like, and should be performed whenever the RubpyxRobot doesn't appear to be operating smoothly.**
 - **The calibration procedure can be used to calibrate a single state for a single Hand or for all five states for all four Hands. At any time during the calibration procedure you can press the 'Esc' key to end the procedure.**
 
 The following instructions explain how to calibrate all 5 states for all 4 hands:
 
 1. Navigate to the RubpyxRobot directory by running the command `cd ~/RubpyxRobot`<br>This command will **ALWAYS** navigate you to the RubpyxRobot directory regardless of the current directory you are in on the Raspberry Pi.
 2. Run the command `./calibrate.py`<br>This will start the calibration Python script and a message will be displayed to the screen as shown below.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/calibration1.png">
 3. When the calibration script first starts, the white Hand (though your's might be a different colour) is activated by default. To change control to a different Hand, press the '1', '2', '3', or '4' key on your keyboard. A message will be displayed indicating which Hand is now being controlled.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/calibration2.png">
 4. Begin by maneuvering each of the Hands into its **neutral state**. Press the '1' key, followed by pressing and holding the 'A' key. The white Hand should begin to rotate counter-clockwise (when viewed from behind). **How COOL is that!** Press and hold the 'D' key and the white Hand should begin to rotate clockwise. Use the 'A' and 'D' keys to position the Hand so its Fingers are straight up and down (**neutral state**) and then press the 'G' key to save this position. A message will appear on screen indicating that the position has been saved. Repeat this process three more time, once for each Hand. **Very important, finish this step by pressing the 'spacebar' key, which writes the saved positions to the *calibration.txt* file**.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/calibration3.png">
 5. Next, maneuver each of the Hands into its **opened state**. Press the '1' key, followed by pressing and holding the 'W' key. The Fingers on the white Hand should begin to open. When the Fingers are in the desired opened state, press the 'T' key to save this position. A message will appear on screen indicating that the position has been saved. Repeat this process three more times, once for each Hand. Finish this step by pressing the 'spacebar' key.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/calibration4.png">
 6. With the Fingers of the Hands now all open, place a standard-sized Rubik's Cube into the middle of the RubpyxRobot. Press and hold the 'X' key and the Fingers on the white Hand should begin to close. When the Fingers are in the desired closed state, press the 'B' key to save this position. A message will appear on screen indicating that the position has been saved. Repeat this process three more times, once for each Hand. Finish this step by pressing the 'spacebar' key.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/calibration5.png">
 7. Next, maneuver each of the Hands into its **CCW state**. Press the '1' key, followed by pressing and holding the 'A' key. The white Hand should begin to rotate counter-clockwise. When the Cube appears to be rotated exactly 1 turn counter-clockwise, press the 'F' key to save this position. A message will appear on screen indicating that the position has been saved. Before repeating this process three more times, once for each Hand, the current Hand needs to be positioned back into its **neutral state**, press and hold the 'D' key until the Cube goes back into its **neutral** position. Finish this step by pressing the 'spacebar' key.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/calibration6.png">
 8. Next, maneuver each of the Hands into its **CW state**. Press the '1' key, followed by pressing and holding the 'D' key. The white Hand should begin to rotate clockwise. When the Cube appears to be rotated exactly 1 turn clockwise, press the 'H' key to save this position. A message will appear on screen indicating that the position has been saved. Before repeating this process three more times, once for each Hand, the current Hand needs to be positioned back into its **neutral state**, press and hold the 'A' key until the Cube goes back into its **neutral** position. Finish this step by pressing the 'spacebar' key.<br>
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/calibration7.png">
 9. Before ending the calibration procedure you should check the saved states for each Hand. To recall the saved calibrated states for each Hand, the following keyboard keys can be used:<br>
    a. 'K' key recalls the **neutral** state.<br>
    b. 'I' key recalls the **opened** state.<br>
    c. 'comma' key recalls the **closed** state.<br>
    d. 'J' key recalls the **CCW** state.<br>
    e. 'L' key recalls the **CW** state.<br>
    **Be careful NOT to rotate a Hand while the Fingers are in the opened state!**<br><br>
    The following image highlights the keyboard keys used in the calibration process. The red coloured keys are used to manually maneuver the Fingers and Wrist of a Hand. The green coloured keys are used to save the current Fingers or Wrist state. The blue coloured keys are used to quickly recall the saved calibration states. The orange coloured keys are for writing the calibration values to the *calibration.txt* file (spacebar) or ending the calibration procedure (Esc). The yellow coloured keys are for changing control of the Hands.
    <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/calibration_keyboard.jpg">
