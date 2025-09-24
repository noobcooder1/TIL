want_time = int(input("가지고싶으신 시간을 말하시오.(단위:년) "))

print("당신이 원하는 시간의 변환을 시작하겠습니다.")
print(want_time * 365 * 24 * 60 * 60, "second")
print("분:", want_time * 365 * 24 * 60, "minute")
print("시간:", want_time * 365 * 24, "hour")
print("일:", want_time * 365, "day")