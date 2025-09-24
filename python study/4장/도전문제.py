list = []
a = input("추가할 사람을 입력하세요.")
list.append(a)          #append는 리스트에 요소를 추가하는 함수이다.   
b = int(input("그 사람의 나이를 입력하세요"))
list.append(b)
c = input("그 사람의 주소를 입력하세요.")
list.append(c)
print(f"{a}의 나이는 {b}이고, 주소는 {c}입니다.")