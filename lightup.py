#!/usr/bin/env python3
# lightup, release 0.3
# Thanks to wavexx(acpilight) for udev idea
# Copyright 2017, Aswin Babu Karuvally

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
        curr_val = brightness_file.readline().rstrip()
        value = int(curr_val)+int(value)
        brightness_file.write(str(value))
        brightness_file.close()


# the main function
def main():
    # set some essential variables
    brightness_file_path = '/sys/class/backlight/intel_backlight/brightness'
    
    # parse run-time arguments
    parser = argparse.ArgumentParser(description=
        'lightup, adjust your backlight brightness')
    parser.add_argument('-b', '--brightness', help='set backlight')
    arguments = parser.parse_args()
    
    # set brightness
    if arguments.brightness:
        brightness(brightness_file_path, 'set', arguments.brightness)
    
    # return current brightness
    else:
        brightness(brightness_file_path, 'get', None)


# run the main function
main()
