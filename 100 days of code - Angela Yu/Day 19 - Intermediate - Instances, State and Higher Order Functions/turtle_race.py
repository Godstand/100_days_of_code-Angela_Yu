import random
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color.").lower()
colors = ["red", "orange", "green", "yellow", "blue", "purple"]
all_turles = []

# create different turtles
horizontal_coordinate = 100
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=horizontal_coordinate)
    horizontal_coordinate -= 40
    all_turles.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won. The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
screen.exitonclick()