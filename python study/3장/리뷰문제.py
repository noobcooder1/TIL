#사용자에게 두 개의 정수를 입력받아 변수를 저장
#두 개 정수의 합, 차, 곱, 몫, 나머지를 계산하여 출력

num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))


print("두 수의 모든 연산을 시작하겠습니다. ")

print("합은", num1 + num2)
print("차는", num1 - num2)
print("곱은", num1 * num2)
print("몫은", int(num1 / num2))
print("나머지는", num1 % num2)

