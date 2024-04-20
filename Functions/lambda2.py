'''
In the RGB color scheme, colors are specified using three components:

R is the intensity of the red component of the color;
G is the intensity of the green component of the color;
B is the intensity of the blue component of the color.
The opposite colors are specified as RGB and (255-R)(255-G)(255-B). It is believed that these colors harmonize
well with each other.

Write a program that, given three components of a given color, finds components of the opposite color.

Input format
The input to the program is a string containing three non-negative integers, components R, G and B of the initial
color, separated by a space character.

Output format
The program should output three components R, G and B of opposite colors, separated by a space character.
'''

print(*map(lambda x: 255 - int(x), input().split()))

# input
# 244 11 120
# output
# 11 244 135

