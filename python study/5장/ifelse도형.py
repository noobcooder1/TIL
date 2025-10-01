import turtle as t

n = int(t.textinput("도형 선택", "3~6 사이의 정수를 입력하세요 (3:삼각형, 4:사각형, 5:오각형, 6:육각형)"))
t.shape("turtle")
t.pensize(3)

if n == 3:
		t.forward(100)
		t.left(360/n)
		t.forward(100)
		t.left(360/n)
		t.forward(100)
		t.left(360/n)
		
elif n == 4:
		t.forward(100)
		t.left(360/n)
		t.forward(100)
		t.left(360/n)
		t.forward(100)
		t.left(360/n)
		t.forward(100)
		t.left(360/n)
		
elif n == 5:
		t.forward(100)
		t.left(360/n)
		t.forward(100)
		t.left(360/n)
		t.forward(100)
		t.left(360/n)
		t.forward(100)
		t.left(360/n)
		t.forward(100)
		t.left(360/n)
		
elif n == 6:
		t.forward(100)
		t.left(360/n)
		t.forward(100)
		t.left(360/n)
		t.forward(100)
		t.left(360/n)
		t.forward(100)
		t.left(360/n)
		t.forward(100)
		t.left(360/n)
		t.forward(100)
		t.left(360/n)
		
else:
	t.write("3~6 사이의 정수만 입력하세요!")

t.done()
