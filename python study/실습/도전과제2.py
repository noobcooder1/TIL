# 2. Random함수를 이용하여 1~100숫자중에서 10개를  중복된 값없이 무작위로 추출하여 리스트변수에 저장한다.
# 이 리스트값을 인수로 넘겨 그중에서 최고값을 return하는 함수를 정의한다.
# 10개의 숫자와 해당함수의 호출값인 최고값을  화면에 출력한다.

# 자동제안 활성화는 옵션 + 시프트 + 역슬래시

import random

nums = []
for i in range(10):
    nums.append(random.randint(1, 100))

print(nums)

def returnmax(arr) :
    count = 0
    for j in range (len(arr)):              #파이썬에서 배열길이구하는 함수는 len(배열명)이다. 물론 배열뿐이 아니라 문자열 길이도 구하기가능!
        if arr[j] > arr[count] :
            count = j
        print(j, "인덱스의 숫자는", arr[j])
    print("이 숫자들중 최고값은", arr[count])


returnmax(nums)