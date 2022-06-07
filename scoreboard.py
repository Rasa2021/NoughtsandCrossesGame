from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.crosses_score = 0
        self.noughts_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.color("white")
        self.goto(-100, 250)
        self.write(f"Crosses {self.crosses_score}", align="center", font=("Courier", 20, "normal"))
        self.goto(100, 250)
        self.write(f"{self.noughts_score} Noughts", align="center", font=("Courier", 20, "normal"))

    def cross_point(self):
        self.crosses_score += 1
        self.update_scoreboard()

    def nought_point(self):
        self.noughts_score += 1
        self.update_scoreboard()

    def draw_point(self):
        self.crosses_score += 0
        self.noughts_score += 0
        self.update_scoreboard()

    def crosses_won(self):
        self.goto(0, 180)
        self.color("red")
        self.write("CROSSES WON!", align="center", font=("Courier", 30, "normal"))

    def noughts_won(self):
        self.goto(0, 180)
        self.color("green")
        self.write("NOUGHTS WON!", align="center", font=("Courier", 30, "normal"))

    def draw(self):
        self.goto(0, 180)
        self.color("blue")
        self.write("IT'S A DRAW!", align="center", font=("Courier", 30, "normal"))




