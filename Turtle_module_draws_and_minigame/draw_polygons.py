import turtle as t
import math
def spiral(segment, count, a=90):
    for i in range(1, count):
        angle = a * i
        length = segment * math.ceil(i / 2)
        t.setheading(angle)
        t.forward(length)
t.speed(100)
t.pensize(2)
segment =3
turns = 150
angle = 75
print("segment=",segment, "turns=", turns, "angle=", angle )
spiral(segment, turns, angle)
t.done()