# AndroidCopyTool
A very simple application to copy all the files in a folder of your android mobile phone.

# Requirements
This app:
- Uses ADB, so you must have installed ADB in your pc and added it to the PATH variable of, in my case, Windows.
- Uses python (obviously lol). In my case I have run with no issues using Python 3.10.

# Ideal setup 
The exact setup I have used this app with is: 
- Reboot phone to recovery. ADB pull is way more faster from recovery than the normal system (I got like 7MBps in system and like 40MBps in recovery, which is the limit of my USB cable).
- USB-c connected to 3.0 port in my pc.
