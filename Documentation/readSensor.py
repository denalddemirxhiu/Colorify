import smbus
import time
from tkinter import *

# Get I2C bus
bus = smbus.SMBus(1)

# Create a WINDOW
window = Tk()
window.title ("Colour Readings")


# ISL29125 address, 0x44(68)
# Select configuation-1register, 0x01(01)
# 0x0D(13) Operation: RGB, Range: 360 lux, Res: 16 Bits
bus.write_byte_data(0x44, 0x01, 0x05)

time.sleep(1)
# ISL29125 address, 0x44(68)
# Read data back from 0x09(9), 6 bytes
# Green LSB, Green MSB, Red LSB, Red MSB, Blue LSB, Blue MSB

print("Reading colour values and displaying them in a new window\n")

def getAndUpdateColour():
    while True:
        data = bus.read_i2c_block_data(0x44, 0x09, 6)

        # Convert the data
        green = int((data[1] * 256 + data[0])/256)
        red = int((data[3] * 256 + data[2])/256)
        blue = int((data[5] * 256 + data[4])/256)
        hex = "#" + format(red, '02x') + format(green, '02x') + format(blue, '02x')
        
        # Output data to the console RGB and HEX values
        print("RGB(%d %d %d)" % (red, green, blue))
        print("HEX ", hex)
        print()
        
        # Update window Color
        window.configure(bg=hex)
        window.update_idletasks()
        
        time.sleep(2) 
        
# Settinh window size, resizable and the update interval
window.geometry("500x500");
window.resizable(0, 0)
window.after(2000, getAndUpdateColour())
window.mainloop()


