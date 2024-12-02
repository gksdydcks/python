print("오늘은 12월 %d일 입니다." % 2)
print("오늘은 %d월 %d일 입니다." % (12,2))
print("오늘은 %d%s %d일 입니다." % (12,'월',2))
print(f"오늘은 {12}{'월'} {2}일 입니다.")
print("오늘은 " +str(12)+"월 "+str(2)+"일 입니다.")
print("오늘은 ",12,"월 ",2,"일 입니다.",sep="")

print("Hello".upper())      #대문자로 바꿈 코딩테스트 문제
print("Hello".lower())      #소문자로 바꿈 코딩테스트 문제

        #split !!!코딩테스트 , AI 단골  가장 중요
friends = "고찬국 김다운 김민창"
a = friends.split("김") #" "띄어쓰기 디폴트
print(a)

email = "jerry@spreatics.com"
print(email.split('@')) # @기준으로 split

sentence = "{}월 {}일".format(12,2) #12월 2일 {} 안에 쓴 순서대로 나음 빈칸은 그대로출력
print(sentence)

b = "   111     222     " 
print(b.replace("111, 222"))
#print(b.strip())  #srtip = 앞뒤 공백만 제거 lstrip() = 왼쪽 제거, rstrip() = 오른쪽 제거
#print(b.split())

