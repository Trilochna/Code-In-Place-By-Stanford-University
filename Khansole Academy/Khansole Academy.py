import random

def generate_problem():
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    return num1, num2

def check_answer(num1, num2, answer):
    expected = num1 + num2
    if answer == expected:
        return True
    else:
        return False

def main():
    print("Khansole Academy")

    while True:
        num1, num2 = generate_problem()
        print("What is", num1, "+", num2, "?")
        user_answer = int(input("Your answer: "))

        if check_answer(num1, num2, user_answer):
            print("Correct!")
        else:
            print("Incorrect.")
            print("The expected answer is", num1 + num2)

        print()

if __name__ == "__main__":
    main()
