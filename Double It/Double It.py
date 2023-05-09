def main():
    """
    You should write your code here. 
    """
    global curr_value
    curr_value = int(input("Enter a number: "))

    while curr_value < 100:
        print(curr_value * 2)
        curr_value = curr_value * 2

if __name__ == '__main__':
    main()
