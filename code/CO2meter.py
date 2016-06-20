from machine import uart
import os
uart = uart(0, baudrate=115200)
os.dupterm(uart)

machine.sleep() # 950uA (in WLAN STA mode). Wake sources are Pin, RTC and WLAN

