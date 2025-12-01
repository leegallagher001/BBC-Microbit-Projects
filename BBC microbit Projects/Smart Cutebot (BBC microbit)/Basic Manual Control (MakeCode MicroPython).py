# Smart Cutebot (BBC micro:bit) - Basic Manual Control (MakeCode MicroPython)

# This program allows the user to, in a very basic fashion, manually control the Cutebot robot with the
# Micro:bit and the "Lofi Control" app (this is best done using a smartphone)

# Would definitely like to improve upon this one in future, as at the moment the user needs to keep inputting
# the movement they want continuously - can't just hold down a directional key/button

# Best flashed onto the BBC micro:bit from the Microsoft MakeCode website - https://makecode.microbit.org/

# Imports

from microbit import *
import cuteBot

# Main Code

controlInput = ""
bluetooth.start_uart_service() # initialises bluetooth input
basic.show_icon(IconNames.SILLY) # silly face, because I felt silly trying to get this to work

def on_uart_data_received():
    global controlInput
    controlInput = bluetooth.uart_read_until(serial.delimiters(Delimiters.NEW_LINE)) # when new line is detected
    if controlInput == "up":
        cuteBot.move_time(cuteBot.Direction.FORWARD, 30, 1) # moves forward 30% speed for 1 second
    if controlInput == "down":
        cuteBot.move_time(cuteBot.Direction.BACKWARD, 30, 1) # back 30% 1 second
    if controlInput == "right":
        cuteBot.move_time(cuteBot.Direction.RIGHT, 30, 0.1) # right 30% 0.1 second (for precise turning)
    if controlInput == "left":
        cuteBot.move_time(cuteBot.Direction.LEFT, 30, 0.1) # left 30% 0.1 second
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.NEW_LINE),
    on_uart_data_received)
