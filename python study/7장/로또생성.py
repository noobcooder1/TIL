import random

boks = []
some_checks = int(input("복권 몇 장 사실래요?"))


def bokgwon():
    for i in range(some_checks):
        nums = []
        for j in range(6):
            nums.append(random.randint(0, 45))
        boks.append(nums)
    print(boks)

bokgwon()