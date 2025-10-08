# [실습2] P.143 주사위던지기 게임 완성하기
import random 

print("주사위 게임에 오신 것을 환영합니다.")

sum = 0

roll = int(input("주사위를 굴릴 횟수를 입력하세요 :"))

for i in range(roll):
    dice = random.randint(1,6)
    print(f"{i+1}번째 주사위의 값은 {dice}입니다.")
    sum += dice

print(f"총 주사위의 합은 {sum}입니다.")
print("게임이 종료되었습니다. 이용해주셔서 감사합니다.")