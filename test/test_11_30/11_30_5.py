a = []  #lsit 만들기
b = [1,2,3,4]
c = ["장원영","안유진"]
d = [1, "아이브"]

#print(len(c))   #[]lsit 개수
#print(c[0])     #c에있는 0번째 !0부터 시작
#print(c[1])
#c[0] = "카리나"
#print(c)
#del c[0]
#print(c)

#c.append("Asd")  #append = 추가
#c.append("sdf")
#print(c)

print (b[-1]) #[-1]뒤에서 첫번째
print (b[-2])
print (type(b))

                            #!!!슬라이싱!!!중요 
seasons = ["봄", "여름", "가을", "겨울"]
print(seasons[0:1]) 
print(seasons[0:2])
print(seasons[:2]) #앞에 없으면 처음부터
print(seasons[1:]) #뒤에 없으면 끝까지
print(seasons[2:])
print(seasons[:])#처음부터 끝까지
print(seasons)
print(seasons[::3])
print(seasons[::-2]) #!!뒤에서부터 처음까지 [::-1]

seasons2 = ["봄", "여름", "가을", "겨울", [1,2,3,4]]
print(seasons2[-1][0]) #큰리스트에서 뒤에서 1 에서 첫번째

abcd = "abcd"
abc = ['a','b', 'c', 'd']
print(len(abcd))  #len = list 개수
print(len(abc))

                    #list 슬라이싱구조 [start:stop:step]
a = [1,2,3,4,5,6,7,8,9,10]
even = a[1::2]
print(even)