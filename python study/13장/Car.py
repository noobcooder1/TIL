from turtle import *

class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
        self.turtle = Turtle()
        self.turtle.shape("beast.gif")  # jpg는 안됨, gif만 가능

    def drive(self):
        self.turtle.forward(self.speed)

    def left_turn(self):
        self.turtle.left(90)

register_shape("beast.gif")
myCar = Car(200, "red", "E-class")
for i in range(100):
    myCar.drive()
    myCar.left_turn()
