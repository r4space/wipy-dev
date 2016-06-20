from machine import uart
import os
uart = uart(0, baudrate=115200)
os.dupterm(uart)
