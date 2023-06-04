import random

def main():
    secret_number = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99...")
    guess = int(input("Enter a guess: "))
    # True if guess is not equal to secret number
    while guess != secret_number:
        # True if guess is less than secret number
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
            
        print("") # an empty line
        guess = int(input("Enter a new guess: "))
        
    print("Congrats! The number was: " + str(secret_number))
    
if __name__ == '__main__':
    main()
