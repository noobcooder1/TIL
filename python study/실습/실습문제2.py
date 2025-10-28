# <실기문제 #2>
# 1. 사용자에게 화면에 “입력받을 학생수:”라고 메시지를 띄우고 학생수를 입력받는다.
# 2. 입력받은 학생 수만큼 각 학생의 영문이니셜, 학년, 총점(100점 만점, 동점 입력금지, 따로 에러 체크는
# 하지 않음)을 입력받는다.
# 3. 각 학년별 총점이 제일 높은 학생의 영문이니셜과 총점을 아래의 양식에 맞춰 화면에 출력한다.
# 4. 입력한 모든 학생의 평점(평균 점수)을 소수점 아래 둘째자리까지만 표시한다.

# ※ max()함수 등 사용금지, 직접 최고값을 찾는 코드 작성할 것
# [화면출력 형식]
# 1학년 수석 : 000 총점: 00점
# 2학년 수석 : 000 총점: 00점
# 3학년 수석 : 000 총점: 00점
# 총 00명 학생들의 평점: 00.00점

students = []
grade = []
total_score = []
max_score1 = 0
max_score2 = 0
max_score3 = 0

student_count = int(input("입력받을 학생수: "))

for i in range(student_count):
    students.append(input("영문이니셜을 입력하세요: "))
    grade.append(int(input("학년을 입력하세요 (1~3): ")))
    total_score.append(int(input("총점을 입력하세요 (100점 만점, 동점 입력금지): ")))


for i in range(student_count):
    if(grade[i] == 1): 
        if(total_score[i] > total_score[max_score1]):
            max_score1 = i

    elif(grade[i] == 2): 
        if(total_score[i] > total_score[max_score2]):
            max_score2 = i

    else: 
        if(total_score[i] > total_score[max_score3]):
            max_score3 = i

print(f"1학년 수석 : {students[max_score1]} 총점: {total_score[max_score1]}점")
print(f"2학년 수석 : {students[max_score2]} 총점: {total_score[max_score2]}점")
print(f"3학년 수석 : {students[max_score3]} 총점: {total_score[max_score3]}점")