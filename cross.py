from turtle import Turtle


class Cross(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.pensize(3)
        self.hideturtle()

    def draw_cross(self, x, y):
        self.penup()
        self.goto(x, y)
        self.pendown()
        self.right(45)
        self.forward(50)
        self.backward(100)
        self.forward(50)
        self.left(90)
        self.forward(50)
        self.backward(100)
        self.forward(50)
        self.right(45)



