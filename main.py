import time
from turtle import Screen
from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(turtle.move_up, "Up")

game_is_on = True
iterations = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if iterations % 6 == 0:
        car_manager.add_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if turtle.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if turtle.ycor() > 300:
        scoreboard.next_level()
        scoreboard.create_scoreboard()
        turtle.start()

    iterations += 1

screen.exitonclick()
