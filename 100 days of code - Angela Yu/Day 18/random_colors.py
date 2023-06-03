import turtle
from turtle import Turtle, Screen
import random

lines = Turtle()
turtle.colormode(255)

def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors

directions = [0, 90, 180, 270, 360]
lines.pensize(15)
# lines.speed("fastest")

for _ in range(200):
    lines.color(random_colors())
    lines.forward(40)
    lines.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()