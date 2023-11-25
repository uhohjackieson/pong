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

screen = Screen()
screen.title("PONG")
turtle = Turtle()

screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.exitonclick()
