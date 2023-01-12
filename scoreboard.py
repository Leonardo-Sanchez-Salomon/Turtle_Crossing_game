from turtle import Turtle
import car_manager
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        self.level = 1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 50)
        self.write(arg="GAME OVER", align="center", font=FONT)
