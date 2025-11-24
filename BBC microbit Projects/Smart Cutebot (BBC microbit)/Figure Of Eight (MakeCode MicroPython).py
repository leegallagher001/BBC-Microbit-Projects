# Smart Cutebot (BBC micro:bit) - Figure Of Eight (MakeCode MicroPython)

# This program allows the Smart Cutebot to drive in a simple "figure of eight" pattern
# I wouldn't say its hugely precise, but I have had to experiment a little and slow mines
# down considerably as at 100% it is very fast
# Best flashed onto the BBC micro:bit from the Microsoft MakeCode website - https://makecode.microbit.org/

# Imports

import basic
import cuteBot

# On Start - LED Pattern (a big smily face, of course :D)

basic.show_leds("""
    # # . # #
    . . . . .
    # # # # #
    # . . . #
    . # # # .
    """)

# Forever Loop

def on_forever():
    cuteBot.move_time(cuteBot.Direction.FORWARD, 25, 0.2) # moves forward at 20% speed for 0.2 seconds
    cuteBot.motors(25, 10) # (left wheel speed, right wheel speed) (25%, 10%) - turns right
    basic.pause(1500) # continues the turn for 1.5 seconds
    cuteBot.move_time(cuteBot.Direction.FORWARD, 25, 0.4)
    cuteBot.motors(10, 25) # (left wheel speed, right wheel speed) (10%, 25%) - turns left
    basic.pause(1500)
    cuteBot.move_time(cuteBot.Direction.FORWARD, 25, 0.2)
basic.forever(on_forever) # runs the forever loop
