#need a class for scoreboard, paddles, ball

# create the screen
# create and move a paddle
# create another paddle
# create the ball and make it move
# detect collision with ball and bounce
# detect collision with paddle
# detect when paddle misses
# keep score

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("PONG")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# x_pos = 350
# y_pos = 0
#
# right_paddle.goto(x_pos, y_pos)
# left_paddle.goto(-350, 0)
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        print("made contact")
        ball.bounce_x()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when paddle misses
    if ball.xcor() > 380:
        print("paddle misses")
        ball.reset_ball()

    if ball.xcor() < -380:


    # keep score

screen.exitonclick()
