from graphics import Canvas
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 450
BALL_DIAMETER = 30
INITIAL_VELOCITY = 5
START_X = 0
START_Y = 0
DELAY = 0.001

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    x_velocity = INITIAL_VELOCITY
    y_velocity = INITIAL_VELOCITY
    ball_x = START_X
    ball_y = START_Y
    ball = canvas.create_oval(ball_x, ball_y,
                              ball_x + BALL_DIAMETER,
                              ball_y + BALL_DIAMETER,
                              'blue')
                              
    while True:
        if (ball_x < 0) or (ball_x + BALL_DIAMETER >= CANVAS_WIDTH):
            x_velocity = -x_velocity
        if (ball_y < 0) or (ball_y + BALL_DIAMETER >= CANVAS_HEIGHT):
            y_velocity = -y_velocity
        ball_x += x_velocity
        ball_y += y_velocity
        canvas.moveto(ball, ball_x, ball_y)
        time.sleep(DELAY)

if __name__ == '__main__':
    main()
