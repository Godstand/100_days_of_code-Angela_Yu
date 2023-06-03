from turtle import Turtle, Screen
import random

lines = Turtle()
colors = ["cornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "slateGray", "SeaGreen"]
# num_sides = int(input("what's the number of size? "))
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        lines.forward(100)
        lines.right(angle)

for shape_side_n in range(3, 10):
    lines.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()