from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


import time

screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True

while game_is_on:
    
    screen.update()
    time.sleep(0.15)
    snake.move()

    #The collision Detection
    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            scoreboard.reset()
            snake.reset()
    #if head collides with any segments in the tail:
        #trigger game_over


screen.exitonclick()