import turtle as t
t.shape("turtle")

t.penup()
t.goto(100, 100)
t.write("거북이가 양수로 이동했어요")
t.goto(100, 0)
t.write("거북이가 여기로 이동시에는 0이에요")
t.goto(100, -100)
t.write("거북이가 음수로 이동했어요")

t.goto(0, 0)
t.pendown()
n = int(t.textinput("title", "숫자를 입력하세요."))

if (n > 0):
    t.goto(100, 100)
elif (n == 0):
    t.goto(100, 0)
else: 
    t.goto(100, -100)

t.done()