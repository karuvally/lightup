#!/bin/bash
# lightup installation script, release 0.5

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
chmod 555 /opt/lightup/lightup.py

# add user to video group
gpasswd -a $LOGNAME video

# tell user to restart
echo "okay, you might have to restart now :)"
