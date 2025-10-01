#사용자에게 숫자를 입력받아서 입력받은 각형을 선으로 그린후에 점점 확장시켜서 촘촘한 도형만들기.

import turtle as t
import math
t.shape("turtle")

n = int(t.textinput("title", "몇 각형을 그리고 싶으신가요. 삼각형어면 3, 사격형이면 4같이 정수로 입력하세요."))

color = ["red", "yellow", "orange", "green", "skyblue", "blue", "gray", "black"]
default_length = 50
pensize = 10
t.pensize(pensize)
r = 50

for j in range (n) :
    t.pencolor(color[j % len(color)])
    t.penup()
    t.goto(-r/2, -r)
    t.setheading(0)
    t.pendown()
    for i in range(n) : 
        t.forward(2 * r * math.sin(math.pi / n))
        t.left(360/n)   
    t.penup()
    t.goto(0, 0)
    t.pendown()
    r+=pensize

t.done()

# import turtle as t
# t.shape("turtle")

# n = int(t.textinput("title", "몇 각형을 그리고 싶으신가요. 삼각형어면 3, 사격형이면 4같이 정수로 입력하세요."))

# t.pensize(10)
# t.fillcolor("blue")
# t.begin_fill()
# for i in range(n) : 
#     t.pencolor("purple")
#     t.forward(100)
#     t.left(360/n)   
    

# t.end_fill()
# t.done()