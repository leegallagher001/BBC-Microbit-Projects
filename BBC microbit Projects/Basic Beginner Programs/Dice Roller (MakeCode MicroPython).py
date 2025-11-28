# BBC Micro:bit - Dice Roller (MakeCode MicroPython)

# A program that uses the Micro:bit's built-in LEDs and motion sensors to function
# as a virtual dice

# When the Micro:bit is shaken, a random number "dice_roll" between 1 and 6 is generated
# which is then shown on the LEDs. Depending on the number, a happy or sombre tune is
# played and the screen flashes to the number of times of the dice roll number


import microbit

dice_roll = 0 # define dice roll (random number) variable

def on_gesture_shake(): # function for when device is shaken
    global dice_roll
    dice_roll = randint(1, 6) # random number between 1 and 6 generated
    basic.show_number(dice_roll) # show number on screen
    if dice_roll <= 3: # sad tune if number is between 1 and 3
        music._play_default_background(music.built_in_playable_melody(Melodies.WAWAWAWAA),
            music.PlaybackMode.IN_BACKGROUND)
    else: # happy tune if between 4 and 6
        music._play_default_background(music.built_in_playable_melody(Melodies.ENTERTAINER),
            music.PlaybackMode.IN_BACKGROUND)
    basic.pause(1000) # pause for 1 second
    for i in range(0, dice_roll): # for range of dice roll number
        basic.clear_screen() # clear screen
        basic.pause(300) # 0.3 second pause
        # then all LEDs light up for 0.3 seconds
        # this repeats the same number of times as the dice roll number
        basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)
        basic.clear_screen()
        basic.pause(300)
input.on_gesture(Gesture.SHAKE, on_gesture_shake) # implement above function
# when Micro:bit is shaken
