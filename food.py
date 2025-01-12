from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color(r, g, b)

        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(x=random_x, y=random_y)

