#!/bin/bash
# lightup installation script, release 0.1

# copy the files
echo "copying files..."
mkdir /opt/lightup
cp lightup.py /opt/lightup
cp 90-backlight.rules /etc/udev/rules.d

# make links
echo "making links..."
ln -s /opt/lightup/lightup.py /usr/bin/lightup

# set the permissions
echo "setting permissions..."
chmod 777 /opt/lightup/lightup.py
chmod 777 /etc/udev/rules.d/90-backlight.rules

# tell user to restart
echo "okay, you might have to restart now :)"
