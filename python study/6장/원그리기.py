import turtle as t

Colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta", "lime", "teal", "lavender"]
size = int(input("그릴 원의 지름을 입력하세요: "))
gak = int(input("원을 회전시킬 각도를 입력하세요: "))

def drawSquare(size): 
    t.circle(size)
    t.speed(0)
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
    

