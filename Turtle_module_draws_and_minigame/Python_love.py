import math as m
import turtle as t


def go(x0, y0):
    t.up()
    t.goto(x0, y0)
    t.down()


def move(x0, y0):
    x, y = t.pos()
    go(x + x0, y + y0)


def draw_heart(k, pen='Black', fill='Red', xcor=0, ycor=0):
    t.color(pen, fill)
    t.begin_fill()
    for s in range(630):
        s *= 0.01
        x = 128 * m.sin(s) ** 3 + xcor
        y = 8 * (13 * m.cos(s) - 5 * m.cos(2 * s) - 2 * m.cos(3 * s) - m.cos(4 * s) - 5) + ycor
        t.goto(x * k, y * k)
    t.end_fill()


def Heart(size):
    # Window params
    t.Screen().title('<!3')
    t.Screen().setup(720, 720)
    t.Screen().colormode(255)
    t.bgcolor(20, 0, 10)
    t.width(size * 0.05)
    t.tracer(2)
    t.ht()

    go(0, size)
    draw_heart(size / 48, pen='Red', fill='Red', ycor=size / 2)
    draw_heart(size / 50, pen='White', fill='Red', ycor=size / 2)

    t.pencolor('White')
    go(0, -size * 2)
    t.write('!', align='center', font=('simsun', int(size * 2.3), 'bold'))
    go(0, size * 2.5)
    t.write('Python', align='center', font=('Intro', size // 2))
    t.pencolor('Red')
    go(0, -size * 3.2)
    t.write('                          ', align='center', font=('Intro', size // 2, 'underline'))
    t.pencolor('White')
    move(0, -size / 3.5)
    t.write('Love is War', align='center', font=('Intro', size // 2,))


crop = 100
Heart(crop)
t.done()