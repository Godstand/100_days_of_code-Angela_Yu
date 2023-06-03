from turtle import Turtle, Screen
import random

lines = Turtle()
colors = ["cornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "slateGray", "SeaGreen"]
directions = [0, 90, 180, 270, 360]
lines.pensize(15)
lines.speed("fastest")

for _ in range(200):
    lines.color(random.choice(colors))
    lines.forward(40)
    lines.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()