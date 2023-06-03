# Moving Square

from graphics import Canvas
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SQUARE_SIZE = 40
VELOCITY = 2
DELAY = 0.01

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    start_x = 0
    start_y = CANVAS_HEIGHT / 2 - SQUARE_SIZE / 2
    square = canvas.create_rectangle(start_x, start_y,
                    SQUARE_SIZE,
                    start_y + SQUARE_SIZE)
                    
    while (start_x + SQUARE_SIZE / 2) < (CANVAS_WIDTH / 2):
        start_x += VELOCITY
        print("x:", start_x)
        canvas.moveto(square, start_x, start_y)
        time.sleep(DELAY)
        
    print("Done!")

if __name__ == '__main__':
    main()
