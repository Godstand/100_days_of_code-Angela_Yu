from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("yellow3")

for _ in range(4):
    timmy_the_turtle.forward(200)
    timmy_the_turtle.left(90)

screen = Screen()
screen.exitonclick()
