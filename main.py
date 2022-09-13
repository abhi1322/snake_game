from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
screen.listen()

is_game_on = True
snake = Snake()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
collision = snake.self_collision()

food = Food()
snake.create_snake()
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head(food) < 15:
        food.refresh()
        snake.size_increase()

    if snake.is_snake_outside():
        is_game_on = False

    # for segment in snake.snake:
    #     if segment == snake.snake[0]:
    #         pass
    #     elif snake.snake[0].distance(segment) < 10:
    #         is_game_on = False
    #         snake.game_over()
    for segment in snake.snake[1:]:
        if snake.snake[0].distance(segment) < 10:
            is_game_on = False
            snake.game_over()

screen.exitonclick()
