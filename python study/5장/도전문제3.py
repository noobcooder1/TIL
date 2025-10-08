# [실습3] 연습문제 4번 : if – elif- else 구문 사용

score = int(input("점수를 입력하세요: "))

if score >= 90:
    print("A학점 입니다.")
elif score >= 80:
    print("B학점 입니다.")
elif score >= 70:
    print("C학점 입니다.")
elif score >= 60:
    print("D학점 입니다.")
else:
    print("F학점 입니다.")