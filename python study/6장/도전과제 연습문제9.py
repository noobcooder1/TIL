password = input("Enter the password please: ")

while True:
    answer = input("패스워드를 맞춰보세요. : ")
    if answer == password:
        print("패스워드가 일치합니다. 잠금을 해제합니다.")
        break
    else:
        print("패스워드가 일치하지 않습니다. 다시 시도하세요.")