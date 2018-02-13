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
# if current_brightness + increment_value > max_brightness, set max_brightness
# if current_brightness - decrement_value < 0, set 0

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
        str(int(brightness_value) / step_value) + ' percent')
        exit()

    # keep the file opened for rest of the operations
    brightness_file = open(brightness_directory + '/brightness', 'w')

    if function == 'set':
        if value != None and value < 0 or value > 100:
            print('error: the valid brightness range is between 0 and 100')
            exit()

        brightness_file.write(str(value * step_value))

    if function == 'increment':
        increment_value = int(brightness_value) + int(value) * step_value

        if increment_value > int(max_brightness_value):
            increment_value = max_brightness_value

        brightness_file.write(str(increment_value))

    elif function == 'decrement':
        decrement_value = int(brightness_value) - int(value) * step_value

        if decrement_value < 0:
            decrement_value = 0

        brightness_file.write(str(decrement_value))
        
    # close the file
    brightness_file.close()


# the main function
def main():
    # set some essential variables
    brightness_directory = '/sys/class/backlight/intel_backlight'
    
    # parse run-time arguments
    parser = argparse.ArgumentParser(description=
    'Lightup v0.4, adjust your backlight brightness')

    parser.add_argument('-b', '--brightness', type=int, help=
    'set brightness to given value')
    
    parser.add_argument('-i', '--increment', type=int, help=
    'decrease brightness by given value')
    
    parser.add_argument('-d', '--decrement', type=int, help=
    'decrease brightness by given value')
    
    arguments = parser.parse_args()
    
    # set brightness using the -b argument
    if arguments.brightness:
        brightness(brightness_directory, 'set', arguments.brightness)

    # increase brightness using the -i argument
    elif arguments.increment:
        brightness(brightness_directory, 'increment', arguments.increment)

    # decrease brightness using the -d argument
    elif arguments.decrement:
        brightness(brightness_directory, 'decrement', arguments.decrement)
        
    # return current brightness
    else:
        brightness(brightness_directory, 'get', None)


# run the main function
main()

