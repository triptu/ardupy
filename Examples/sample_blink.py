from pyduino import *
import time

board = Arduino('COM10')
pin = 11

board.pinMode(pin, OUTPUT)

while True:
    board.digitalWrite(pin, HIGH)
    time.sleep(1)
    board.digitalWrite(pin, LOW)
    time.sleep(1)


