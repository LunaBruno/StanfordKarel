from stanfordkarel import *


def main():

    while front_is_clear():
        if right_is_blocked():
            move()
        else:
            turn_right()
            move()

    if right_is_blocked():
        turn_left()
    else:
        turn_right()

    while front_is_clear():
        if right_is_blocked():
            move()
        else:
            turn_right()
            move()

    if right_is_blocked():
        turn_left()
    else:
        turn_right()

    while front_is_clear():
        if right_is_blocked():
            move()
        else:
            turn_right()
            move()

    if right_is_blocked():
        turn_left()
    else:
        turn_right()

    while front_is_clear():
        if right_is_blocked():
            move()
        else:
            turn_right()
            move()

    if right_is_blocked():
        turn_left()

    if right_is_blocked():
        turn_left()

    while front_is_clear():
        if right_is_blocked():
            move()
        else:
            turn_right()
            move()


if __name__ == "__main__":
    run_karel_program()


def turn_right():
    for contador in range(3):
        turn_left()
