def add_five(x):
    x += 5
    return x
    
def add_five_buggy(x):
    x += 5
    
def main():
    x = 3
    print("original:", x)
    
    add_five_buggy(x)
    print("after add_five_buggy:", x)
    
    x = add_five(x)
    print("after add_five:", x)
    
if __name__ == '__main__':
    main()
