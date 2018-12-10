# Colorify Build Instructions

## Introduction
Colorify is a creative project that allows the user to scan colours in the environment with the help of a colour sensor. The project is meant to detect colours so that they can be used for illustration and graphic design purposes. At the end of this instructive tutorial, we will be able to detect colours in the environment as well as display the colour readings in RGB and HEX format for the user to use freely. Below, the diagrams provide a visual way on how the project works, and how it might be integrated with a database and a mobile application for further development.

### System Diagram
![System Diagram](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/System%20Diagram.png?raw=true)

### Capstone UML Diagram
![Capstone UML Diagram](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/System%20UML%20Diagram.png?raw=true)

#### Helpful Skills
 - Soldering
 - Raspberry PI knowledge
 - I2C knowledge
 - Python knowledge

## Bill of Materials
The devices and components that we will need to complete the project, as well as the sources where they can be found are provided below for reference

| Item Name                                 | Source/Supplier                                                                                                  |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Raspberry Pi 3B+ Starter Kit              | CanaKit - https://www.canakit.com/raspberry-pi-3-model-b-plus-starter-kit.html                                   |
| ISL29125 RGB Light Sensor                 | SparkFun - https://www.sparkfun.com/products/12829                                                               |
| Breadboard Jumper Wires                   | HaoBase/Amazon - https://www.amazon.ca/gp/product/B01DLKLL6C/ref=ox_sc_act_title_1_1_1?smid=A3F3WC2XXCSM1P&psc=1 |
| Bernzomatic Rosin Core Solder (Lead free) | Canadian Tire - http://www.canadiantire.ca/en/pdp/bernzomatic-rosin-core-solder-0586000p.html#srp                |
| Wire Stripper                             | Ideal/Amazon - https://www.amazon.ca/Ideal-45-120-Stripper-10%C3%9018-Stranded/dp/B000JKWVXA                     |
| Breadboard                                | Canada Robotix - http://www.canadarobotix.com/solderless-breadboard/830-point-breadboard                         |
| Soldering Iron                            | Canadian Tire - http://www.canadiantire.ca/en/pdp/weller-25w-soldering-iron-kit-0586309p.html#srp                |
| Digital Multimeter                        | Canadian Tire - http://www.canadiantire.ca/en/pdp/autoranging-digital-multimeter-0520052p.0520052.html           |
| Clear Acrylic 12"x24"                     | Johnston Industrial - http://www.johnstonplastics.com/toronto/                                                   |
| 40-pin Stackable Header                   | Adafruit - https://www.adafruit.com/product/1979                                                                |
| Arduino Stackable Header Kit              |  Sparkfun - https://www.sparkfun.com/products/10007                                                            |
| Computer Monitor                          |  Bestbuy - https://www.bestbuy.ca/en-ca/product/hewlett-packard-hp-21-5-fhd-60hz-7ms-gtg-ips-led-monitor-22vc-black-22vc/10514441.aspx?                                                                                                              |
| Wired Keyboard                            |  Bestbuy - https://www.bestbuy.ca/en-ca/product/mmnox-mmnox-usb-keyboard-op004-english-op004/10383781.aspx?&cmp=knc-s-71700000022735665&gclid=CjwKCAiA9K3gBRA4EiwACEhFe3TcS5GJtncWi2ZyHx2JcIT2YdmtqwuIXsQ2FbTyfpRkxJ3cG1OAhRoCo4QQAvD_BwE&gclsrc=aw.ds                                                                                                     |
| Wired Mouse                               |   Bestbuy - https://www.bestbuy.ca/en-ca/product/rapoo-optical-mouse-n1130-white/12966363.aspx?                                                                                                              |

Note: The Raspberry Pi 3B+ Starter Kit comes with everything you need such as:
 - Standard Power Supply
 - 16 GB microSD card
 - Black enclosure
 - microSD USB adapter
 - HDMI Cable

If you would like to purchase the above items separately make sure they are bought from a reliable source!

For a more detailed bill of materials with the component prices, sources, part numbers you can click [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Colorify%20Budget.xlsx). The total amount of money needed to be spent for this project is about $230 (CAD).

## Time Commitment
This project should not take more than a weekend to be completed after all the components have been gathered. Overall, it should take about 5-7 hours to complete (considering that the PCB has been printed successfully, otherwise the PCB should take about a half-day to be printed). This can be divided in these steps:
 - Raspberry PI setup (2 - 3 hours)
 - Sensor Soldering (30 mins)
 - PCB Soldering with stackable headers (45 mins)
 - Enclosure printing (laser cutting) and assembly (45 mins)
 - Putting it all together (1 hour)
 - Verifying that everything works (30 mins)

## Setting up the Raspberry PI 
For this portion you will need a monitor compatible with HDMI, a wired keyboard (USB) and a wired mouse (USB).
 1. Download the latest version of Raspbian. The image for flashing the Raspbian OS in the Raspberry PI can be found [here](https://www.raspberrypi.org/downloads/raspbian/)
 2. Format the microSD card by plugging it in your computer of choice and use the software found [here](https://www.sdcard.org/downloads/formatter_4/index.html)
 3. Use a software such as [Etcher](https://www.balena.io/etcher/) or [Win32DiskImager](http://sourceforge.net/projects/win32diskimager/) to flash the OS image to the microSD card.
 4. After this process has been finished successfully plug the microSD card in the Raspberry PI 3B+, connect the HDMI cable, the mouse, and the keyboard and power the device on.
 5. After finishing the setup and while on the Desktop we need to change the I2C and VNC interfaces to enabled. This can be done by going to the Start Menu->Preferences->Raspberry Pi Configuration->Interfaces, then set VNC to enabled and I2C to enabled
 
 After these steps have been followed carefully, we can move on to the mechanical assembly.
 
## Mechanical Assembly
To get started, we need to solder the pins to the ISL29125 RGB Light sensor. To do so we need to have 5 pins for each of the holes in the sensor and we need to have the soldering equipment ready. The soldering process needs to be careful as to not short any of the pins with each other which damage the sensor. After the pins have been soldered to the sensor, it should look something like this:

![Sensor Soldered](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Sensor%20with%20pins.png?raw=true)

Secondly, we need to connect the sensor to the Raspberry PI 3B+ to test if it works properly. It is a good idea to power down the Raspberry PI before continuing with this step. First, we place already soldered sensor in the breadboard. Using [this](https://www.theengineeringprojects.com/wp-content/uploads/2018/07/introduction-to-raspberry-pi-3-b-plus-2.png) diagram, we are going to make the appropriate connections from the sensor to the pin headers of the Raspberry PI. For the connections we are going to use the Male-to-Female jumper wires. Since the sensor has labeled pins, we are going to make these connections:
 - PIN 1 (3.3V) of the Raspberry PI should be connected to the pin labeled as 3.3V in the sensor
 - PIN 6 (GND) of the Raspberry PI should be connected to the pin labeled as GND in the sensor
 - PIN 3 (SDA) of the Raspberry PI should be connected to the pin labeled as SDA in the sensor
 - PIN 5 (SCL) of the Raspberry PI should be connected to the pin labeled as SCL in the sensor
 
After the appropriate connections have been made, the wiring should look something like this:

![Sensor Wiring](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/RaspberryPi-Sensor-Wired.png?raw=true)

After powering on the Raspberry PI we need to verify that the sensor is being recognized. With the wiring still in place launch the terminal window and type this command:

      sudo i2cdetect -y 1
 
The command will display the sensor in a table like this:
![i2cDetect](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/i2cDetect.png)

NOTE: If you don't see the sensor's I2C address in the table (0x44), then verify the connections, verify that I2C Interface is enabled, and as a final resort restart the Raspberry PI.

After all the steps in this section have been verified, you can move on to the next step.

## PCB Soldering
The PCB design used to print the PCB can be found [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/ISL29125.fz.fzz). The design was made using [Fritzing](http://fritzing.org/home/). To print the PCB you need to convert the provided files into Gerber files and send them to any production facility, as the files are industrially universal.

After the PCB has been printed, we are going to solder the 5 pin stackable header, and the 20 pin stackable header into the PCB. Since none of the stackable headers we have is 5-pin we are going to break one of them into a 5-pin, which can easily be done using a set of pliers. After we do that, we are going to solder the VIAs (small holes with connections on both sides). To do that we are going to use some hookup wire, which we are going to strip and place in the VIAs. After verifying that the VIAs have been soldered, we can insert the stackable headers in the appropriate pins. The 5-pin header is going to be inserted in the side where the labels are found (GND, 3.3V, SDA, SCL). The 40-pin header is going to be inserted on the other side with the pins facing the side the labels are found. After the pins have been soldered we can verify if the connections have been correctly made by using a multimeter. After all the work has been finished the PCB should look something like this:

### PCB Soldered Front
![PCB Front](https://raw.githubusercontent.com/denalddemirxhiu/Colorify/master/Documentation/PCB%20Soldered%20Front.jpg)

### PCB Soldered Back
![PCB Back](https://raw.githubusercontent.com/denalddemirxhiu/Colorify/master/Documentation/PCB%20Soldered%20Back.jpg)

## Power Up
After the PCB has been soldered correctly and the sensor has been verified to work with the Raspberry PI, it is time for the power up portion. With the Raspberry PI powered off, the PCB is going to be mounted on the Raspberry PI using the 40-pin stackable header and the sensor is going to be mounted on the 5-pin header on the PCB. After the mounting process is done it should look something like this:

![Mounted PCB Sensor](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/SensorMountedOnTheBoard.png?raw=true)

The case that comes with the Raspberry PI 3B+ can fit the PCB board mounted in it. For that reason we don't need to make any specific enclosure for it.

![Case with Sensor](https://raw.githubusercontent.com/denalddemirxhiu/Colorify/master/Documentation/PCB%20Mounted%20in%20Case.jpg)

After the PCB and the sensor is mounted on the board, it can be powered up and verified that the Raspberry PI recognizes the sensor using the same i2cdetect command as above:

       sudo i2cdetect -y 1

Using the supplied script that can be downloaded from [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/readSensor.py), you can test the sensor reading actual colour values from the environment. The code uses Python 3 and can be compiled and run using the default python editor in the Raspberry PI, Thonny. If everything has been done correctly you should see an output on the screen like this:

![Sensor Output](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/SampleReadingOutput.png?raw=true)

Note: For the sensor to read different colour values you might want to use a plastic piece of paper (preferrably with colour), however if it is transparent you can use a Sharpie with some different colours to simulate different colour readings. This is one way to test if the sensor is reading values correctly

![Colour samples](https://raw.githubusercontent.com/denalddemirxhiu/Colorify/master/Documentation/ColourSamples.jpg)

## Enclosure

The enclosure for this project does not require any custom case to be made. In fact the case that comes with the Raspberry PI 3B+ can hold the PCB and the sensor intact. The only part that is needed for this enclosure is the top part which ensures that the sensor is kept intact with no contact to materials that might damage it. The enclosure also requires a set of 4 clamps that hold everything together. Both the top enclosure sheets and the clamps are made of acrylic and can easily be laser cut in a matter of minutes. The file for the top enclosure sheets can be found [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Top%20Case%20Design%20Files.cdr) and the file for the clamps can be found [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Case%20Clamps.cdr). Both designs were made with CorelDraw X6.

The top enclosure part has 5 acrylic frames and one acrylic top that can be stacked together. To glue the components together you might use any transparent glue that you can think of, but if you can find some Liquid Cement for plastic that would work too. After the acrylic sheets have been stacked together and have been glued, the top part of the case should look something like this:

### Acrylic Top
![Top Case](https://raw.githubusercontent.com/denalddemirxhiu/Colorify/master/Documentation/Acrylic%20Top.png)

## Finishing it up
By now the Raspberry PI should be in its black case that came with the Starter Kit. The PCB with the mounted sensor, will be inserted into the GPIO pins of the Raspberry PI. Next the acrylic top will be placed on the top of the case with the 4 clamps inserted on each side to support the enclosure. After all the processes above these should be the final results:

### Case with Acrylic sheets on top
![Completed Case](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Case%20With%20Acrylic%20Top.png?raw=true)

### Completed Case
![Completed Case with Clamps](https://raw.githubusercontent.com/denalddemirxhiu/Colorify/master/Documentation/Case%20Completed.png)

## Testing
It is useful to test the hardware before testing the software side of the project. First when finishing the soldering of the PCB it is a good idea to check each connection between the appropriate pins. This part of the testing process can be performed using any conductive wire inserted in the stackable header for the pins we are going to use, and a multimeter to test if the connection is correct. If when testing the pins a open circuit is observed then the soldering should be checked and the appropriate measures should be taken.

After testing the hardware we are going to test the software side. With the sensor plugged in the PCB, which should be inserted in the Raspberry PI with the help of the stackable header, we are going to compile and run the provided software for detecting color values and displaying them. 
 - First, we need to check that the Raspberry PI can recognize the sensor mounted on the board. This can be done with the command: `i2cdetect -y 1`. If the sensor is not shown in the table output with the address 0x44 printed on the table, then the Raspberry PI cannot detect it. Make sure that the connections have been checked appropriately, the sensor is not damaged, and the I2C interface has been enabled in the Raspberry PI.
 - Second, compile and run the python code found [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/readSensor.py) using Thonny. The color readings should be displayed accordingly in RGB and HEX format in the console, while the color readings should also be displayed in a separate window. If there are problems with compilation and running the code, check if the source code is correct, check if Python 3 is correctly installed in the Raspberry PI, and as a last resort restart the device.

## Resources used
 - Intersil Datasheet for ISL29125 found [here](https://www.intersil.com/content/dam/Intersil/documents/isl2/isl29125.pdf)
 - Sparkfun ISL29125 hookup guide found [here](https://learn.sparkfun.com/tutorials/isl29125-rgb-light-sensor-hookup-guide?_ga=2.166805693.2081027499.1544412420-1494811950.1544240207)
 - Soldering tutorial found [here](https://www.youtube.com/watch?v=Qps9woUGkvI)
 
