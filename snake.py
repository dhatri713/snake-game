from turtle import Turtle

FORWARD_DISTANCE = 20
SHAPE = "square"
COLOR = "white"
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[len(self.segments) - 1]

    def create_snake(self):
        start_x = 0
        start_y = 0
        for num_square in range(3):
            square = Turtle(shape=SHAPE)
            square.color(COLOR)
            square.penup()
            square.setpos(start_x, start_y)
            start_x -= 20
            self.segments.append(square)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for n in range(len(self.segments) - 1, 0, -1):
            position_x = self.segments[n - 1].xcor()
            position_y = self.segments[n - 1].ycor()
            self.segments[n].setpos(position_x, position_y)
        self.head.forward(FORWARD_DISTANCE)

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

    def food_collision(self, food):
        if self.head.distance(food) < 25:
            return True

    def wall_collision(self):
        if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 265 or self.head.ycor() < -290:
            return True

    def tail_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 15:
                return True

    def add_segment(self):
        curr_x = self.tail.xcor()
        curr_y = self.tail.ycor()
        square = Turtle(shape=SHAPE)
        square.color(COLOR)
        square.penup()
        square.setpos(curr_x, curr_y)
        curr_x -= 20
        self.segments.append(square)

