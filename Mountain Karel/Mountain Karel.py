from karel.stanfordkarel import *

"""
File: Mountain.py
----------------------------
Karel climbs a mountain of any size
and plants a beeper at the top
"""

def main():
    climb_mountain()
    put_beeper()
    descend_mountain()
    

def climb_mountain():
    """
    Pre: Karel is at the base of a mountain
    Post: Karel is standing at the top.
    Karel's front will only be clear when karel
    is at the top
    """
    while front_is_blocked():
        step_up()
        
        
def descend_mountain():
    """
    Pre: Karel is at the top of a mountain
    Post: Karel is on the other side
    Karel's front will only be blocked when
    Karel is at the base, facing the far right wall
    """
    while front_is_clear():
        step_down()


def step_down():
    """
    Take one step down. In both Pre/Post Karel is 
    facing right (East)
    """
    move()
    turn_right()
    move()
    turn_left()
    
    
def step_up():
    """
    Take one step up. In both Pre/Post Karel is 
    facing right (East)
    """
    turn_left()
    move()
    turn_right()
    move()


def turn_right():
    """
    Makes karel turn in the clock-wise direction.
    Works in any pre-condition state!
    """
    for i in range(3):
        turn_left()


if __name__ == '__main__':
    main()
