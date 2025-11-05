import random
import turtle as t
#마우스 광클하면 버그생김

def square(size):
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)

def drawit(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(random.random(), random.random(), random.random())
    t.begin_fill()
    square(random.randint(10, 100))
    t.end_fill()


s = t.Screen()
s.onscreenclick(drawit)
t.done()