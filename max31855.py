#!/usr/bin/python

from max31855 import *
import time
#from wiringpi import gpio

global duty
global secs
global ramp
duty = 0.001
secs = 10
ramp = 0.0

# Initiate Thermocouple
thermocouple = MAX31855(0, "f")

start_time = time.time()
old_time = time.time()

def outputTemp():
    global ramp
    global secs
    global old_temp
    global old_time
    global start_time
    avg_num = 10
    for x in range(0,secs):
        temp = []
        for y in range(0,avg_num):
            temp.append(thermocouple.get())
            time.sleep(1/avg_num)
        new_temp = sum(temp)/float(len(temp))
        if x == 0:
             old_temp = new_temp
        
        new_time = time.time()-.5
        delta_time = new_time - old_time
        if x == secs - 1:
           ramp = 15*(new_temp - old_temp)/delta_time
           old_time = new_time

        output = ('Current Temp: {:.2f} Ramp: {:.2f} Elap Time: {:.2f}'.format(new_temp, ramp, (new_time - start_time)/60))
        return output
while 1:
    try:
        
        print(outputTemp())
    except KeyboardInterrupt:
        break


