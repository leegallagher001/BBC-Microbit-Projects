# BBC Micro:bit - Pet Hamster (MakeCode MicroPython)

# A silly program that turns the Micro:bit into a sleeping pet hamster, that gets
# happy when "petted" (the logo is pressed) and sad when shaken

import microbit

basic.show_icon(IconNames.ASLEEP)

def on_logo_pressed(): # function that makes hamster happy when logo is pressed
    basic.show_icon(IconNames.HAPPY)
    music._play_default_background(music.built_in_playable_melody(Melodies.JUMP_UP),
        music.PlaybackMode.UNTIL_DONE)
    basic.clear_screen()
    basic.show_string("Hello there!", 60) # Best Kenobi impression :D
    basic.show_icon(IconNames.ASLEEP)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_gesture_shake(): # function that makes hamster sad when shaken
    basic.show_icon(IconNames.SAD)
    music._play_default_background(music.built_in_playable_melody(Melodies.DADADADUM),
        music.PlaybackMode.UNTIL_DONE)
    basic.clear_screen()
    basic.show_string("Go Away!", 60)
    basic.show_icon(IconNames.ASLEEP)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
