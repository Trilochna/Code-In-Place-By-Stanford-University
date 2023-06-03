import graphics

def main():
    # makes a canvas
    canvas = graphics.create_canvas(300, 300)
    # make 20 some blue suares
    for i in range(20):
        value = i * 10
        # it can be helpful to store each coord into its own variable
        left_x = value
        top_y = value
        right_x = value + 10
        bottom_y = value + 10
        canvas.create_rectangle(left_x,top_y,right_x,bottom_y, 'blue')
        
        # keep track of i
        print(i)
        
if __name__ == '__main__':
    main()
