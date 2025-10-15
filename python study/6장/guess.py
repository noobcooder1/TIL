import random as ran

correct = ran.randint(1, 100)

print("1부터 100사이의 숫자를 맞춰보세요.")
answer = 0
count = 0

while answer != correct:
    answer = int(input("정답일 것 같은 숫자를 입력하세요: "))
    count += 1

    if answer > correct:
        print(f"제시하신 {answer}은 정답보다 커요. 더 작은 수를 입력해보세요. 현재 시도 횟수는 {count}회 입니다.")
    elif answer < correct:
        print(f"제시하신 {answer}은 정답보다 작아요. 더 큰 수를 입력해보세요. 현재 시도 횟수는 {count}회 입니다.")
    else:
        print(f"정답입니다! 정답은 {correct}였습니다.  현재 시도 횟수는 {count}회 입니다.")
        break
    if count == 10:
        print(f"시도 횟수 10회를 초과하여 게임이 종료됩니다. 정답은 {correct}였습니다.")
        break