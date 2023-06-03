import turtle
from turtle import Turtle, Screen
import random


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


lines = Turtle()
lines.pensize(5)
turtle.colormode(255)
lines.speed("fastest")

size_of_gap = int(input("what is the size of the gap between each circle?: "))


def draw_spirograph(size_of_gap):
    num_circle = int(360 / size_of_gap)
    lines.circle(120)
    for _ in range(num_circle):
        lines.color(random_colors())
        lines.circle(100)
        current_heading = lines.heading()
        lines.setheading(current_heading + size_of_gap)


draw_spirograph(size_of_gap)

screen = Screen()
screen.exitonclick()
