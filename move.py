from turtle import Turtle
line = Turtle()


class Move:
    def __init__(self):
        self.up()
        self.down()

    def up(self):
        new_y = line.ycor() + 20
        line.goto(x=line.xcor(), y=new_y)

    def down(self):
        new_y = line.ycor() - 20
        line.goto(x=line.xcor(), y=new_y)

