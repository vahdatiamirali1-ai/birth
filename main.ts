input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music.setVolume(1000)
    basic.showIcon(IconNames.Heart)
    music.play(music.stringPlayable("C5 B A G F E G D ", 214), music.PlaybackMode.LoopingInBackground)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    music.setVolume(0)
})
