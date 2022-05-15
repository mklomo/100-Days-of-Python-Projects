from turtle import Turtle

STARTING_Y_POSITION = ((0, 0), (-20, 0), (-40, 0))

MOVE_DISTANCE = 10

UP = 90

DOWN = 270

LEFT = 180

RIGHT = 0

class Snake:

    def __init__(self):
        self.up = None
        self._snake_segments = []
        self.create_snake()
        self._head = self._snake_segments[0]

    def create_snake(self):
        for position in STARTING_Y_POSITION:
            self.add_segment(position)
            

    def motion(self):
        for seg_num in range(len(self._snake_segments) - 1, 0, -1):
            new_x = self._snake_segments[seg_num - 1].xcor()
            new_y = self._snake_segments[seg_num - 1].ycor()
            self._snake_segments[seg_num].goto(x=new_x, y=new_y)
        self._head.forward(MOVE_DISTANCE)
        
    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self._snake_segments.append(snake)
    
    def extend(self):
        self.add_segment(self._snake_segments[-1].position())

    def move_up(self):
        if self._head.heading() != DOWN:
            self._head.setheading(UP)

    def move_down(self):
        if self._head.heading() != UP:
            self._head.setheading(DOWN)

    def move_left(self):
        if self._head.heading() != RIGHT:
            self._head.setheading(LEFT)

    def move_right(self):
        if self._head.heading() != LEFT:
            self._head.setheading(RIGHT)

    def reset(self):
        for segment in self._snake_segments:
            segment.goto(1000, 1000)
        self._snake_segments.clear()
        self.create_snake()
        self._head = self._snake_segments[0]
