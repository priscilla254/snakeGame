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
        snake.extend()

    # detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.reset()
        snake.reset_snake()
#     Detect collision with tail
    for segment in snake.segments[1:]:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment) <10:
            score.reset()
            snake.reset_snake()






















screen.exitonclick()
