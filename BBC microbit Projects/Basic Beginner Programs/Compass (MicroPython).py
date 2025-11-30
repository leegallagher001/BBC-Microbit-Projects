# BBC Micro:bit - Compass (MicroPython)

# A program that turns the Micro:bit into a simple compass, using the onboard
# LEDs to show the user (roughly) what direction that they are facing

# This is the first project I've made where I didn't use MakeCode to flash the
# program to the Micro:bit, so it proved a little trickier than usual. The "Micro:bit Python
# Editor" website proved useful for this

from microbit import *

if button_a.was_pressed():
    compass.calibrate() # requests that user tilt screen to calibrate

while True:
    heading = compass.heading()
    if heading > 20 and heading < 160:
        display.show(Image.ARROW_W)
    elif heading >= 160 and heading < 200:
        display.show(Image.ARROW_S)
    elif heading >= 200 and heading < 340:
        display.show(Image.ARROW_E)
    else:
        display.show(Image.ARROW_N)
