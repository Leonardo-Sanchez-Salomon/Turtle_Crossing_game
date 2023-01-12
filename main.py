import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.title("Turtle Crossing")
screen.listen()
screen.onkeypress(player.go_forward, "Up")
# screen.onkeypress(player.go_backward, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car(scoreboard.level)
    car_manager.car_move(scoreboard.level)

    for car in car_manager.cars:
        y_distance = player.ycor() - car.ycor()
        x_distance = player.xcor() - car.xcor()
        if -20 < y_distance < 20 and -30 < x_distance < 30:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.reset()
        scoreboard.level_up()



screen.exitonclick()
