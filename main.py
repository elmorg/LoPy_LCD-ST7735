# MicroPython ST7735 TFT display driver example usage
import pycom
import time
from font import terminalfont
from machine import Pin, SPI
from tft import TFT_GREEN

pycom.heartbeat(False)
# DC       - RS/DC data/command flag
# CS       - Chip Select, enable communication
# RST/RES  - Reset
dc  = Pin('P2', Pin.OUT, Pin.PULL_DOWN)
cs  = Pin('P23', Pin.OUT, Pin.PULL_DOWN)
rst = Pin('P22', Pin.OUT, Pin.PULL_DOWN)
pycom.rgbled(0x7f7f00)
# SPI Bus (CLK/MOSI/MISO)
# check your port docs to see which Pins you can use
spi = SPI(0, mode=SPI.MASTER, baudrate=2000000, polarity=0, phase=0)

# TFT object, this is ST7735R green tab version
tft = TFT_GREEN(128, 160, spi, dc, cs, rst)

# init TFT
tft.init()
pycom.rgbled(0x7f0000)
# start using the driver
tft.clear(tft.rgbcolor(20, 0, 25))
tft.rect(10,10,20,20,tft.rgbcolor(0, 255, 255))
tft.text(0, 0, "hi", terminalfont, tft.rgbcolor(0, 255, 255), size=1)
