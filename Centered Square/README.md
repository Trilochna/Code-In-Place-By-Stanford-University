# Centered Square

Instructions
Write a program that draws a square, 200 pixels wide, by 200 pixels high, right in the center of the canvas. Warning: this example involves a little math. But it is math worth knowing!



This program is hard, because the first attempt that most students try does not work. It is tempting to try to place the square in the middle by setting the first two parameters of create_rectangle to be middle_x and middle_y:



middle_x = CANVAS_WIDTH/2
middle_y = CANVAS_HEIGHT/2
    
# calculate the right and bottom of the square
right_x = middle_x + SQUARE_SIZE
bottom_y = middle_y + SQUARE_SIZE
    
# draw the square
canvas.create_rectangle(middle_x, middle_y, right_x, bottom_y, 'blue')


However, instead of putting the square in the middle, this puts the top left corner of the square in the middle of the canvas.

![image](https://github.com/Trilochna/Code-In-Place-By-Stanford-University/assets/97858274/c10febe7-04f3-405e-ae13-f7ccc141634a)

Oops. We need to subtract a few pixels from the first two coordinates. How many? exactly half the size of the square in either direction. This code works correctly:

# get the middle of the canvas
middle_x = CANVAS_WIDTH/2
middle_y = CANVAS_HEIGHT/2
    
# calculate the top left corner position
left_x = middle_x - SQUARE_SIZE/2
top_y = middle_y - SQUARE_SIZE/2
    
# calculate the right and bottom of the square
right_x = left_x + SQUARE_SIZE
bottom_y = top_y + SQUARE_SIZE

![image](https://github.com/Trilochna/Code-In-Place-By-Stanford-University/assets/97858274/1cb0b738-d97d-4262-9ebc-61dcef239abf)

