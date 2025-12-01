mydict = {}

while True:
    choice = int(input("일정추가는 1을, 일정삭제는 2를, 일정확인은 3을, 종료하려면 4을 입력하세요: "))

    if choice == 1:
        # 일정 추가
        date = input("날짜를 입력하세요: ")
        if date not in mydict:
            job = input("일정을 입력하시오: ")
            mydict[date] = [job]  # 문자열 대신 리스트로 저장
        else:
            plus = int(input("이미 일정이 있습니다. 더 추가하시려면 1을 아니면 2를 입력하세요: "))
            if plus == 1:
                job = input("일정을 입력하시오: ")
                mydict[date].append(job)  # 리스트에 추가
            else:
                print("일정등록을 취소합니다.")

    elif choice == 2:
        # 일정 삭제
        date = input("날짜를 입력하세요: ")
        if date not in mydict:
            print("등록된 일정이 없습니다!")
        else:
            print("현재 일정:", mydict[date])
            delete_choice = int(input("전체 삭제는 1을, 특정 일정만 삭제하려면 2를 입력하세요: "))
            if delete_choice == 1:
                del mydict[date]
                print("해당 날짜의 모든 일정을 삭제했습니다.")
            elif delete_choice == 2:
                job_to_delete = input("삭제할 일정을 입력하세요: ")
                if job_to_delete in mydict[date]:
                    mydict[date].remove(job_to_delete)
                    print("일정을 삭제했습니다.")
                    if len(mydict[date]) == 0:
                        del mydict[date]
                else:
                    print("해당 일정이 없습니다.")

    elif choice == 3:
        # 일정 확인
        if len(mydict) == 0:
            print("등록된 일정이 없습니다!")
        else:
            print("\n=== 전체 일정 ===")
            for date in mydict:
                print(date + ":", mydict[date])
            print()

    elif choice == 4:
        # 종료
        print("일정관리 프로그램을 종료합니다.")
        break

    else:
        print("잘못된 입력입니다. 다시 입력하세요.")