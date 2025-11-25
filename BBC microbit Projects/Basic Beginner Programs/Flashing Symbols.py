# BBC Micro:bit - Flashing Symbols (MakeCode MicroPython)

# A very basic program that flashes a sequence of symbols on the onboard LEDs

# Button A plays a sequence of Hearts
# Button B plays a sequence of Smiles

# Would like to develop this program further to run each sequence on a loop of it's own
# And also print some instructions to the screen

import microbit

# The Forever Loop

def on_forever():
    if input.button_is_pressed(Button.A):
        basic.show_icon(IconNames.HEART)
        basic.clear_screen()
        basic.pause(500)
        basic.show_icon(IconNames.SMALL_HEART)
        basic.clear_screen()
        basic.pause(500)
    if input.button_is_pressed(Button.B):
        basic.show_leds("""
            # . . . #
            . . . . .
            . . . . .
            # # # # #
            . # # # .
            """)
        basic.clear_screen()
        basic.pause(500)
        basic.show_leds("""
            # . . . #
            . . . . .
            # # # # #
            # . . . #
            . # # # .
            """)
        basic.clear_screen()
        basic.pause(500)
basic.forever(on_forever)
