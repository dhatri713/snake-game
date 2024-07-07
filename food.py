from turtle import Turtle
import random

SHAPE = "circle"
COLOR = "blue"
SIZE = 0.75


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(SIZE)

    def create(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 268)
        self.penup()
        self.goto(random_x, random_y)

    def regenerate(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.penup()
        self.goto(random_x, random_y)
