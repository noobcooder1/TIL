
from gtts import gTTS
import os

a = 100
b = "just walk away"

print (type(a)) 
print (len(b))
print (f"hello, {b} please")
print(b[6:10])


text ="안녕하세요, 여러분. 파이썬은 재미있습니다. "
tts = gTTS(text=text, lang='en')
tts.save("ttt.mp3")
os.system("ttt.mp3")

#int() float() str() 함수를 사용하여 변환가능
#f-string : f"문자열 {변수} 문자열"
#문자형변수이름 [시작인덱스:끝인덱스] : 슬라이싱가능