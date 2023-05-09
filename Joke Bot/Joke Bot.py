PROMPT = "What do you want? "
JOKE = "Here is a joke for you! Karel is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Karel returns with 13 liters of milk. The programmer asks why and Karel replies: 'because they had eggs'"
SORRY = "Sorry I only tell jokes"

def main():
    user_input = input(PROMPT)
    if user_input == "Joke":
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()
