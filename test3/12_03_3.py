#실습3 구구단
#a = int (input("몇 단을 출력할까요? "))
#for i in range(1,10):
#        print(f"{a} * {i} = {a*i}")
#print()

#a = sum [10,20,30]
#print(sum(a))
#sum = 0
#for i in a:
#    sum +=i
#print(sum)

#a= [1,2,3,4,5]
#a3 = []
#a4 = []
#a3 = [i*3 for i in a ]
#print(a3)

#a4 = [i*3 for i in a if i%2==0]
#print(a4)

#for y in range(3): # 경우의 수
#    for x in range(2):
#        print(f"y: {y}, x: {x}")
#   print()

for i in range(2 ,10):
    print(f"{i} 단")
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
    print()