import bmp280
import radio
from time import sleep
import digitalio
import board

# Set up LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

# Forever loop printing readings and waiting for 2 seconds
while True:
    # Turn LED on or off
    led.value = not led.value
    # Read temp and pressure from bmp280
    temp = bmp280.read_temperature()
    pres = bmp280.read_pressure()
    # Create variable to store message
    mess = "MHS, T: {:.1f}, P: {:.2f}".format(temp, pres)
    # Print message for debugging
    print(mess)
    # Send message on radio
    radio.send(mess)
    # Print message for debugging (radio send worked)
    print("radio message sent")
    sleep(2)

