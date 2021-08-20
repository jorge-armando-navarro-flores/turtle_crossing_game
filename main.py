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

screen.onkey(turtle.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    if turtle.is_at_finish_line():
        scoreboard.next_level()
        scoreboard.update_scoreboard()
        turtle.go_to_start()
        car_manager.increase_car_speed()


screen.exitonclick()
