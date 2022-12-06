from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.penup()
        self.x = 10
        self.y = 10
        self.moves = 5

    def refresh(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def refresh_new(self):
        self.goto(-self.xcor() - self.x, -self.ycor() - self.y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1

    def game_over(self):
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 8, "normal"))

    def increase(self):
        self.x += 1
        self.y + 1

