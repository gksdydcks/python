#i=0
#while i <5:
#    i+=1
#    print(i)
#print("끝")

        #Crtl + C = 무한 루프때 종료

#num = 0     #더하기가 제일 빠름
#while num < 10:
#    num = num + 1
#    if num %2 == 0:
#        continue
#    print(num)

num = 0
a =int(input("숫자 입력 : "))
for i in range(1,a+1):
    num += i
print(f"합 : {num}")

num2 = 0
a =int(input("숫자 입력 : "))
for i in range(1, a+1):
    if i%2 ==1:         #&,% 기호 주의
         num2 +=i
print(f"합 : {num2}")

