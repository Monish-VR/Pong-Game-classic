from turtle import   Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

ball = Ball()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
screen.listen()
is_game_on = True
score = Score()


screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)

screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.refresh()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        ball.increase()
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.bounce_x()
        ball.refresh()
        score.r_point()
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.bounce_x()
        ball.refresh_new()
        score.l_point()

screen.exitonclick()
