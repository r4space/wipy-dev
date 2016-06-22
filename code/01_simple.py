"""
Blynk is a platform with iOS and Android apps to control
Arduino, Raspberry Pi and the likes over the Internet.
You can easily build graphic interfaces for all your
projects by simply dragging and dropping widgets.

  Downloads, docs, tutorials: http://www.blynk.cc
  Blynk community:            http://community.blynk.cc
  Social networks:            http://www.fb.com/blynkapp
                              http://twitter.com/blynk_app

This example shows one of the simplest scripts,
that doesn't define any custom behaviour.
You're still able to do direct pin operations.

In your Blynk App project:
  Add a Gauge widget,  bind it to Analog Pin 5.
  Add a Slider widget, bind it to Digital Pin 25.
  Run the App (green triangle in the upper right corner).

Don't forget to change WIFI_SSID, WIFI_AUTH and BLYNK_AUTH ;)
"""

import BlynkLib
from network import WLAN

BLYNK_AUTH = '00b0a417efa24ee6a99507c78c986063'

# show IP address (assume WiPy already booted with wifi in station mode)
print('IP address:', WLAN().ifconfig()[0])

# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# start Blynk (this call should never return)
blynk.run()
