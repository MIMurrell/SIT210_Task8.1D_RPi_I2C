#Title: Task 8.1D Raspberry Pi I2C
#Author: Matthew Murrell - 218296335
#Date: 8/05/2022
#Purpose: Prints a different message to the screen depending on the sensed light level
#Developed using information from the Pibits Raspberry Pi and BH1750 Light Sensor Tutorial: http://www.pibits.net/code/raspberry-pi-bh1750-light-sensor.php 

#LIBRARIES
import smbus
import time

#GLOBAL VARIABLES
BH1750     = 0x23 # Default device I2C address
OTHR_MODE = 0x20 #One-time high-res mode
bus = smbus.SMBus(1)  #Bus 1

#The maximum thresholds for each level of light
BRIGHT = 200
MEDIUM = 150
DARK = 100
TOO_DARK = 50

#The time to sleep between each reading
SLEEP_TIME = 2

#FUNCTIONS
#Converts the passed raw data reading into a decimal number
def convert_to_number(data):
    return ((data[1] + (256 * data[0])) / 1.2)
 
#Gets a light reading from the BH1750 sensor and returns it as a decimal number
def get_light(addr=BH1750):
    raw_data = bus.read_i2c_block_data(addr,OTHR_MODE)
    return convert_to_number(raw_data)

#Prints a different message for each light level
def light_output(light):
    if light <= TOO_DARK:
       print("Too dark")
    elif light <= DARK:
       print("Dark")
    elif light <= MEDIUM:
       print("Medium") 
    elif light <= BRIGHT:
       print("Bright") 
    else:
       print("Too bright") 

#MAIN LOOP
#The main loop of the program
while True:
    light = get_light()
    light_output(light)
    time.sleep(SLEEP_TIME)

    
