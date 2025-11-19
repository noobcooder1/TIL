dict = {}
dict["사랑"] = "love"

def delete_word(num, dict):
    if num == 1:
        key = input("삭제할 단어를 입력하세요: ")
        if key in dict.keys():
            del dict[key]
            print("단어가 삭제되었습니다.")
        else:
            print("단어가 사전에 없습니다.")
    else :
        dict.clear()


def find_word(flag, dict):
    if flag == 1:
        print("찾을 단어를 입력하세요: ")
        key = input()
        if key in dict.keys():
            print(dict[key])
        else:
            print("단어가 사전에 없습니다.")
    else:
        for key in sorted(dict.keys()):
            print(f"{key}의 뜻은 {dict[key]}입니다.")

if __name__ == "__main__":
    while True:
        print("1: 단어 추가 2: 단어 삭제 3: 단어 검색 4: 사전 초기화 5: 종료")
        flag = int(input("원하는 작업을 선택하세요: "))
        if flag == 5:
            print("프로그램을 종료합니다.")
            break
        if flag == 1:
            word = input("단어를 입력하세요: ")
            value = input("뜻을 입력하세요: ")
            dict[word] = value
            print("단어가 추가되었습니다.")
        elif flag == 2:
            print("1: 단어 하나 2: 전체 단어")
            num = int(input("원하는 작업을 선택하세요: "))
            delete_word(num, dict)
        elif flag == 3:
            print("1: 단어 하나 2: 전체 단어")
            num = int(input("원하는 작업을 선택하세요: "))
            find_word(num, dict)
        elif flag == 4:
            dict.clear()
            print("사전이 초기화되었습니다.")
        else:
            print("잘못된 선택입니다. 다시 선택하세요.")
