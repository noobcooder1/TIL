import random

word = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
password = []
password1 = ""

digitcount = int(input("설정할 비밀번호의 자릿수를 입력하세요."))

for i in range (digitcount):
    password.append(random.choice(word))
    password1 += str(password[i])

print("저장된 비밀번호는", password1, "입니다.")