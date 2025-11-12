# 3. 다각형을 그리는 함수를 정의하기. 한변의 길이,중심 좌표, 색깔, 다각형 그리는 횟수를 랜덤으로 생성해서  다양한 크기, 색깔의 다각형그리기

import random
import turtle as t

colors = ["red", "yellow", "green", "orange", "blue", "skyblue", "purple", "gray"]

def drawObject() :
    size = random.randint(50, 200)
    position_x = random.randint(-200, 200)
    position_y = random.randint(-200, 200)
    count = random.randint(3, 13)
    color = random.choice(colors)
    t.pensize(5)
    t.fillcolor(color)
    t.penup()
    t.goto(position_y, position_y)
    t.pendown()
    t.begin_fill()

    for i in range(count) :
        t.forward(size)
        t.left(360/count)
    t.end_fill()
    t.done()

drawObject()