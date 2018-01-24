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

    elif function == 'inc':
        brightness_file = open(brightness_file_path, 'r+')
        curr_val = brightness_file.readline().rstrip()
        value = int(curr_val)+int(value)
        brightness_file.write(str(value))
        brightness_file.close()

    elif function == 'set':
        brightness_file = open(brightness_file_path, 'r+')
        brightness_file.write(value)
        brightness_file.close()


# the main function
def main():
    # set some essential variables
    brightness_file_path = '/sys/class/backlight/intel_backlight/brightness'
    
    # parse run-time arguments
    parser = argparse.ArgumentParser(description=
        'lightup, adjust your backlight brightness')
    parser.add_argument('-b', '--brightness', help='set backlight')
    parser.add_argument('-i', '--increment', help='Increase brightness')
    arguments = parser.parse_args()
    
    # set brightness
    if arguments.brightness: # in ['-b', '--brightness']:
        brightness(brightness_file_path, 'set', arguments.brightness)

    # increase brightness
<<<<<<< HEAD
    elif arguments.increment:
=======
    elif arguments.increment: # in ['-i', '--increment']:
>>>>>>> 6239a563a3b3860c28ee34c97dbd1220add0ac7b
        brightness(brightness_file_path, 'inc', arguments.increment)
        
    # return current brightness
    else:
        print('here')
        brightness(brightness_file_path, 'get', None)


# run the main function
main()
