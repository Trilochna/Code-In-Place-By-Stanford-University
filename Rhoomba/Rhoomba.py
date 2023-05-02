# This tells PyCharm who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *

def main():
    """
    Clear the world, row by row. Each time a row is
    cleared, reset to the start of the row to create
    a consistent pre/post of the while loop
    Left is clear until you are on the top row
    """
    while left_is_clear():
        # while loop always assumes that karel is facing
        # right (east)
        clear_row()
        reset_to_next_row()
    # fence-post
    clear_row()
    
    
def clear_row():
    """
    Clear an entire row
    """
    while front_is_clear():
        clear_corner()
        move()
    # fence-post
    clear_corner()
    
    
def clear_corner():
    """ 
    Only works if there are zero or one beepers
    present
    """
    if beepers_present():
        pick_beeper()
        
        
def reset_to_next_row():
    """
    Pre: Karel is at the end of a row, facing right (east)
    Post: Karel is at the start of the next row, facing right (east)
    """
    turn_around()
    move_to_wall()
    turn_right()
    move()
    turn_right()
    

def move_to_wall():
    while front_is_clear():
        move()
    
    
def turn_right():
    for i in range(3):
        turn_left()
        
        
def turn_around():
    turn_left()
    turn_left()



# This is "boilerplate" code which launches your code
# when you hit the run button
if __name__ == '__main__':
    main()
