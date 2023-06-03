from turtle import Turtle, Screen

lines = Turtle()

for _ in range(15):
    lines.forward(10)
    lines.penup()
    lines.forward(10)
    lines.pendown()

screen = Screen()
screen.exitonclick()