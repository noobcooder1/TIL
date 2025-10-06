# [실습 1] 
# 그림판에서 사용자로부터 도형종류(0~8입력, 3~8각형,원:0, 1.2,7를 입력하면 오류메시지출력), 크기,  어떤 색깔로 
# 그릴 지(1,red 2:yellow 3:blue, 4: green, 5: black) 물어보고 요구사항에 맞게 화면의 중앙에 그리기 
# (if문, for, list사용하기)

import turtle as t

colors = ["red", "yellow", "blue", "green", "black"]

t.shape("turtle")
n = int(t.textinput("title", "그리고 싶으신 각형은? (3~8사이의 정수 입력): "))

if (n < 3 or n > 8):
    t.textinput("오류", "3~8 사이의 정수를 입력해야 합니다.")
    t.bye()
    quit()


for i in range(n):
    t.forward(100)
    t.left(360/n)


t.done()

