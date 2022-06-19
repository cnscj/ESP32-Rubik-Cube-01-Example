import ili934x
color565 = ili934x.color565
from machine import Pin, SPI
spi = SPI(miso=Pin(19), mosi=Pin(23, Pin.OUT), sck=Pin(18, Pin.OUT))
display = ili934x.ILI9341(spi, cs=Pin(14), dc=Pin(27), rst=Pin(33))
display.fill(color565(0xff, 0xff, 0xff))
display.print('Hello,World!')

