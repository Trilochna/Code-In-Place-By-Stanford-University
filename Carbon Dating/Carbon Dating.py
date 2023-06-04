import math

K = -8266.64

def main():
    calculate_age_single_sample()

def calculate_age_single_sample():
    # ask the user to enter the percent c14 left in their sample
    pct_left = float(input("% of natural c14: "))
    # calc the age    
    age = K * math.log(pct_left / 100)
    # print the result    
    print("Sample is " + str(age) + " years old.")

if __name__ == '__main__':
    main()
