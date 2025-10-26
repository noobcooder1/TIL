# 실습문제 1번
# 자동차 그리기
# 1. 가로 400, 세로 200 크기의 빨간색 자동차 몸통 그리기

import turtle as t

color1 = input("자동차 몸통의 색상을 영어로 입력하세요.")
color2 = input("자동차 지붕의 색상을 영어로 입력하세요.")
color3 = input("자동차 바퀴의 색상을 영어로 입력하세요.")

size1 = int(input("자동차 몸통 가로를 숫자로 입력하세요"))
size2 = int(input("자동차 몸통 세로를 숫자로 입력하세요"))
size3 = int(input("자동차 지붕 가로를 숫자로 입력하세요"))
size4 = int(input("자동차 지붕 세로를 숫자로 입력하세요"))
size5 = int(input("자동차 바퀴 반지름을 숫자로 입력하세요"))

t.penup()
t.goto(-size1/2, -size2/2)
t.pendown()

t.shape("turtle")
t.color("black")
t.width(1)

t.fillcolor(color1)
t.begin_fill()

t.forward(size1)
t.left(90)
t.forward(size2)
t.left(90)
t.forward(size1)
t.left(90)
t.forward(size2)
t.left(90)

t.end_fill()

# 2. 가로 200, 세로 100 크기의 노란색 자동차 뚜껑 그리기
t.up()
t.goto(-size3/2, size2/2)
t.down()

t.fillcolor(color2)
t.begin_fill()

t.fd(size3)
t.left(90)
t.fd(size4)
t.left(90)
t.fd(size3)
t.left(90)
t.fd(size4)
t.left(90)

t.end_fill()

# 3. 반지름 50의 검은색 타이어 두개 그리기
t.up()
t.goto(-size1/4, -size2/2 - size5)
t.down()

t.fillcolor(color3)
t.begin_fill()
t.circle(size5)
t.end_fill()

t.up()
t.goto(size1/4, -size2/2 - size5)
t.down()

t.fillcolor(color3)
t.begin_fill()
t.circle(size5)
t.end_fill()
t.done()