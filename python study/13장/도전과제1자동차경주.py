import random
from turtle import *

#필요한 클래스를 만듦
class CarRace:
    def __init__(self, speed, color, fname, locate_x, locate_y):
        self.speed = speed
        self.color = color
        self.locate_x = locate_x
        self.locate_y = locate_y
        self.turtle = Turtle()
        self.turtle.shape(fname)
        self.turtle.speed(self.speed)
        self.turtle.penup()
        self.turtle.goto(self.locate_x, self.locate_y)

    def drive(self):
        self.turtle.forward(random.randint(10, 40))  # ✅ 숫자를 작게!

#차의 디자인과 리스트를 만들어서 만들은 5대의 자동차를 담는다.
register_shape("car2.gif")
car_list = []
for i in range(5):
    car_list.append(CarRace(5, "red", "car2.gif", -300, 300 - (100 * i)))


# 모든 자동차가 동시에 여러 번 움직임
for _ in range(100):
    for car in car_list:
        car.drive()

done()