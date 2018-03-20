# Lightup  
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
- Run lightup -b BRIGHTNESS_VALUE
- To increment brightness, use lightup -i INCREMENT_VALUE
- To decrement brightness, use lightup -d DECREMENT_VALUE

## Integrating Lightup with OpenBox 
- Open ~/.config/openbox/rc.xml 
- Locate <!-- Keybindings for running aplications --> under <keyboard> section and add the following
    <keybind key="XF86MonBrightnessUp">
        <action name="Execute">
            <command>lightup -i 2</command>
        </action>
    </keybind>

    <keybind key="XF86MonBrightnessDown">
        <action name="Execute">
            <command>lightup -d 2</command>
        </action>
    </keybind> 
- Replace XF86MonitorBrightnessUp and XF86MonitorBrightnessDown with your key of choice 

## Alternatives
acpilight is a nice alternative to lightup, and has better capabilities at 
the moment
