from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.cars = []

    def create_car(self, level):
        while level > 0:
            rand_chance = random.randint(0, 6)
            if rand_chance == 1:
                car = Turtle("square")
                car.shapesize(stretch_wid=1, stretch_len=2)
                car.penup()
                car.color(random.choice(COLORS))
                rand_y = random.randint(-250, 250)
                car.goto(350, rand_y)
                self.cars.append(car)
            level -= 1

    def car_move(self, level):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT*(level - 1))

