# <실기문제 #1>
# 1. “shingu”, “it”, “software”, 3개 항목을 가지는 list변
# 수 std_id를 만든다.
# 2. 사용자가 입력한 id가 std_id에 있다면 “환영합니다”
# 를 출력하고 임의로 숫자로 이루어진 3자리 문자열
# 암호를 생성하여 화면에 출력해준다.
# 3. std_id리스트에 없는 id를 입력했다면 “없는 id입니
# 다”를 출력한다.

import random

std_id = ["shingu", "it", "software"]

user_id = input("아이디를 입력하세요: ")

if user_id in std_id:
    print("환영합니다")
    password1 = str(random.randint(0, 9))
    password2 = str(random.randint(0, 9))
    password3 = str(random.randint(0, 9))
    password = password1 + password2 + password3
    print(f"{user_id}에 자동생성된 비밀번호는 {password}입니다.")
else:
    print("없는 아이디입니다.")