import random

def minus(count):
    print(count, "번째 문제를 시작합니다. ")
    a =  random.randint(1, 100)
    b =  random.randint(1, 100)
    print("자 두 번째 문제를 시작합니다. ", a, "-", b, "는?")
    answer = int(input("정답을 입력하세요: "))
    if (answer == a - b) :
        print("정답입니다.")
    else:
        print("틀렸습니다. 정답은", a - b, "입니다.")

def sum_(count):
    print(count, "번째 문제를 시작합니다. ")
    a =  random.randint(1, 100)
    b =  random.randint(1, 100)
    print(a, "+", b, "는?")
    answer = int(input("정답을 입력하세요: "))
    if (answer == a + b) :
        print("정답입니다.")
    else:
        print("틀렸습니다. 정답은", a + b, "입니다.")

def multiply(count):
    print(count, "번째 문제를 시작합니다. ")
    a =  random.randint(1, 100)
    b =  random.randint(1, 50)
    print(a, "*", b, "는?")
    answer = int(input("정답을 입력하세요: "))
    if (answer == a * b) :
        print("정답입니다.")
    else:
        print("틀렸습니다. 정답은", a * b, "입니다.")

def divide(count):
    print(count, "번째 문제를 시작합니다. ")
    a =  random.randint(1, 100)
    b =  random.randint(1, 50)
    print(a, "/", b, "는?")
    answer = int(input("정답을 입력하세요: "))
    if (answer == int(a / b)) :
        print("정답입니다.")
    else:
        print("틀렸습니다. 정답은", int(a / b), "입니다.")



count = 0
while True:
    print("1. 덧셈 2. 뺄셈 3. 곱셈 4. 나눗셈 5. 종료")
    menu = int(input("원하는 문제유형의 번호를 입력하세요: "))
    count += 1

    if (menu == 1):
        sum_(count)
    elif (menu == 2):
        minus(count)
    elif (menu == 3):
        multiply(count)
    elif (menu == 4):
        divide(count)
    elif (menu == 5):
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        count -= 1
