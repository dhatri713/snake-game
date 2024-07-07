from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.listen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

game_is_on = True

snake = Snake()
food = Food()
food.create()
score = Score()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.food_collision(food):
        food.regenerate()
        snake.add_segment()
        score.update_scoreboard()

    if snake.wall_collision():
        score.reset()
        snake.reset()
        food.regenerate()

    if snake.tail_collision():
        score.reset()
        snake.reset()
        food.regenerate()

screen.exitonclick()
