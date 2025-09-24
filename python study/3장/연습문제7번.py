nums = int(input("정수를 입력하세요: "))
num = nums
sum1 = 0

print("정수의 자릿수의 합을 계산하겠습니다.")

def digit_count(nums):
    return len(str(abs(nums)))


for i in range (digit_count(nums)):
    num1 = num % 10
    num = int(num / 10)   
    sum1 += num1


print("자릿수의 합은", sum1, "입니다.")