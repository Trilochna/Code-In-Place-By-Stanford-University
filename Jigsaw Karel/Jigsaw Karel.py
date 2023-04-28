from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    
    move()
    move()
    pick_beeper()
    move()
    turn_left()
    for i in range(2):
        move()
    put_beeper()
    for i in range(2):
        turn_left()
    move()
    move()
    turn_right()
    for i in range(3):
        move()
    for i in range(2):
        turn_right()



def turn_right():
  for i in range(3):
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
