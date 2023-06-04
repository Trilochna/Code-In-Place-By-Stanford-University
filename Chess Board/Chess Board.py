from graphics import Canvas
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = CANVAS_WIDTH
N_ROWS = 8
N_COLS = N_ROWS
SIZE = CANVAS_WIDTH / N_ROWS

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for r in range(N_ROWS):
        for c in range(N_COLS):
            draw_square(canvas, r, c)
            
def draw_square(canvas, r, c):
    print(r, c)
    color = get_color(r, c)
    x = c * SIZE
    y = r * SIZE
    end_x = x + SIZE
    end_y = y + SIZE
    
    canvas.create_rectangle(x, y, end_x, end_y, color, 'black')
            
        
def get_color(r, c):
    if is_even(r+c):
        return "green"
    else:
        return "beige"
        
def is_even(value):
    return value % 2 == 0
            
if __name__ == '__main__':
    main()
