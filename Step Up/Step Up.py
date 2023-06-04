# This tells PyCharm who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *

# this program executes in a special function called main
def main():
    move()
    
    pick_beeper()
    
    move()
    
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()

    move()
    put_beeper()
    move()


# This is "boilerplate" code which launches your code
# when you hit the run button
if __name__ == '__main__':
    main()
