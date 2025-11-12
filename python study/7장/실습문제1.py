#실습 1 요구사항 : 2이상 정수 입력받고 변수에 저장(오류체크 안 함) 연산자는 더하기나 곱하기중 입력받음
# 연산자가 곱하기면 1부터 정수까지의 곱을 합이면 정수부터 1까지의 합을 계산한다  그리고 결과값을 화면에 출력한다.
# 2번째 요구사항 함수사용하는 프로그램으로 변경하기, 함수사용하기 전과 후를 비교한다.

num = int(input("2이상의 정수를 입력하세요."))
op = input("+ 또는 * 중 하나의 연산자를 입력하세요.")

def result() :
    if op == '*':
       sum1 = 1
       for i in range(num, 1, -1):
           sum1 = sum1 * i
       print("결과는 ", sum1)

    elif op == "+":
       sum2 = 1
       for i in range(num, 1, -1):
           sum2 = sum2 + i
       print("결과는 ", sum2)

    else :
        print("+ 아니면 *만 입력하세요.")


result()


# 함수 없는 버전!
# if op == '*':
#     sum1 = 1
#     for i in range(num, 1, -1):
#         sum1 = sum1 * i
#     print("결과는 ", sum1)
#
# else :
#     sum2 = 1
#     for i in range(num, 1, -1):
#         sum2 = sum2 + i
#     print("결과는 ", sum2)
#