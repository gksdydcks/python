             #tuple
#t1 = (10, 20, 30)
#print(type(t1))
#print(t1)
#print(t1[0])
#del(t1[0])#특정원소 삭제 안됨
#t1[0] =3 안됨
#del (t1)

#t2=(10)
#t3=(10,)
#t4=10,20 #,있으면 tuple
#print(type(t4))

            #set
set1 = {1,2,3,3} #set >중복 출력 안됨
print(set1)
set2 = set({2,1,3,3}) 
print(set2)
set2.add(4)
print(set2)
while len(set2) > 0:
    a= set2.pop()
    print(a)
print()

l1 = [1,2,3,3]
while len(l1) > 0:
    a= l1.pop()
    print(a)

set3= set("apple") #set은 정렬 안됨!!
print(set3)
while len(set3) > 0:
    a =set3.pop()
    print(a)