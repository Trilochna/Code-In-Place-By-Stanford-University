"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

def main():
    print("This program multiplies two numbers.")
    # your code here
    
    # Prompt the user to enter the first number.
    num1 = input("Enter first number: ")

    # Convert the first input to an integer.
    num1 = int(num1)

    # Prompt the user to enter the second number.
    num2 = input("Enter second number: ")

    # Convert the second input to an integer.
    num2 = int(num2)

    # Multiply the two numbers.
    result = num1 * num2

    # Print the result.
    print(result)



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
