
import radio
from time import sleep
import digitalio
import board
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True


# Forever loop printing readings and waiting for 2 seconds
while True:
    led.value = not led.value
    radio.send("Test")
    print("radio message sent")
    time.sleep(2)

