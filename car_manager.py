from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def add_car(self):
        car_color = random.choice(COLORS)
        y_axis = random.randint(-250, 250)
        x_axis = random.randint(300, 5000)
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(1, 2)
        new_car.penup()
        new_car.color(car_color)
        new_car.goto(300, y_axis)
        new_car.setheading(180)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)



