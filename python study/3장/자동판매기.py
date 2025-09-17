import sys

print("안녕하세요. 자동판매기입니다. 판매하는 물건은 다음과 같습니다. \n " 
      "1. 수치(500원) \n 2. 물건(600원) \n 3. 능력(700원) \n 4. 기타(800원)" )

product = input("구매할 물건의 번호를 입력하시오.")

if (product == '1'):
    product = "수치"
    price = 500
elif (product == '2'):
    product = "물건"
    price = 600
elif (product == '3'):
    product = "능력"
    price = 700
elif (product == '4'):
    product = "기타"
    price = 800
else:
    product = "판매하지 않는 물건"
    price = 0
    print("판매하지 않는 물건입니다. 종료합니다.")
    sys.exit()
    

print ( "당신이 선택한", product, "의 가격은,", price, "입니다. \n")

money = input("투입할 금액을 입력하시요.")

money = int(money)
change = money - price

coin500 = change // 500
change = change % 500
coin100 = (change % 500) // 100
change = change % 100
coin50 = (change % 100) // 50
change = change % 50
coin10 = (change % 50) // 10
change = change % 10

print("잔돈은 500원", coin500, "개, 100원", coin100, "개, 50원 ", coin50, "개, 10원, ", coin10, "개 입니다.")