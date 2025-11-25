# BBC Micro:bit - LED Scroll Text (MakeCode MicroPython)

# A very basic program that takes in a couple of strings and "scrolls"
# them through the onboard LEDs

# The two buttons are each assigned a small sequence of strings (or sentences) to
# be printed to the LEDs when the corresponding button is pushed

import microbit

# The Forever Loop

def on_forever():
    if input.button_is_pressed(Button.A): # if Button A pressed
        basic.show_string("My name is: ", 75) # (string, interval of scroll (in ms))
        basic.show_string("Lee", 75) # each interval "scroll" takes 75 milliseconds
        basic.show_string("My age is: ", 75)
        basic.show_string("29 :(", 75)
    if input.button_is_pressed(Button.B): # if Button B pressed
        basic.show_string("I am learning about Micro:bit", 70) # each interval 70 milliseconds
        basic.show_string("And MicroPython!", 70)
        basic.show_string("I want to learn more about: ", 70)
        basic.show_string(" - Embedded Systems", 70)
        basic.show_string(" - Electronics", 70)
        basic.show_string(" - Hardware Programming", 70)
basic.forever(on_forever) # plays forever loop
