# <실습문제 #2>
# 주석문달기
# 요구사항: 3명 학생의 이름, 국,영,수 점수를 입력받아 list변수에 저장하기(중첩리스트와 반복구조 사용)
# 화면에 아래와 같이 서식을 갖춰서 출력하기(평균값은 소수점1자리까지 표시)

# 성명           국어    영어    수학   총점     평균
# Kim             95        90       95    총점1    평균1
# Min              100     50       40    총점2    평균2
# Park             75       88       63   총점3    평균3
# ===================================
# 총점/평균     O/o.o  O/o.o    O/o.o

# 4. 소스는 간결하게, 읽기 쉽게 작성할 것

students = []
kors = []
engs = []
maths = []
totals = []
averages = []

for i in range(3):
    students.append(input ("학생 이름을 입력하세요: "))
    kors.append(input ("국어 점수를 입력하세요: "))
    engs.append(input ("영어 점수를 입력하세요: "))
    maths.append(input ("수학 점수를 입력하세요: "))
    totals.append(int(kors[i]) + int(engs[i]) + int(maths[i]))
    averages.append(totals[i] / 3)

print("성명\t국어\t영어\t수학\t총점\t평균")
for i in range(3):
    print(f"{students[i]}\t{kors[i]}\t{engs[i]}\t{maths[i]}\t{totals[i]}\t{averages[i]:.1f}")