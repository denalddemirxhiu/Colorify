# Colorify
denalddemirxhiu.github.io/Colorify

## November 20th, 2018 (Case Design)

### Designed and laser cut the acrylic top case
Since the ISL29125 sensor mounted on the PCB fits perfectly on the case that came with the Raspberry Pi 3B+, I did not have to design a case from scratch. However I needed to design the top part for the case to completely enclose the sensor without affecting the sensor's ability to obtain readings. The top part of the case was made of acrylic sheets that were laser cut and stacked on top of one another to create a simple clear enclosure. A set of clamps were designed to hold the case in place, but unfortunately due to the Prototype Lab's working hours I couldn't laser cut the clamps.

- The design files for the stacks of acrylic needed to make the top part of the case can be found [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Top%20Case%20Design%20Files.cdr)
- The design files for the clamps to hold the case in place can be found [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Case%20Clamps.cdr)

#### Acrylic Case
![Acrylic Top Case](https://raw.githubusercontent.com/denalddemirxhiu/Colorify/master/Documentation/Acrylic%20Top.png)

![The completed case](https://raw.githubusercontent.com/denalddemirxhiu/Colorify/master/Documentation/Case%20With%20Acrylic%20Top.png)

### Budget Update
There has been no budget update as of this date. This week the top part of the acrylic case was properly designed, laser cut and assembled. Next week the presentations are due and the following weeks the build instructions should be ready. The project budget can be viewed [here](https://github.com/denalddemirxhiu/ify/blob/master/Documentation/Colorify%20Budget.xlsx)

### Project Schedule Update
The schedule has been followed as of this date. The he project schedule can be viewed [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Capstone%20Gantt%20Schedule.mpp)


## November 13th, 2018

### PCB Soldered and Mounted on the board
The PCB was re-designed, updated, printed and then soldered with the stackable headers in the respective places. The PCB was checked for problems with a multimeter, the sensor was checked if it was working with the PCB mounted on the Raspberry PI, and verified that the program worked while the sensor was mounted on the PCB. This can be seen in the following pictures:

![PCB with the Sensor](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/RaspberryPIwithPCB.png?raw=true)

![PCB mounted on the Raspberry Pi](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/SensorMountedOnTheBoard.png?raw=true)

### Sensor Readings and Output
Using Python 3 the sensor readings were obtained and printed on the terminal in RGB format and in HEX format. The colour readings from the sensor are displayed in a window with the respective colour. The sensor readings are not fully accurate because the way that the Red, Green, and Blue photoresistors are placed in the sensor appear to be in a box array where blue and red are always adjacent to each-other, but the green photoresistors are all together. The datasheet also provided this explanation to why the colour readings of the green photoresistors are the most accurate, while the red and blue ones are not always accurate. Furthermore, the sensor is affected by light intensity from direct light coming from a light source. One solution to this might be using an acryllic case that reflects some of the light and lets a portion of the light hit the sensor, but that is not definitive. More research has to be done in that matter. 

The respective pages from the datasheet that display information on this matter are 1, 5, and 15. The datasheet can be viewed [here](https://www.intersil.com/content/dam/Intersil/documents/isl2/isl29125.pdf)

#### Colour samples used
These are colour samples I made to demonstrate the sensor reading colours.

![ColourSamples](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/ColorSamples.png?raw=true)

#### Displaying Color Readings in the Terminal and the Window
![Displaying Colour Readings](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/SampleReadingOutput.png?raw=true)

### Reading the sensor data
To read the sensor data I used the open-source code obtained from [here](https://github.com/bhaskar-anil429/ISL29125/blob/master/ISL29125.py) and modified it to fit my needs. The problem with my sensor was that there was no library to read data from it; the resources from the company that produced the sensor were scarce. The only provided libraries were for Arduino, which are not compatible with the Raspberry PI. Therefore, I used [bhaskar-anil429](https://github.com/bhaskar-anil429)'s source code to work with. I tested the code first and after proving that it worked I made the necessary changes to fit the needs of my project. The program that I designed reads the color values continuously and prints them in a HEX and RGB format, as well as displaying them on another window. The source code for the Python script can be viewed [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/readSensor.py)

### Budget Update
There has been no budget update since I have not ordered any new parts. Everything has been kept track of and reported properly. The project budget can be viewed [here](https://github.com/denalddemirxhiu/ify/blob/master/Documentation/Colorify%20Budget.xlsx)

### Project Schedule Update
The project is going on schedule as of this week. There were some drawbacks last week when trying to solder the designed PCB, but when carefully examining it, the connections were done incorrectly. The PCB was re-designed, updated, printed and then soldered on November 12, 2018. The PCB was checked for problems with a multimeter, the sensor was checked if it was working with the PCB placed on the Raspberry PI and verified that the program worked while the sensor was mounted on the PCB. In the next few weeks, the enclosure of the completed project is due, the presentation needs to be prepared for and the final results of the project need to be made, such as the build instructions. The project schedule can be viewed [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Capstone%20Gantt%20Schedule.mpp)

## November 6th, 2018

### Updated PCB Design
Today the PCB vias were soldered, but when asked for feedback I realized that the connections on the PCB were upside down. The PCB design was updated on the Fritzing file, the files were sent to the prototype lab and they were updated on the Documentation folder in the repository. Below are the pictures of the soldered PCB vias on the improperly designed PCB and the new Updated PCB design:

#### Soldered vias on the improperly designed PCB
![Via Soldered Top](https://raw.githubusercontent.com/denalddemirxhiu/Colorify/master/Documentation/Via_soldered1.png)

![Via Soldered Bottom](https://raw.githubusercontent.com/denalddemirxhiu/Colorify/master/Documentation/Via_soldered2.png)

#### Updated PCB Design
![Updated PCB Design](https://raw.githubusercontent.com/denalddemirxhiu/Colorify/master/Documentation/Updated%20PCB%20Design.png)

### Budget Update
There has been no budget update since I have not ordered any new parts. The project budget can be viewed [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Colorify%20Budget.xlsx)

### Project Schedule Update
As of today we are one week behind on schedule since the PCB was not soldered. The updated design PCB will be soldered by Friday November 9th and be ready by next week. Next week is the Power Up Milestone, therefore there should be a Project Report update and the Raspberry Pi should be reading data from my sensor. The project schedule can be viewed [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Capstone%20Gantt%20Schedule.mpp)

## October 23rd, 2018

### PCB Designed
At this point the PCB design was finished and the gerber files were sent to the Prototype Lab. 
Here are some images displaying the fritzing file work on the breadboard, schematic and PCB design:

#### Breadboard
![Breadboard](https://raw.githubusercontent.com/denalddemirxhiu/Colorify/master/Documentation/ISL29125_breadboard.png)

#### Schematic
![Schematic](https://raw.githubusercontent.com/denalddemirxhiu/Colorify/master/Documentation/ISL29125_Schematic.png)

#### PCB Design
![PCB Design](https://raw.githubusercontent.com/denalddemirxhiu/Colorify/master/Documentation/ISL29125_PCB.png)

### Budget Update
There has been no budget update since I have not ordered any new parts. The project budget can be viewed [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Colorify%20Budget.xlsx)

### Project Schedule Update
According to the project schedule we have completed the PCB design on time therefore we are on schedule. Next week is the PCB soldering Milestone therefore there should be updates next week. The project schedule can be viewed [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Capstone%20Gantt%20Schedule.mpp)

## October 23rd, 2018

### Breadboarding Milestone
  At this point the Raspberry Pi was hooked up to the sensor via jumper wires. Below are the images that provide proof that the Raspberry Pi was connected to the sensor and it recognized the sensor using the i2cdetect command.
  The sensor was connected to the Rasberry Pi using the following pins:  
- PIN 1 (3.3V) - connected to 3.3 V pin in the sensor with an orange jumper wire  
- PIN 3 (SDA1) - connected to SDA pin in the sensor with a blue jumper wire  
- PIN 5 (SCL1) - connected to the SCL pin in the sensor with a brown jumper wire  
- PIN 6 (GND) - connected to the GND pin in the sensor with a black jumper wire  
  
### Sensor Hookup (Breadboard wiring)
  ![Raspberry Pi Breadboard Sensor Hookup](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/RaspberryPi-Sensor-Wired.png?raw=true)
  
### i2cDetect Proof that shows the address of the sensor 0x44
  ![Raspberry Pi i2cdetect proof](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/i2cDetect.png?raw=true)
  
### Project Schedule Update
  We just finished the Breadboarding milestone which shows that based on the project planned schedule I am currently on schedule. For the moment I am working to create the diagram for the PCB in Fritzing which should be completed by next week. As soon as I get the PCB design completed I will send the files to Vlad and Kelly in the Prototype Lab (J233). The project schedule can be viewed [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Capstone%20Gantt%20Schedule.mpp)
  
### Budget Update
  Currently there are no changes to the budget, except for the parts that have arrived. All the parts that I ordered have arrived and I am not planning to buy any extra parts. The project budget can be viewed [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Colorify%20Budget.xlsx) 

### Resources used to wire and connect to the sensor
  - Raspberry Solutions website that shows the pinout of the Raspberry Pi 3B+ can be found [here](https://www.raspberry-solutions.com/connect-sensor-to-raspberry-pi/)  
  - Sparkfun guide that shows the step by step tutorial on how to hookup the ISL29125 sensor can be found [here](https://learn.sparkfun.com/tutorials/isl29125-rgb-light-sensor-hookup-guide/hardware-overview)
  
## October 16th, 2018
### Group Pseudo Code Assignment
  Met with the first year students and helped them write the pseudo code for my third year capstone project. Provided the System UML Diagram which can be viewed [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/System%20UML%20Diagram.pdf)
  
  
## October 9th, 2018

### Reading week holiday
  
## October 2nd, 2018
### Proof of purchase of Raspberry Pi:
  ![Raspberry Pi Proof of Purchase](https://raw.githubusercontent.com/denalddemirxhiu/Colorify/master/Documentation/Raspberry%20Pi%20Proof%20of%20Purchase.png)
  
  
### Proof of purchase of ISL29125 Colour Sensor:
  ![ISL29125 Colour Sensor Proof of Purchase](https://raw.githubusercontent.com/denalddemirxhiu/Colorify/master/Documentation/RBG%20Color%20Sensor%20ISL29125%20Proof%20of%20Purchase.png)
  
## September 25th, 2018
  Provided Budget. Can be viewed [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Colorify%20Budget.xlsx)

## September 18th, 2018
  Compiled and completed Project Schedule. Can be viewed [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Capstone%20Gantt%20Schedule.mpp)
  
## September 11th, 2018 
  Project proposal finished. Can be viewed [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/ProjectProposalDenaldDemirxhiu.xlsx)

## September 4th, 2018

### Repository Created
  Welcome
