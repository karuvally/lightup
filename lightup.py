#!/usr/bin/env python3
# lightup, release 0.5
# Thanks to wavexx(acpilight) for udev idea
# Copyright 2017, Aswin Babu Karuvally
# Copyright 2018, Aswin Babu Karuvally, Bipin Peacerebel

# import the serious stuff
import os
import shutil
import argparse


# set or get the brightness
def brightness(brightness_file_path, function, value):
    if function == 'get':
        brightness_file = open(brightness_file_path, 'r')
        print("current brightness is " + brightness_file.readline().rstrip())
        brightness_file.close()

    elif function == 'set':
        brightness_file = open(brightness_file_path, 'r+')
        brightness_file.write(value)
        brightness_file.close()

    # common code for increment and decrement

    elif function:
        brightness_file = open(brightness_file_path, 'r+')
        current_value = brightness_file.readline().rstrip()

        if function == 'increment':
            brightness_file.write(str(int(current_value) + int(value)))
        elif function == 'decrement':
            brightness_file.write(str(int(current_value) - int(value)))
        
        brightness_file.close()


# the main function
def main():
    # set some essential variables
    brightness_file_path = '/sys/class/backlight/intel_backlight/brightness'
    
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
        brightness(brightness_file_path, 'set', arguments.brightness)

    # increase brightness using the -i argument
    elif arguments.increment:
        brightness(brightness_file_path, 'increment', arguments.increment)

    # decrease brightness using the -d argument
    elif arguments.decrement:
        brightness(brightness_file_path, 'decrement', arguments.decrement)
        
    # return current brightness
    else:
        brightness(brightness_file_path, 'get', None)


# run the main function
main()

