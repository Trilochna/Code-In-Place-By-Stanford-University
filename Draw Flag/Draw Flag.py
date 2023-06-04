from graphics import Canvas


CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Draws the Indonesian flag
    canvas.create_rectangle(0,                  # left x
                            0,                  # top y
                            CANVAS_WIDTH,       # right x
                            CANVAS_HEIGHT / 2,  # bottom y
                            "red")              # color
    

if __name__ == '__main__':
    main()
