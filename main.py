def on_button_pressed_a():
    basic.show_number(randint(0, 99))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global letter
    letter = randint(1, 5)
    if letter == 1:
        basic.show_icon(IconNames.NO)
    elif letter == 2:
        basic.show_leds("""
            # . . . .
                        # . . . .
                        # # # . .
                        # . . . .
                        # # # . .
        """)
    elif letter == 3:
        basic.show_leds("""
            # . . . .
                        # . . . .
                        # # # . .
                        # . # . .
                        # # # . .
        """)
    elif letter == 4:
        basic.show_leds("""
            # # # # #
                        # . # . #
                        # . # . #
                        # . # . #
                        # . # . #
        """)
    else:
        basic.show_leds("""
            # . . . .
                        # . . . .
                        # # # . .
                        # . # . .
                        # . # . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global pass2
    pass2 = ""
    for index in range(9):
        pass2 = "" + pass2 + String.from_char_code(randint(33, 122))
    basic.show_string(pass2)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

pass2 = ""
letter = 0
basic.show_string("Press A or B")

def on_forever():
    pass
basic.forever(on_forever)
