# Random Circles

Instructions :

Section 4: Graphics


In this section, our goal is to work on a graphics problem together.

Problem: Random Circles
Write a program that draws a 20 circles at random positions with random colors on the canvas. You are provided with the constants N_CIRCLES (the number of circles to draw), CANVAS_WIDTH and CANVAS_HEIGHT (the width and height of the canvas, respectively) and CIRCLE_SIZE  (the width and height of each circle respectively). Specifically, your job is to implement the following function:

def draw_random_circles(canvas):


which takes as a parameter the canvas that will be used to draw all of the random circles. In order to choose a random color, we have a defined a function for you to use called random_color. It will return a random color that you can use for a given circle. 

def random_color():
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

A call to your function draw_random_circles should produce something that looks like this (of course with randomness yours will have the circles in different locations:

Possible Extensions:

If you find you have extra time you can try adding the following extensions on to this problem

Draw a random number of circles between 1 and 20

Draw circles of a random size 

Draw the circles such that all parts of the circle are within the canvas 


OUTPUT:

![image](https://github.com/Trilochna/Code-In-Place-By-Stanford-University/assets/97858274/b373606e-762e-4926-bf47-b9ea6dd4f066)
