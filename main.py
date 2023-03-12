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

    # for snake_num in range(start= 2, stop= 0, step= -1):
    for snake_num in range(len(snake_segments) - 1, 0, -1):
        new_x = snake_segments[snake_num - 1].xcor()
        new_y = snake_segments[snake_num - 1].ycor()
        snake_segments[snake_num].goto(new_x, new_y)
    snake_segments[0].forward(20)
    snake_segments[0].left(30)
screen.exitonclick()