from graphics import Canvas
import time

CANVAS_SIZE = 400
PAUSE_TIME = 1/50

def main():
    canvas = Canvas(CANVAS_SIZE, CANVAS_SIZE)
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        time.sleep(PAUSE_TIME)
        print("Mouse location: (" + str(mouse_x) + ", " + str(mouse_y) + ")")

if __name__ == '__main__':
    main() 
