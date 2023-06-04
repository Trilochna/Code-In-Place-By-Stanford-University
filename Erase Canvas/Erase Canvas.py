"""
This program implements an 'eraser' on a canvas. 

The canvas consists of a grid of blue 'cells' which are drawn 
as rectangles on the screen. We then create an eraser rectangle
which, when dragged around the canvas, sets all of the rectangles 
it is in contact with to white.
"""

from graphics import Canvas
import time
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""
    pass


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    num_rows = CANVAS_HEIGHT // CELL_SIZE  # figure out how many rows of cells we need
    num_cols = CANVAS_WIDTH // CELL_SIZE   # figure out how many columns of cells we needd
    
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE   # The right coordinate of the cell is CELL_SIZE pixels away from the left
            bottom_y = top_y + CELL_SIZE   # The bottom coordinate of the cell is CELL_SIZE pixels away from the top
            
            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')
            
            
    canvas.wait_for_click()  # wait for the user to click before creating the eraser
    
    last_click_x, last_click_y = canvas.get_last_click()
    
    eraser = canvas.create_rectangle(
        last_click_x, 
        last_click_y, 
        last_click_x + ERASER_SIZE, 
        last_click_y + ERASER_SIZE, 
        'pink'
    )
    
    while True:
        # move the eraser, and erase what it's touching
        
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        
        erase_objects(canvas, eraser)  # we need to implement this!
        
        time.sleep(0.05)
        

if __name__ == '__main__':
    main()
