## Welcome to RubpyxRobot Project

An educational STEM open-source project from the [Innovation at Central Collegiate (I2C) Club](https://schools.prairiesouth.ca/centralcollegiate/) in Moose Jaw, Sask., Canada.

**Build your own Rubik's Cube Solving Machine from 3D printed parts, servo motors, a Raspberry Pi computer, and some nuts and bolts.**

<table style="border:0px;">
  <tr style="border:0px;">
   <td style="border:0px;"><img width="125px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/I2C.png"></td>
   <td style="border:0px;"><img width="450px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/finish_solve.gif"></td>
  </tr>
</table>

### Getting Started

Though currently not the [fastest Rubik's Cube machine](https://youtu.be/o9hPXDKmV7I) out there (with an average solve time of around 5 mins), it sure is a fun machine to build, play with, and learn from! The entire machine (minus the motors and screws) is built out of 3D printed parts. The parts 'should' be able to be printed on most desktop 3D printers, where the only limitation is if the printer has a printbed that is big enough to accommodate the *frame* part (see below). The 'algorithm' used to generate the sequence of cube turns is a beginner (layers-based) cube solving approach. On average, around 150 individual turns are required to solve any cube, hence it takes the machine a bit of time to perform these individual turns. 

***Below are lists of the components that need to be 3D printed and/or purchased in order to build your very own RubpyxRobot. If you don't have access to a 3D printer, check out [3D Hubs](https://www.3dhubs.com/) to find someone near you who can possibly help with the 3D printing.***

**3D Model of the Rubik's Cube Machine**
1. Trimble SketchUp 2017 - [RubpyxRobot_3D_Model.skp](https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/3D_parts/RubpyxRobot_3D_Model.skp)

**3D Printed Parts List, click on a part to view its 3D model (print 4 of each part, recommended to use different colours for each, 32 total parts)**
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
2. [Adafruit Servo Hat for Raspberry Pi](https://www.adafruit.com/product/2327)
3. microSD card (min. 4GB)
4. [Digital High Torque MG 996R Servo motor](https://www.amazon.ca/MG996R-Torque-Digital-SENHAI-Helicopter/dp/B0716V3WNH/ref=pd_day0_147_3/136-2894002-7736867) (Quanity 8)
5. [Servo wire extensions](https://www.amazon.ca/dp/B07RJSM469/ref=sspa_dk_detail_4)

**Hardware Parts List**
1. Flat top wood screws, total length ~1/2"
2. Metric 3mm socket cap machine screws ~10mm threaded length
3. Metric 3mm nuts (optional)

### Machine Building Instructions ###
1. The Hands
    1. The first 5 3D Parts listed above, 2 servo motors, 2 trimmed servo horns, and some hardware are needed to build a single Hand.<br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2164.jpeg">
    2. Find the counter-clockwise rotation limit.<br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2165.jpeg">
    3. Find the clockwise rotation limit.<br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2166.jpeg">
    4. Estimate the midpoint between the rotation limits.<br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2167.jpeg">
    5. Install a trimmed servo horn inline with the body of the servo motor (you will need to mark the hole locations and carefully drill holes in the servo horn).<br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2168.jpeg">
    6. It's suggested to use some loctite on the servo horn bolt.<br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2169.jpeg">
    7. Twisting servo motor setup is now complete.<br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2170.jpeg">
    8. Position the twisting servo motor on the back-edge of the *hand_bottom* 3D printed part.<br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2171.jpeg">
    9. Use two metric 3mm machine bolts to attach the servo horn to the 3D printed part.<br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2172.jpeg">
   10. Install the other servo horn perpendicular to the long direction of the servo motor body, then set the servo horn bolt (don't forget the loctite).<br>
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
   17. The 1 dot on the *servo_pinion* part must align with the 2 dots in the *bottom_finger* part. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2180.jpeg">
   18. Install the *top_finger* 3D printed part on the upper post of the *hand_bottom* part. The *top_finger's* last gear cog must be on the OUTSIDE of the *bottom_finger's* last gear cog (pay close attention to the following image).<br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2181.jpeg">
   19. Install the *hand_top* 3D printed part onto the rest of the Hand assembly, align the holes with the posts and the servo pinion.<br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2182.jpeg">
   20. Use three 1/2" flat top wood screws to secure the *hand_top* part to the *hand_bottom* part.<br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2183.jpeg">
   21. An assembled Hand.<br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2184.jpeg">
   22. Gently open the fingers of the hand and install a soft pad on each 'fingertip' (foam or cork works well).<br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2185.jpeg">
   23. Repeat this process three more times in order to assemble all 4 Hands.<br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2186.jpeg">
2. Frame
    1. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2187.jpeg">
    2. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2188.jpeg">
    3. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2189.jpeg">
    4. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2190.jpeg">
    5. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2191.jpeg">
    6. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2192.jpeg">
    7. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2193.jpeg">
    8. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2194.jpeg">
    9. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2195.jpeg">
   10. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2196.jpeg">
   11. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2197.jpeg">
   12. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2198.jpeg">
   13. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2199.jpeg">
   14. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2200.jpeg">
   15. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2201.jpeg">
   16. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2202.jpeg">
   17. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2203.jpeg">
   18. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2204.jpeg">
   19. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2205.jpeg">
   20. <br>
       <img width="500px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/IMG_2208.jpeg">
    
