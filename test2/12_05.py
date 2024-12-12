        #실습
a= int(input("점수를 입력하세요 : "))

if a<60:
    print("E")
elif a<70:
    print("D")
elif a<80:
    print("C")
elif a<90:
    print("B")
else:
    print("A")
if a>100:
    print("Error\n만점은 100점")