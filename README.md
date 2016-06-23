# ardupy
Copy the ardupy folder to "C:\Python27\Lib\site-packages". And upload the arduino code to your Arduino board.

######**Blink code**
````python
from pyduino import *
import time
board = Arduino('COM10')
pin=13
board.pinMode(pin, OUTPUT)
while True:
    board.digitalWrite(pin, HIGH)
    time.sleep(1)
    board.digitalWrite(pin, LOW)
    time.sleep(1)
````
**All functions suppported are**
*pinMode(pin, set_to)
*digitalWrite(pin, set_to)
*digitalRead(pin)
*analogWrite(pin, set_to)
*analogRead(pin, set_to)
*closeAll()       ->sends low to all the OUTPUT pins.
*close()          ->closes the serial for communication.

#####Requirements- Python 2.x and pyserial.
More sample codes given in Examples Folder.
