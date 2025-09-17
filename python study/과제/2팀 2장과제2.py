# import webbrowser
# url = input("웹 사이트 URL을 입력하시오: ")
# webbrowser.open("https://www."+ url +".com")

import webbrowser

#url인코딩


s = input("번역할 영어 문장을 입력하시오: ")
url = "https://translate.google.com/#en/ko/" + s
webbrowser.open(url)