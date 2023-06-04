def main():
    door = int(input("Door: ")) # while the input is invalid 
    while door < 1 or door > 3 :
       # tell the user the input was invalid
       print("Invalid door!")
       # ask for a new input
       door = int(input("Door: "))
    
    prize = 4
    if door == 1:
        prize = 2 + 9 // 10 * 100
    elif door == 2:
        locked = prize % 2 != 0 
        if not locked:
            prize += 6
    elif door == 3 :
        for i in range(door):
            prize += i
    print("You win", prize, "prizes")
            
if __name__ == '__main__':
    main()
