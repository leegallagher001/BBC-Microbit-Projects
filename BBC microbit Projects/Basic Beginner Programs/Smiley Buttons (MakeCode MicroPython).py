# BBC Micro:bit - Smiley Buttons (MakeCode MicroPython)

# A very basic program that flashes different face on the onboard LEDs depending
# on which button is pressed

# Button A is a happy face
# Button B is a sad face
# Buttons A+B is a silly face, then a surprised face, then a laughing face


import microbit

def on_button_pressed_a(): # function for when button A is pressed
    basic.show_icon(IconNames.HAPPY) # show happy face
    basic.pause(2000) # for 2 seconds
    basic.clear_screen() # then clear screen
input.on_button_pressed(Button.A, on_button_pressed_a) # carry out function when input from button A

def on_button_pressed_b():
    basic.show_icon(IconNames.SAD)
    basic.pause(2000)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    basic.show_icon(IconNames.SILLY)
    basic.pause(1000)
    basic.show_icon(IconNames.SURPRISED)
    basic.pause(1000)
    basic.show_leds("""
    . # . # .
    . . . . .
    # # # # #
    # . . . #
    . # # # .
    """)
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)
