from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.
def main():
    move()
    # your code here
    
    while front_is_clear():
        for i in range(10): 
            if beepers_present():
                pick_beeper()
            if no_beepers_present():
                move()
                
        


   
   # beepers_present()
# no_beepers_present()

   # front_is_clear()

# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
