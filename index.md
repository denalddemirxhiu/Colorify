# Colorify
denalddemirxhiu.github.io/Colorify

## November 13th, 2018

### PCB Soldered and Mounted on the board
The PCB was re-designed, updated, printed and then soldered with the stackable headers in the respective places. The PCB was checked for problems with a multimeter, the sensor was checked if it was working with the PCB mounted on the Raspberry PI and verified that the program worked while the sensor was mounted on the PCB. This can be seen in the following pictures:

![PCB with the Sensor](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/RaspberryPIwithPCB.png?raw=true)

![PCB mounted on the Raspberry Pi](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/SensorMountedOnTheBoard.png?raw=true)

### Sensor Readings and Output
Using Python 3 the sensor readings were obtained and printed on the terminal in RGB format and in HEX format. The colour reading from the sensor was displayed in a window with the respective colour. The sensor readings are not fully accurate because the way that the Red, Green, and Blue photoresistors are placed in the sensor are in a box array where blue and red are always adjacent to each-other, but the green photoresistors are all together. The datasheet also provided explanation to why the colour readings of the green photoresistors are the most accurate, while the red and blue ones are not always accurate. Furthermore, the sensor is affected from light intensity and direct light from a light source affects the colour readings. One solution to this might be using an acryllic case that reflects some of the light and lets part of the light hit the sensor, but that is not definitive. More research has to be done in that matter. 

The respective pages from the datasheet that display information on this matter are 1, 5, and 15. The datasheet can be viewed [here](https://www.intersil.com/content/dam/Intersil/documents/isl2/isl29125.pdf)

#### Colour samples used
![ColourSamples](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/ColorSamples.png?raw=true)

#### Displaying Color Readings in the Terminal and the Window
![Displaying Colour Readings](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/SampleReadingOutput.png?raw=true)

### Budget Update
There has been no budget update since I have not ordered any new parts. Everything has been kept track of and reported properly. The project budget can be viewed [here](https://github.com/denalddemirxhiu/ify/blob/master/Documentation/Colorify%20Budget.xlsx)

### Project Schedule Update
The project is going on schedule as of this week. There were some drawbacks last week when trying to solder the designed PCB, but when carefully examining it, the connections were done incorrectly. The PCB was re-designed, updated, printed and then soldered on November 12, 2018. The PCB was checked for problems with a multimeter, the sensor was checked if it was working with the PCB placed on the Raspberry PI and verified that the program worked while the sensor was mounted on the PCB. In the next few weeks, the enclosure of the completed project is due, the presentation needs to be prepared for and the final results of the project need to be made, such as the build instructions and the repository. The project schedule can be viewed [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Capstone%20Gantt%20Schedule.mpp)


## November 6th, 2018

### Updated PCB Design
Today the PCB vias were soldered, but when asked for feedback I realized that the connections on the PCB were upside down. The PCB design was updated on the Fritzing file, the files were sent to the prototype lab and they were updated on the Documentation folder in the repository. Below are the pictures of the soldered PCB vias on the improperly designed PCB and the new Updated PCB design:

#### Soldered vias on the improperly designed PCB
![Via Soldered Top](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Via_soldered1.png)

![Via Soldered Bottom](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Via_soldered2.png)

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
