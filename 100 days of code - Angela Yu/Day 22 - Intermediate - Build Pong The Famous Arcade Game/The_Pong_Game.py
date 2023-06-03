import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("orange")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with the paddles
    if ball.distance(r_paddle) < 40 and ball.xcor() > 360 or ball.distance(l_paddle) < 40 and ball.xcor() > -360:
        ball.bounce_x()

    # detect if ball misses the right paddle and add score
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()
    # detect if ball misses the left paddle and add score
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()
