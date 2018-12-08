# Colorify Build Instructions

## Introduction
Colorify is a creative project that allows the user to scan colours in the environment with the help of a colour sensor. The project is meant to detect colours so that they can be used for illustration and graphic design purposes. At the end of this instructive tutorial, we will be able to detect colours in the environment as well as display the colour readings in RGB and HEX format for the user to use freely.  

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
| Stackable Header                               |                                                                                                                  |
| Stackable Header                               |                                                                                                                  |
| Computer Monitor                          |                                                                                                                  |
| Wired Keyboard                            |                                                                                                                  |
| Wired Mouse                               |                                                                                                                  |

Note: The Raspberry Pi 3B+ Starter Kit comes with everything you need such as:
 - Standard Power Supply
 - 16 GB microSD card
 - Black enclosure
 - microSD USB adapter
 - HDMI Cable

If you would like to purchase the above items separately make sure they are bought from a reliable source!

For a more detailed bill of materials with the component prices, sources, part numbers you can click [here](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/Colorify%20Budget.xlsx)

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
 
 After these steps have been followed we can move on to the mechanical assembly.
 
## Mechanical Assembly

To get started, we need to solder the pins to the ISL29125 RGB Light sensor. To do so we need to have 5 pins for each of the holes in the sensor and we need to have the soldering equipment ready. The soldering process needs to be careful as to not short any of the pins with each other which damage the sensor. After the pins have been soldered to the sensor, it should look something like this:

// TODO insert image here

Secondly, we need to connect the sensor to the Raspberry PI 3B+ to test if it works properly. It is a good idea to power down the Raspberry PI before continuing with this step. First, we place already soldered sensor in the breadboard. Using [this](https://www.theengineeringprojects.com/wp-content/uploads/2018/07/introduction-to-raspberry-pi-3-b-plus-2.png) diagram, we are going to make the appropriate connections from the sensor to the pin headers of the Raspberry PI. For the connections we are going to use the Male-to-Female jumper wires. Since the sensor has labeled pins, we are going to make these connections:
 - PIN 1 (3.3V) of the Raspberry PI should be connected to the pin labeled as 3.3V in the sensor
 - PIN 6 (GND) of the Raspberry PI should be connected to the pin labeled as GND in the sensor
 - PIN 3 (SDA) of the Raspberry PI should be connected to the pin labeled as SDA in the sensor
 - PIN 5 (SCL) of the Raspberry PI should be connected to the pin labeled as SCL in the sensor
 
After the appropriate connections have been made, the wiring should look something like this:

// TODO insert image here

After powering on the Raspberry PI we need to verify that the sensor is being recognized. With the wiring still in place launch the terminal window and type this command:

 sudo i2cdetect -y 1
 
The command will display the sensor in a table like this:
[!i2cDetect](https://github.com/denalddemirxhiu/Colorify/blob/master/Documentation/i2cDetect.png)

NOTE: If you don't see the sensor I2C address in the table (0x44), then verify the connections, verify that I2C Interface is enabled, and as a final resort restart the Raspberry PI.


## PCB Soldering

## Power Up

## Unit Testing


