#Lightup
An xbacklight replacement 

## Introduction
Lightup is a simple utility to change the backlight brightness. It was developed
as xbacklight, a utility developed by intel for changing the brightness no
longer works.

## Installation
- Clone the git repository or download as zip and unzip the contents
- Run ./install.sh as root
- Reboot your machine

## Usage
Run lightup -b <brightness_value>

## Todo
- Automated backlight path finding
- Add increment and decrement switches
- Fading backlight adjustments
- Reload udev rules without reboot

## Alternatives
acpilight is a nice alternative to lightup, and has better capabilities at 
the moment

##Troubleshooting
 -if you get permission errot for `brightness` file, change its permission to 756 or higher.
