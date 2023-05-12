"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

# We use constants!
MARS_MULTIPLE = 0.378

def main():
    earth_weight_str = input('Enter a weight on Earth: ')

    # Get the numeric value since input() returns a value in string form
    earth_weight = float(earth_weight_str)

    # Having a variable for each piece of information is a good habit
    mars_weight = earth_weight * MARS_MULTIPLE
    rounded_mars_weight = round(mars_weight, 2)


    # Note the string concatenation!
    print('The equivalent weight on Mars: ' + str(rounded_mars_weight))

if __name__ == '__main__':
    main()
