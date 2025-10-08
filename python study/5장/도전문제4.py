# [실습4] 연습문제 9번 : 2자리 숫자로 이루어진 복권, 복권번호는 사용자가 입력, 당첨번호는 무작위로 생성하여
#  사용자 번호와 비교,  다 맞으면 100만원, 2자리중 1개 맞으면 50만원,아니면 꽝
# <힌트> 사용자가 입력한 2자리 숫자의 값을 // % 연산자 이용하여 각각의 변수로 저장,
# 복권번호도 2자리 숫자의 값을 // % 연산자 이용하여 각각의 변수로 저장,
# 4개의 숫자를 비교하여 50만원 상금 받을 지 조건절로 확인

import random

answer = int(input("복권번호 2자리를 입력하세요. : "))
first = answer // 10
second = answer % 10

lotto = random.randint(10, 99)
lotto_first = lotto // 10
lotto_second = lotto % 10

if lotto_first == first and lotto_second == second:
    print(f"1등 복권 당첨! 상금 100만원! 당첨번호는 {lotto}입니다.")
elif lotto_first == first or lotto_second == second:
    print(f"2등 복권 당첨! 상금 50만원! 당첨번호는 {lotto}입니다.")
else:
    print(f"꽝 다음기회에! 당첨번호는 {lotto}입니다.")