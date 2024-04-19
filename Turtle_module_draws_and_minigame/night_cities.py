from turtle import *
import random as r
import math as m


def settings(show, sp, up, sh, pos, sz, b_col, trace):
    # show(True\False)|sp(int)|up(True\False)|sh(str)|pos(tuple)|sz(int)|b_col(str)
    if not show:
        hideturtle()
    if up:
        penup()
    Screen().colormode(255)  # нужно закомментировать для Trinket
    params = [speed(sp), shape(sh), goto(pos), pensize(sz), Screen().bgcolor(b_col), tracer(trace), delay(0)]


def star(size, col, dest):
    star_defaults = [setpos(dest[0] - size, dest[1]), pencolor(col), pensize(1), pd()]
    gran = size / 4 * m.sqrt(10)
    a = m.degrees(m.atan(1 / 4))
    b = 90 - a * 2
    c = 180 - a * 2
    angle = r.randint(0, 180)
    lt(angle)
    draw_st = [lt(a), begin_fill(), fillcolor(col), [[fd(gran), lt(b), fd(gran), rt(c)] for _ in range(4)],
                end_fill(), pu(), rt(a)]
    rt(angle)


def rain_stars(x, y, coordinates):
    attempt_counter = 0
    while attempt_counter < 10 ** 5 * 2:
        if attempt_counter > 10 ** 3:
            size_k = (10, 15)
        else:
            size_k = (15, 21)
        size = r.randrange(*size_k)
        dest = (r.randint(*x), r.randint(*y))
        math_coord = tuple([dest[i] + size * j for i in [0, 1] for j in [-5, 5]])
        condition = [any([math_coord[0] > c[1], math_coord[1] < c[0], math_coord[2] > c[3],
                          math_coord[3] < c[2]]) for c in coordinates.values()]
        if all(condition):
            col = (255, 255, 205)
            star(size, col, dest)
            update()
            coordinates[dest] = math_coord
            if attempt_counter < 10 ** 4:
                attempt_counter = 0
            else:
                attempt_counter = 10 ** 4
        else:
            attempt_counter += 1


def figure(size, color, dest, end, color_wind):
    figure_defaults = [goto(dest), pd(), pencolor('black')]
    if not end:
        poly_x = [begin_fill(), fillcolor(color), [setx(dest[0] + size), sety(dest[1] + size), setx(dest[0]),
                                                   sety(dest[1])], end_fill(), pu()]
    if end == 1:
        if color_wind is not None:
            poly_x = [pensize(size / 8), pencolor('grey'), begin_fill(), fillcolor(color_wind),
                     [setx(dest[0] + size), sety(dest[1] + size), setx(dest[0]), sety(dest[1])], end_fill(), pu()]
        else:
            poly_x = [pensize(size / 8), pencolor('grey'),
                     [setx(dest[0] + size), sety(dest[1] + size), setx(dest[0]), sety(dest[1])], pu()]
    if end >= 2:
        poly_x = [pencolor('grey'), pensize(size / 8), begin_fill(), fillcolor('grey'),
                [setx(dest[0] + size), sety(dest[1] + size), setx(dest[0]), sety(dest[1])], end_fill(), pu()]


def draw_panelka(size, start, panel_height):
    panel_weight = 70
    end_pan = 0
    for y_range, x_range in zip([panel_height, panel_height // 10 - 1], [panel_weight, panel_weight // 10]):
        num_square = 0
        col_wind = None
        for y in [start[1] + size * i for i in range(y_range)]:
            num_square += 1
            if end_pan == 1:
                num_square = 0
            for x in [start[0] + size * j for j in range(x_range)]:
                dest = (x, y)
                col = [(145, 170, 200), (110, 135, 160)][num_square % 2]
                if end_pan == 1:
                    if y >= start[1] + size * (panel_height // 10 - 2):
                        end_pan = 2
                if end_pan == 1 and num_square in [1, 4, 2, 5]:
                    col_wind = r.choice([(32, 32, 32), (32, 32, 32), (32, 32, 32), (255, 250, 100)])
                figure(size, col, dest, end_pan, col_wind)
                col_wind = None
                num_square += 1
            update()
        end_pan = 1
        size *= 10
        start[1] += size


def night_sity(size, coordinates):
    for w, h in zip([-650 + size * 72 * i for i in range(6)], [-410] * 6):
        height = r.choice([70, 110])
        draw_panelka(size, [w, h], height)
        rain_stars((w + 20, w + size * 72 - 20), (-410 + size * height + 20, 350), coordinates)


settings(False, 0, True, 'turtle', (0, 0), None, (15, 20, 45), 0)
coordinates = {(0, 0): (0, 0, 0, 0)}
night_sity(3, coordinates)
end = input('For exit enter any character\n')