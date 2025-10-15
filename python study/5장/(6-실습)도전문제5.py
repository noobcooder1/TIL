# [실습5] 2개의 2자리 정수를 무작위로 생성하여 덧셈,뺄셈, 곱셈,나눗셈 문제를 내고 사용자의 입력값과 
# 계산값을 비교하여 “정답“, “오답“ 출력하기 (if-else사용)

import random
import operator as op
import math

def question(num1, num2, cal):
    print(f"{num1} {cal} {num2} = 정답인 정수를 입력하세요.")
    answer = int(input("정답을 입력하세요: "))
    if answer == eval(f"{num1}{cal}{num2}"):
        print("정답입니다.")
    else:
        print("오답입니다. 정답은", eval(f"{num1} {cal} {num2}"), "입니다.")


num1 = random.randint(10, 99)
num2 = random.randint(10, 99)
num3 = random.randint(0, 3)
cal = ["+", "-", "*", "//"]

print("사칙연산 문제를 풀어보세요.")

while True:
    call = input("문제를 푸시겠습니까? 푸실려면 y, 종료하려면 n을 입력하세요: ")
    if call == 'y':
        question(num1, num2, cal[num3])
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        num3 = random.randint(0, 3)
    elif call == 'n':
        print("문제를 종료합니다.")
        break
    else:
        print("y 또는 n을 입력하세요.")
