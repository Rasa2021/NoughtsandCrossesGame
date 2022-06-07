from turtle import Turtle


class Nought(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        # self.nought = "o"
        self.pensize(3)
        self.hideturtle()

    def draw_nought(self, x, y, radius=40):
        self.penup()
        self.goto(x, y - radius)
        self.pendown()
        self.circle(radius)




