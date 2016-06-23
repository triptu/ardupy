from pyduino import *
import time

b = Arduino('COM10')
pin = 1

b.pinMode(pin, INPUT)

while (True):
    val = b.analogRead(pin)
    print val
    time.sleep(0.5)
