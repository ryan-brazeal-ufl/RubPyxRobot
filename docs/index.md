## Welcome to RubpyxRobot Project

An educational STEM open-source project from the [Innovation at Central Collegiate (I2C) Club](https://schools.prairiesouth.ca/centralcollegiate/) in Moose Jaw, Sask.

<table style="border:0px;">
  <tr style="border:0px;">
   <td style="border:0px;"><img width="125px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/I2C.png"></td>
   <td style="border:0px;"><img width="450px" src="https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/images/finish_solve.gif"></td>
  </tr>
</table>

### Build your own Rubik's Cube Solving Machine from 3D printed parts, some servo motors, a Raspberry Pi computer, and some screws.

**3D Model of the Rubik's Cube Machine**
1. Trimble SketchUp - [RubpyxRobot_3D_Model.skp](https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/3D_parts/RubpyxRobot_3D_Model.skp)

**3D Printed Parts List (4 of each, recommended to use different colours for each, 32 total parts)**
1. [bottom_finger.stl](https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/3D_parts/bottom_finger.stl)
2. [top_finger.stl](https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/3D_parts/top_finger.stl)
3. [hand_bottom.stl](https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/3D_parts/hand_bottom.stl)
4. [hand_top.stl](https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/3D_parts/hand_top.stl)
5. [servo_pinion.stl](https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/3D_parts/servo_pinion.stl)
6. [frame.stl](https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/3D_parts/frame.stl)
7. [frame_brace.stl](https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/3D_parts/frame_brace.stl)
8. [frame_brace_w_leg.stl](https://github.com/ryan-brazeal-ufl/RubpyxRobot/raw/master/3D_parts/frame_brace_w_leg.stl)

**Electronics Parts List**
1. Raspberry Pi computer (2B/3B/3B+/4B)
2. microSD card (min. 4GB)
3. [Digital High Torque MG 996R Servo motor](https://www.amazon.ca/MG996R-Torque-Digital-SENHAI-Helicopter/dp/B0716V3WNH/ref=pd_day0_147_3/136-2894002-7736867) (Quanity 8)
4. [Servo wire extensions](https://www.amazon.ca/dp/B07RJSM469/ref=sspa_dk_detail_4)

**Hardware Parts List**
1. Metric 3mm socket cap machine screws ~10mm threaded length
2. Flat top wood screws, total length ~1/2"

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
    5. Install a trimmed servo horn inline with the body of the servo motor.<br>
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
  
