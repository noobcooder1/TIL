mydict = {}

while True:
    date = input("날짜를 입력하세요, 종료하시려면 q를 입력하세요.")
    if date == "q" :
        break
    if date not in mydict:
        job = input("일정을 입력하시오: ")
        mydict[date] = [job]  # 문자열 대신 리스트로 저장
    else:
        plus = int(input("이미 일정이 있습니다. 더 추가하시려면 1을 아니면 아무키나 입력하세요."))
        if plus == 1:
            job = input("일정을 입력하시오: ")
            mydict[date].append(job)  # 리스트에 추가
        else :
            print("일정을 취소합니다.")
    print(mydict)
