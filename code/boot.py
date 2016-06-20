# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal

from network import WLAN
from machine import UART
import os
import time
import machine

f=open("mylog.log","w")


#Enable the UART on the USB-to-serial port
uart = UART(0, baudrate=115200)
# duplicate the terminal on the UART
os.dupterm(uart)
f.write("/enabled uart 0 at baudrate 115200 for access via USB on expansion board")


#Try to make wipy a station:
wlan = WLAN() # we call the constructor without params
wlan = WLAN(mode=WLAN.STA)
f.write("\nNew Mode: ")
f.write(str(wlan.mode()))
f.write("\n")

#nets = wlan.scan()
#for net in nets:
#    if net.ssid == 'muizenberg':
#        f.write('Network found!')
#        wlan.connect(net.ssid, auth=(net.sec, '7yeb623e'), timeout=5000)
#        while not wlan.isconnected():
#            machine.idle() # save power while waiting
#        f.write('WLAN connection succeeded!')
#        break
#
#f.write("I made a connection")

if machine.reset_cause() != machine.SOFT_RESET:
    wlan.init(WLAN.STA)
    # configuration below MUST match your home router settings!!
    wlan.ifconfig(config=('192.168.2.107', '255.255.255.0', '192.168.2.1', '8.8.8.8'))

if not wlan.isconnected():
    # change the line below to match your network ssid, security and password
    wlan.connect('muizenberg', auth=(WLAN.WPA2, '7yeb623e'), timeout=5000)
    while not wlan.isconnected():
        machine.idle() # save power while waiting

    f.write("\nI connected")

f.close()
