from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Classic Nokia 3310 Snake Game - In Python')

xaxis = 0
for _ in range(0,3):
    new_snake = Turtle('square')
    new_snake.color('white')
    new_snake.goto(x=xaxis, y=0)
    xaxis -= 20

    




screen.exitonclick()