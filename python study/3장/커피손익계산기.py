americano_price = int(input("아메리카노의 가격을 입력하세요."))
cafelatte_price = int(input("카페라떼의 가격을 입력하세요."))
capucino_price = int(input("카푸치노의 가격을 입력하세요."))

americano_sell = int(input("아메리카노의 판매량을 입력하세요."))
cafelatte_sell = int(input("카페라떼의 판매랑을 입력하세요."))
capucino_sell = int(input("카푸치노의 판매량을 입력하세요."))

coffee_cost = 1000
sales = (americano_price * americano_sell) + (cafelatte_price * cafelatte_sell) + (capucino_price * capucino_sell)
coffee_benefit = sales - (americano_sell + cafelatte_sell + capucino_sell) * coffee_cost


print("오늘 카페의 총 매출은", sales, "원 입니다.")
print("오늘 카페의 총 재료비는", sales - coffee_benefit, "원 입니다.")
print("오늘 카페의 총 순이익은", coffee_benefit, "원 입니다.")