# 1. 11번: import time
#       total_sec =time.time()  #  total_sec에 1970년 1월 1일이후 흘러온 전체 초값이 저장됨
#       sec = int(total_sec)  # total_sec이 실수라서 정수로 변환해줌
             
#       출력값  현재시간(GMT) : 00시 00분 

# 2. 초를 입력받아 시간,분,초로 변환하여 출력하기( //, %)
# 3. 교재 P. 81, 자판기 도전문제 완성하기


import time

total_sec = time.time()
sec = int(total_sec)
print(sec / 60, "분")
print(int(sec / 60 / 60), "시간")
print(int(sec / 60 / 60 / 24), "일")
print("현재 시각은", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "입니다.")
