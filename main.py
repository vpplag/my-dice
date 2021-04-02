Roll = 0

def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global Roll
    Roll = randint(1, 6)
    if Roll == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    else:
        if Roll == 2:
            basic.show_leds("""
                . . . . #
                . . . . .
                . . . . .
                . . . . .
                # . . . .
                """)
        else:
            if Roll == 3:
                basic.show_leds("""
                    . . . . #
                    . . . . .
                    . . # . .
                    . . . . .
                    # . . . .
                    """)
            else:
                if Roll == 4:
                    basic.show_leds("""
                        # . . . #
                        . . . . .
                        . . . . .
                        . . . . .
                        # . . . #
                        """)
                else:
                    if Roll == 5:
                        basic.show_leds("""
                            # . . . #
                            . . . . .
                            . . # . .
                            . . . . .
                            # . . . #
                            """)
                    else:
                        basic.show_leds("""
                            # . . . #
                            . . . . .
                            # . . . #
                            . . . . .
                            # . . . #
                            """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
