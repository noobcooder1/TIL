def count_vowel(word):
    moem = ["a", "e", "i", "o", "u"]         #파이썬은 하나의 문자열도 배열취급되기에 string in 'aiueo' 을해도 만족한다.
    count = 0
    for i in range(len(word)):
        wd1 = word[i]
        if wd1 in moem:
            count += 1
    print(count)

word = str(input("모음이 몇 개인지 궁금한 문자열을 입력하세요."))
count_vowel(word)