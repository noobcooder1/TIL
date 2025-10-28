# <실기문제 #3>
# 1. 도형의 종류 : 원, 삼각형, 사각형, 오각형중 임의로 하나의 도형 선택
# 2. 도형의 한 변의 길이나 원의 반지름은 10~100사이의 값중 임의 크기로 선택
# 3. 도형을 채울 색깔은 다음중 하나를 무작위로 고른다. “red”, “yellow”, ‘green“, ”blue“, ”purple“
# 4. 도형을 그리기 시작하는 x,y좌표는 –200 ~ +200 중에서 무작위로 선택한다.
# 5. 1~4에서 선택한 조건으로 도형을 그린다.
# 6. 위의 1~5번 과정을 10번 반복한다.

import turtle as t
import random

def make_start_x():
    start_x = random.randint(-200, 200)
    return start_x

def make_start_y():
    start_y = random.randint(-200, 200)
    return start_y

def make_size():
    size = random.randint(10, 100)
    return size


colors = ["red", "yellow", "green", "blue", "purple"]

shape = input("도형을 선택하세요 (원, 삼각형, 사각형, 오각형): ")

if(shape == "원"):
    color = random.choice(colors)
    t.pensize(3)
    t.penup()
    t.goto(make_start_x(), make_start_y())
    t.pendown()
    t.circle(make_size())
    t.fillcolor(color)
    t.begin_fill()
    t.end_fill()
    



