
def fac(num):
    total = 1
    for i in range(num):
        total = total * (num - i)

    print(total)

while True:
    num = int(input("팩토리얼 값을 구할 1이상의 정수를 입력하세요."))
    fac(num)
    con = int(input("계속하시려면 1을 종료하시려면 아무키나 누르세요."))
    if con != 1:
        break



