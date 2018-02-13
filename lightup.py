#!/usr/bin/env python3
# lightup, release 0.5
# Thanks to wavexx(acpilight) for udev idea
# Copyright 2017, Aswin Babu Karuvally
# Copyright 2018, Aswin Babu Karuvally, Bipin Peacerebel

# import the serious stuff
import os
import shutil
import argparse

# todo
# exception if set value is greater than 100
# if current_brightness + increment_value > max_brightness, set max_brightness

# set or get the brightness
def brightness(brightness_directory, function, value):
    # get the current brightness value
    with open(brightness_directory + '/brightness', 'r') as brightness_file:
        brightness_value = brightness_file.readline().rstrip()

    # get the maximum brightness value
    with open(brightness_directory + '/max_brightness', 'r') as max_brightness:
        max_brightness_value = max_brightness.readline().rstrip()

    # calculate the step value
    step_value = int(int(max_brightness_value) / 100)
    
    if function == 'get':
        print("current brightness is " +
        str(int(brightness_value) / step_value))
        exit()

    # keep the file opened for rest of the operations
    brightness_file = open(brightness_directory + '/brightness', 'w')

    if function == 'set':
        brightness_file.write(str(value * step_value))

    # debug! convert value to int
    if function == 'increment':
        brightness_file.write(str(int(brightness_value) +
        int(value) * step_value))
        
    elif function == 'decrement':
        brightness_file.write(str(int(brightness_value) -
        int(value) * step_value))
        
    # close the file
    brightness_file.close()


# the main function
def main():
    # set some essential variables
    brightness_directory = '/sys/class/backlight/intel_backlight'
    
    # parse run-time arguments
    parser = argparse.ArgumentParser(description=
    'Lightup v0.4, adjust your backlight brightness')

    parser.add_argument('-b', '--brightness', help=
    'set brightness to given value')
    
    parser.add_argument('-i', '--increment', help=
    'decrease brightness by given value')
    
    parser.add_argument('-d', '--decrement', help=
    'decrease brightness by given value')
    
    arguments = parser.parse_args()
    
    # set brightness using the -b argument
    if arguments.brightness:
        brightness(brightness_directory, 'set', int(arguments.brightness))

    # increase brightness using the -i argument
    elif arguments.increment:
        brightness(brightness_directory, 'increment', int(arguments.increment))

    # decrease brightness using the -d argument
    elif arguments.decrement:
        brightness(brightness_directory, 'decrement', int(arguments.decrement))
        
    # return current brightness
    else:
        brightness(brightness_directory, 'get', None)


# run the main function
main()

