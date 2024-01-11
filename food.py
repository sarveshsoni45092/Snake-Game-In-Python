from turtle import Turtle
import random
COLOR = ["red","orange","yellow","green","blue","purple"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        self.color(random.choice(COLOR))
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)

        self.goto(random_x,random_y)

     