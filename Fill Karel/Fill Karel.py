from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

def main():
    while no_beepers_present():
        make_row()
        check_next_row()

def check_next_row():
    while front_is_blocked():
        turn_left()
    while front_is_clear():
        move()
    turn_right()
    if front_is_clear():
        move()
        turn_right()
    else:
        turn_right()
        while front_is_clear():
            move()

def make_row():
    while front_is_clear():
        while no_beepers_present():
            put_beeper()
        move()
        put_beeper()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
