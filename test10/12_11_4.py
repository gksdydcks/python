#             ##os모듈
# import os

# os.chdir("C:/Users/gksdydcks/Documents/python") #디렉터리 경로
# dir = os.popen("cat README.md")   #dir 명령으로 열기
# print(dir.read())       #디렉토리 보기(읽기)
# print(os.listdir())     # 파일을 리스트에 저정

##실습)타자 연습게임
import random
import time

word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
        'grape', 'garlic', 'onion', 'potato']

n = 1

input("[타자 게임] 준비되면 엔터!")
start = time.time()

while n <11:
    print("문제", n)
    question = random.choice(word)
    print(question)
    user = input()
    if question == user:
        print("통과!!")
        n += 1
    else:
        print("오타! 다시도전!")

end = time.time()
et = end -start
print(f"타자 시간 : {et: .2f}초") #:.2f소숫점 2째자리까지
