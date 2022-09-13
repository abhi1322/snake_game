from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake = []
        self.x = 0
        self.text = Turtle()
        self.game_over_text = Turtle()
        self.score = 0

    def create_snake(self):
        for index in range(3):
            new_snake_block = Turtle(shape="square")
            new_snake_block.penup()
            new_snake_block.color("white")
            new_snake_block.goto(STARTING_POSITIONS[index])
            self.snake.append(new_snake_block)
        self.score_text(self.score)

    def move(self):
        for snake_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_num - 1].xcor()
            new_y = self.snake[snake_num - 1].ycor()
            self.snake[snake_num].goto(new_x, new_y)
        self.snake[0].forward(20)

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def head(self, compare):
        value = self.snake[0].distance(compare)
        return value

    def size_increase(self):
        new_snake_block = Turtle(shape="square")
        new_snake_block.penup()
        new_snake_block.color("white")
        new_snake_block.goto(x=self.x, y=0)
        self.snake.append(new_snake_block)
        self.x += 20
        self.text.clear()
        self.score += 10
        self.score_text(self.score)

    def game_over(self):
        self.game_over_text.penup()
        self.game_over_text.color("white")
        self.game_over_text.write("Game Over", True, align="center", font=("Arial", 24, "bold"))

    def is_snake_outside(self):
        x_position = self.snake[0].xcor()
        y_position = self.snake[0].ycor()
        if x_position > 290 or y_position > 290 or x_position < -290 or y_position < -290:
            self.game_over()
            return True
        else:
            return False

    def score_text(self, ponits):
        self.text.color("white")
        self.text.penup()
        self.text.hideturtle()
        self.text.speed(0)
        self.text.goto(0, 230)
        string = str(f"Score : {ponits}")
        self.text.write(arg=string, move=True, align="center", font=("Arial", 24, "bold"))

    def self_collision(self):
        for segment in self.snake:
            if segment == self.snake[0]:
                pass
            elif self.snake[0].distance(segment) < 10:
                self.game_over()
                return True
            return False
