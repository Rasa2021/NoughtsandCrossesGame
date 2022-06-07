from turtle import Turtle


class Frame(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.width(4)
        self.draw_frame()

    def draw_frame(self):
        self.hideturtle()
        self.penup()
        self.right(90)
        self.goto(-50, 150)
        for _ in range(1, 5):
            self.pendown()
            self.forward(300)
            self.right(90)
            self.penup()
            for _ in range(1, 3):
                self.forward(100)
                self.right(90)