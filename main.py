from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Classic Nokia 3310 Snake Game - In Python')
screen.tracer(0)

snake_segments = []

xaxis = 0
for _ in range(0,3):
    new_snake = Turtle('square')
    new_snake.color('white')
    new_snake.penup()
    new_snake.goto(x=xaxis, y=0)
    xaxis -= 20
    snake_segments.append(new_snake)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for snake in snake_segments:
        snake.forward(20)

screen.exitonclick()