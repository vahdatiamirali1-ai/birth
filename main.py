def on_button_pressed_a():
    music.set_volume(1000)
    basic.show_icon(IconNames.HEART)
    music.play(music.string_playable("C5 B A G F E G D ", 214),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    music.set_volume(0)
input.on_button_pressed(Button.B, on_button_pressed_b)
