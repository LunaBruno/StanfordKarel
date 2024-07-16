from stanfordkarel import *


def main():
    put_beeper()
    put_beeper()
    move()


if __name__ == "__main__":
    run_karel_program()


def varrer_zig_zag():
    for contador in range(3):
        move_to_wall()
        turn_left()
        move()
        turn_left()

        move_to_wall()
        turn_right()
        move()
        turn_right()

    move_to_wall()
    turn_left()
    move()
    turn_left()
    move_to_wall()
    turn_left()
    move_to_wall()
    turn_left()


def move_to_wall():
    while front_is_clear():
        move()


def turn_around():
    for contador in range(2):
        turn_left()


def turn_right():
    for contador in range(3):
        turn_left()


def varrer_borda_anti_horario():
    for contador in range(4):
        move_to_wall()
        turn_left()


def varrer_borda_horario():
    turn_left()
    move_to_wall()

    for contador in range(3):
        turn_right()
        move_to_wall()

    turn_left()
    turn_left()
