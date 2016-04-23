#!/usr/bin/env python
########################################################################                                                                  
# Calibration and read of the CO2 sensor MH-Z16
# according to the datasheet : http://www.seeedstudio.com/wiki/images/c/ca/MH-Z16_CO2_datasheet_EN.pdf
# output value directly in ppm
# Doms made                                                              
# History
# ------------------------------------------------
# Author     Date      		Comments
# Doms      13 04 15 		Initial Authoring
# 			                                                         
'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2015  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
'''      
#
########################################################################
import os
import serial, time
import smbus
import math
import RPi.GPIO as GPIO
import struct
import sys
import datetime
import grovepi
import struct
import re
from grovepi import *

#
__author__ = 'Doms Genoud'

#co2 sensor
#use an external usb to serial adapter
#ser = serial.Serial('/dev/ttyUSB0',  9600, timeout = 1)	#Open the serial port at 9600 baud

#To open the raspberry serial port
ser = serial.Serial('/dev/ttyAMA0',  9600, timeout = 1)	#Open the serial port at 9600 baud

#init serial
ser.flush()


############# carbon dioxid CO2 #####################
class RFIDReader:
#inspired from c code of http://www.seeedstudio.com/wiki/Grove_-_CO2_Sensor
    def read(self):
        try:
        	buffer = ''
        	rfidPattern = re.compile(b'[\W_]+')
          	while True:
          		buffer = buffer + ser.read(ser.inWaiting())
          		if '\n' in buffer:
        			lines = buffer.split('\n')
        			last_received = lines[-2]
                    print last_received
        			match = rfidPattern.sub('', last_received)

        		if match:
          			print match
          		else:
            	    print 'no card find'



        except IOError:
                return '-1'

########################################################################################################
#############   MAIN
########################################################################################################
# following the specs of the sensor :
# read the sensor, wait 3 minutes, set the zero, read the sensor
rfid = RFIDReader()

while True:
    try:
        print("Read before calibration-->",rfid.read())
        print("DONE")
        break

    except IndexError:
        print("Unable to read")
    except KeyboardInterrupt:
        print("Exiting")
        sys.exit(0)
