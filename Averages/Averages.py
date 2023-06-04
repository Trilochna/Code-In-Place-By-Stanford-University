def main():
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    final = average(avg_1, avg_2)
    print("avg_1", avg_1)
    print("avg_2", avg_2)
    print("final", final)
    
def average(a, b):
    """
    returns the number which is half way between a and b
    """
    sum = a + b
    return sum / 2
    
if __name__ == '__main__':
    main()
