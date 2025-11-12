# 3, 문제풀이가 끝나면 사용작성한 6장 도전문제소스를  함수 사용하는 소스로 만들기  calc.py
# <문제요구사항>
# 1~9중 2개의 숫자를  무작위로 뽑고,사칙연산자(+,-,*,/)도 무작위로 생성하여  수학식을 만들어 화면에 출력.
# 사용자가 처음 정답을 맞출 때까지 계속 그 수학식을 풀게 한다.
#
# 3, 문제풀이가 끝나면 사용자에게 계속 할 지 를  물어보고(y/n),
# 사용자가 종료를 선택하면 프로그램을 끝내고 아니면 1~2를 계속 수행한다.
# 자에게 계속 할 지 를  물어보고(y/n),
# 사용자가 종료를 선택하면 프로그램을 끝내고 아니면 1~2를 계속 수행한다.

import random
import operator as op
import math

num1 = random.randint(1, 9)
num2 = random.randint(1, 9)
num3 = random.randint(0, 3)
cal = ["+", "-", "*", "//"]

def question(num1, num2, cal):
    print(f"{num1} {cal} {num2} = ? \n정답인 정수를 입력하세요.")
    answer = int(input("정답을 입력하세요: "))
    if answer == eval(f"{num1}{cal}{num2}"):
        print("정답입니다.")
    else:
        print("오답입니다. 정답은", eval(f"{num1} {cal} {num2}"), "입니다.")




print("사칙연산 문제를 풀어보세요.")
question(num1, num2, cal[num3])

while True:
    call = input("종료하시겠습니까? 종료하시려면 y, 계속하려면 n을 입력하세요: ")
    if call == 'n':
        question(num1, num2, cal[num3])
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        num3 = random.randint(0, 3)
    elif call == 'y':
        print("문제를 종료합니다.")
        break
    else:
        print("y 또는 n을 입력하세요.")
