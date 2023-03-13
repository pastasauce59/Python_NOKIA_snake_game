from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
         self.segments = []
         self.create_snake()
         self.head = self.segments[0]

    def create_snake(self):
        xaxis = 0
        for _ in range(0,3):
            new_snake = Turtle('square')
            new_snake.color('white')
            new_snake.penup()
            new_snake.goto(x=xaxis, y=0)
            xaxis -= 20
            self.segments.append(new_snake)

    def move(self):
        for snake_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake_num - 1].xcor()
            new_y = self.segments[snake_num - 1].ycor()
            self.segments[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        # self.head.left(30)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
