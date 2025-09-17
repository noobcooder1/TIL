# 연산자 연습으로 만든 당신이 갖고싶은 시간을 입력받고 그것을 일, 시간, 분, 초로 변환해주는 프로그램이다.

wanttime = input("당신이 갖고싶어하는 시간의 양을 입력하시오. 단위는 년(year)입니다. : ")

wanttime = int(wanttime)

wantday = wanttime*365
wanthour = wantday*24
wantmin = wanthour*60
wantsec = wantmin*60

print("당신이 원하는 시간은 총", wantday, "일 \n", wanthour, "시간 \n", wantmin, "분 \n", wantsec, "초 입니다.")