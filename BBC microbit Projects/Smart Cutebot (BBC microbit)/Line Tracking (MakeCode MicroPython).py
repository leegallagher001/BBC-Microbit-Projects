# BBC micro:bit Smart Cutebot - Line Tracking (MakeCode MicroPython)

# A program that allows the Smart Cutebot to follow a line such as the one
# provided folded up in the kit
# Once again, I had to slow it down a bit, not just for my floor this time but for
# the tracking line provided in the kit - too small to go around it too quickly
# Once again, the best option for flashing this to the micro:bit is to go on the Microsoft
# MakeCode website and paste the code in and then flash from there https://makecode.microbit.org/

# Imports

import basic
import cuteBot

# On Start - once again the smily face :D

basic.show_leds("""
    # . . . #
    . . . . .
    # # # # #
    # . . . #
    . # # # .
    """)

# The Forever Loop

def on_forever():
    if cuteBot.tracking(cuteBot.TrackingState.L_UNLINE_R_LINE): # when tracking sensors see black line on right side but not on left
        cuteBot.motors(20, 10) # (left 20%, right 10% - turns right)
    if cuteBot.tracking(cuteBot.TrackingState.L_LINE_R_UNLINE): # when tracking sensors see black line on left side but not on right
        cuteBot.motors(10, 20) # (left 10%, right 20% - turns left)
    if cuteBot.tracking(cuteBot.TrackingState.L_R_LINE): # black line on both sides
        cuteBot.motors(20, 20) # moves forward at 20% speed
basic.forever(on_forever)
