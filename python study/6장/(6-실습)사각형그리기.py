import turtle as t

Colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta", "lime", "teal", "lavender"]
size = int(input("사각형의 한 변의 길이를 입력하세요: "))
gak = int(input("사각형을 회전시킬 각도를 입력하세요: "))

def drawSquare(size): 
    t.forward(size)
    t.left(90)   # 또는 t.right(90)
    t.forward(size)
    t.left(90)   # 또는 t.right(90)
    t.forward(size)
    t.left(90)   # 또는 t.right(90)
    t.forward(size)
    t.left(90)   # 또는 t.right(90)
    t.left(gak)

t.shape("turtle")
t.pensize(2)

t.penup()
t.goto(0, 0)
t.pendown()

for i in range(360): 
    t.pencolor(Colors[i % len(Colors)])
    drawSquare(size)
    size += 5

t.done()
    

