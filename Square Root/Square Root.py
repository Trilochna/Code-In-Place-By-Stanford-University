"""
This program computes square roots
"""
import math
def main():
    num = float(input("Enter number: "))
    root = math.sqrt(num)
    print("Square root of", num, "is", root)
    
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
