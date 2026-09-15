import turtle
from math import sin, cos, radians, pi
import random as r
from time import perf_counter

turtle.colormode(255)
r.seed(78)

#CONSTANTS
RAND_CONST_R = r.random()
RAND_CONST_G = r.random()
RAND_CONST_B = r.random()

RADIUS = 100
INCREMENT = 4
CIRCLE_STEPS = int(360 / INCREMENT) + 1
NUM_OF_CIRCLES = 64
PEN_SIZE = 1
TURTLE_SPEED = 0
WIDTH = 400
HEIGHT = 400

#SCREEN
sc = turtle.Screen()
sc.setup(width = WIDTH, height = HEIGHT)
sc.bgcolor("white")

#DEFAULT TURTLE SETTINGS
start = perf_counter()

t = turtle.Turtle()
t.hideturtle()
t.speed(TURTLE_SPEED)
t.fillcolor("")
t.pen(pendown = True, pensize = PEN_SIZE, pencolor = "black")

x_coords = []

for x in range(1, CIRCLE_STEPS):
    angle = radians(INCREMENT * x)

    x_coords.append(
        (
            RADIUS * cos(angle),
            RADIUS * sin(angle)
        )
    )

#SPIROGRAPH
for g in range(1, NUM_OF_CIRCLES + 1):

    circle_step = 2 * pi * g / NUM_OF_CIRCLES

    offset_x = RADIUS * cos(circle_step)
    offset_y = RADIUS * sin(circle_step)

    theta_r = -circle_step + radians(360 * RAND_CONST_R)
    theta_g = -circle_step + radians(360 * RAND_CONST_G)
    theta_b = -circle_step + radians(360 * RAND_CONST_B)

    t.teleport(RADIUS - offset_x, -offset_y)

    for x in range(1, CIRCLE_STEPS):
        goto_coords_x, goto_coords_y = x_coords[x - 1]

        angle = radians(INCREMENT * x)

        red = int(abs(255 * sin(angle + theta_r)))
        green = int(abs(255 * sin(angle + theta_g)))
        blue = int(abs(255 * sin(angle + theta_b)))

        t.pencolor(red, green, blue)

        t.goto(goto_coords_x - offset_x, goto_coords_y - offset_y)

end = perf_counter()

print(f"Time to display: {end - start}")

sc.exitonclick()