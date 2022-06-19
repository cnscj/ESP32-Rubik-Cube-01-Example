from machine import SoftI2C, Pin
from ip5306 import IP5306
from machine import Pin, I2C

i2c = I2C(1,scl=Pin(4), sda=Pin(13), freq=400000)
devices = map(hex, i2c.scan())
print("I2C devices found:", end=" ")
print(", ".join(devices))

battery = IP5306(i2c) #从scan中取得正确的bus
print(str(battery.level) + "%")