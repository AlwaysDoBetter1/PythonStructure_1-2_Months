import turtle as T
import random as R
from math import sin, radians

''' --- Function for teleporting the turtle without drawing ---
Arguments:
x, y - coordinates of movement;
d - direction in which the turtle will be rotated.
'''
def tp(x, y, d=None):
    T.penup(), T.goto(x, y), T.pendown()
    if d is not None:
        T.setheading(d)

''' --- Function for drawing a snowflake ---
Arguments:
size - diameter of the snowflake;
rotate - rotation of the snowflake, default is 90°;
color - color of the snowflake, default is white.
'''
def snowflake(size: int, rotate=90, color=('white')):
    T.pensize(size//100+1), T.pencolor(color), T.fillcolor('cadetblue2'), T.setheading(rotate), T.pendown()
    def ray(length, angle, reverse=False, invisible=(False, False)):  # Function for snowflake's component part
        angle /= 2
        sides = (length * sin(radians(angle)) / sin(radians(150 - angle)),
                 length / (2 * sin(radians(150 - angle))))
        pos, direction = T.pos(), T.heading()
        for i in range(2):
            k = (-1) ** i
            T.pendown(), T.left((30, angle)[reverse] * k)
            if invisible[reverse]:
                T.penup()
            T.forward(sides[reverse]), T.pendown(), T.right((30 + angle) * k)
            if invisible[(reverse + 1) % 2]:
                T.penup()
            T.forward(sides[(reverse + 1) % 2])
            tp(*pos, direction)
    pos = T.pos()
    for _ in range(6):  # Draws the rays of the snowflake
        for i in range(3):
            T.begin_fill()
            ray(size - i * size / 4, 30, reverse=True)
            T.end_fill()
            T.penup(), T.forward(size / 6), T.pendown()
            if size < 50:
                break
        tp(*pos), T.left(60)
    for r in range(3):  # Draws the center of the snowflake
        for d in range(2):
            angle = R.randrange(30, 91, 10)
            T.left(30)
            for _ in range(6):
                T.begin_fill()
                ray(size / 2 - r * size / 10, angle, invisible=(True, False))
                T.end_fill()
                T.left(60)
            if size < 50:
                break
    T.penup()

''' --- Function for mouse click action ---
Arguments:
x, y - coordinates where the snowflake will be drawn;
'''
def click(x, y):
    tp(x, y)
    snowflake(R.randrange(20, 200), R.randrange(0, 360), R.choice(colors))

T.Screen().setup(1600, 900), T.bgcolor('cadetblue2'), T.speed(0), T.hideturtle(), T.tracer(4)
colors = ('white', 'snow', 'snow1', 'snow2', 'SteelBlue', 'SteelBlue1', 'SteelBlue2')
# --- Draws a snowflake where the mouse clicks ---
T.Screen().onclick(click)
# --- Draws 50 snowflakes ---
# for _ in range(50):
#     tp(R.randrange(-790, +790), R.randrange(-450, +450))
#     snowflake(R.randrange(20, 200), R.randrange(0, 360), R.choice(colors))
T.done()
