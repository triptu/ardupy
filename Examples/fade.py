from pyduino import *
import time

ard = Arduino('COM10')
pin = 11

#declare output pins as a list/tuple
ard.pinMode(pin, OUTPUT)

brightness = 0
fadeAmount = 5

while (True):
    ard.analogWrite(pin, brightness)
    brightness = brightness + fadeAmount
    if (brightness == 0 or brightness == 255):
        fadeAmount = -fadeAmount
