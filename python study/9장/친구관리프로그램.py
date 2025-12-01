#리스트를 사용하여 친구의 이름 전화번호 주소 를 관리하는 프로그램 작성
#메뉴: 신규친구입력(동명이인가능), 이름검색가능, 조소검색, 이름찾아내용수정 및 삭제(같은 이름이 여러개면 사용자가 그중에 골라서 삭제)
import sys

friend = {}

def add_friend() :
    name = input("이름입력 : ")
    phone = input("전화번호입력 : ")
    address = input("주소입력 : ")

while True :
    youwant = int(input("원하는 기능을 고르세요. 1.친구등록  2. 이름으로 검색  3. 주소로 검색  4. 이름검색후 내용수정  5. 이름으로 삭제  6. 전체출력  7. 종료"))
    if youwant == 1 :
        add_freind()
    elif youwant == 2:
        item_search()
    elif youwant == 3:
        remove_item()
    elif youwant == 4:
        print_item()
    elif youwant == 5:
        market_exit()
    else :
        item_search()


def insert_item() :
    item_key = input("신규물품명 : ")
    item_dict[item_key] = int(input("재고량 : "))
    print("등록완료")

def item_search() :
    item_key = input("재고를 조절할 물품을 입력하세요.")
    if item_key in item_dict :
        print("물품을 찾았습니다. 재고조절 시스템을 시작합니다.")
        print("현재", item_key, "의 재고는 ", item_dict[item_key], " 있습니다.")
    else :
        print("물품을 찾지 못했습니다. 나중에 다시 시도해주세요.")
        sys.exit()
    stock_change = int(input("변경할 재고의 결과값을 입력하세요."))
    item_dict[item_key] = stock_change
    print("변경되었습니다.")

def remove_item() :
    want_rm = input("제거하고싶으신 물품 이름을 입력하세요.")
    if want_rm in item_dict :
        print("물품을 찾았습니다. 물품을 삭제합니다.")
        del item_dict[want_rm]
    else :
        print("물품을 찾지 못했습니다. 나중에 다시 시도해주세요.")
        sys.exit()

def print_item() :
    print("물품 출력을 시작합니다.")
    print(item_dict)
    print("출력을 마쳤습니다.")

def market_exit() :
    print("안녕히가십시오. 주인님! 나중에 또 오시길 기약하겠습니다.")
    sys.exit()

item_dict = {"만능물약" : 1000000, "신비한책" : 10, "정체를알수없는물품" : 10000}

