# 연습문제 4번
# 터틀 그래픽에서 거북이를 이동시킬때에는 forward() left() right() 함수를 사용한다
import turtle as t
t.shape("turtle")

# 시작위치 변경
t.up()
t.goto(-150, 0)
t.down()

# 지그재그 선긋기
t.fd(100)
t.left(90)
t.fd(100)
t.right(90)
t.fd(100)
t.right(90)
t.fd(100)
t.left(90)
t.fd(100)

t.clear()

# 연습문제 5번
# 터틀 그래픽에서 width() 함수를 호출하면 거북이가 그리는 선의 두께를 두껍게 할수있다.

# 시작위치 변경
t.up()
t.goto(-50, 0)
t.down()

# 선 굵기 10으로 변경
t.width(10)

# 모양 그리기
t.fd(100)
t.left(90)
t.fd(100)

t.clear()

# 연습문제 6번
# 터틀 그래픽에서 color() 함수를 호출하면 거북이가 그리는 선의 색상을 변경할 수 있다.
import turtle as t
t.shape("turtle")
t.width(1)

# 시작위치 변경
t.up()
t.goto(-50, 0)
t.down()

# 선 색상을 blue로 변경
t.color("blue")

# 모양 그리기
t.right(90)
t.fd(100)

t.clear()

# 연습문제 7번
# shape() 함수를 사용하여 거북이 모양을 사각형, 삼각형, 원으로 변경할 수 있다
import turtle as t
t.shape("square")

# 시작위치 변경
t.up()
t.goto(-50, 0)
t.down()

# 모양 그리기
t.fd(100)

t.clear()

# 연습문제 8번
# 거북이가 이동할 때 선이 그려지지 않게 하려면 t.up으로 팬을 들고 t.down()으로 팬을 내려놓을 수 있다.
import turtle as t
t.shape("turtle")
t.color("black")


# 시작위치 변경
t.up()
t.goto(-50, -100)
t.down()

# 모양 그리기
t.fd(100)

# 팬 위치 이동
t.up()
t.goto(-50, 100)
t.down()

t.fd(100)

t.clear()

# 연습문제 9번
# circle()로 원을 그릴 수 있다 배운 내용을 토대로 오륜기를 그려보자 색상 : 파노검초빨
t.shape("turtle")
t.speed(5)

# 팬 위치 변경
t.up()
t.goto(-110, 25)
t.down()

t.width(5)
t.color("blue")
t.circle(50)

# 팬 위치 변경
t.up()
t.goto(-55, -25)
t.down()

t.color("yellow")
t.circle(50)

# 팬 위치 변경
t.up()
t.goto(0, 25)
t.down()

t.color("black")
t.circle(50)

# 팬 위치 변경
t.up()
t.goto(55, -25)
t.down()

t.color("green")
t.circle(50)

# 팬 위치 변경
t.up()
t.goto(110, 25)
t.down()

t.color("red")
t.circle(50)

t.clear()

# 실습문제 1번
# 자동차 그리기
# 1. 가로 400, 세로 200 크기의 빨간색 자동차 몸통 그리기
t.penup()
t.goto(-200, -100)
t.pendown()

t.shape("turtle")
t.color("black")
t.width(1)

t.fillcolor("red")
t.begin_fill()

t.forward(400)
t.left(90)
t.forward(200)
t.left(90)
t.forward(400)
t.left(90)
t.forward(200)
t.left(90)

t.end_fill()

# 2. 가로 200, 세로 100 크기의 노란색 자동차 뚜껑 그리기
t.up()
t.goto(-100, 100)
t.down()

t.fillcolor("yellow")
t.begin_fill()

t.fd(200)
t.left(90)
t.fd(100)
t.left(90)
t.fd(200)
t.left(90)
t.fd(100)
t.left(90)

t.end_fill()

# 3. 반지름 50의 검은색 타이어 두개 그리기
t.up()
t.goto(-100, -150)
t.down()

t.fillcolor("black")
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(100, -150)
t.down()

t.fillcolor("black")
t.begin_fill()
t.circle(50)
t.clear()
t.end_fill()

#실습문제 2번
#집 그림 2
# 1. 가로 200, 세로 200 크기의 빨간색 집 몸통 그리기
t.penup()
t.goto(-100, -100)
t.pendown()

t.fillcolor("yellow")
t.begin_fill()

t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)

t.end_fill()

# 2. 초록새 세모 지붕 만들기
t.penup()
t.goto(-100, 100)
t.pendown()

t.fillcolor("green")
t.begin_fill()

t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.end_fill()


# 반지름 30 바퀴 두개 그리기
t.penup()
t.goto(-50, -150)
t.pendown()

t.fillcolor("brown")
t.begin_fill()
t.circle(25)
t.end_fill()

t.penup()
t.goto(50, -150)
t.pendown()

t.begin_fill()
t.circle(25)
t.end_fill()

t.done()