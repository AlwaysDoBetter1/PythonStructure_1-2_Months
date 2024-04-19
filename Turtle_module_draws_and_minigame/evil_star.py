import turtle as t
from turtle import *
def my_circle(r):
    pendown()
    speed(100)
    for i in range(16, 76):
        pensize(i // 6)
        circle(r, 6, 6)
    penup()

def line(length, size):
    for _ in range(length//2):
        pensize(size)
        forward(2)
        size += 0.01
    return size
hideturtle()
shape('turtle')
bgcolor('black')
pencolor('darkred')
my_circle(140)
goto(xcor(), ycor() + 40)
vertex = pos()
my_circle(100)
pendown()
circle(100, 30, 76//6)
penup()
goto(vertex)
size = 3
setheading(72)
vertex = []
pendown()
for _ in range(5):
    vertex.append(pos())
    size = line(190, size)
    left(144)
penup()
setheading(270)
for v in vertex:
    goto(v)
    forward(15)
    stamp()
    setheading(heading() + 144)
goto(vertex[0][0], (vertex[1][1] + vertex[0][1])/2)
setheading(90)
shapesize(2, 2)
stamp()
done()