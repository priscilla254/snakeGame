from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen=Screen()
snake=Snake()
food=Food()
score=Score()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game, 'snakedooodloo'")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
#     detect collision with food
    if snake.head.distance(food)<30:
        score.increase_score()
        food.refresh()



























screen.exitonclick()
