#         #for x,y in d:  사용해 3단 출력하기          
d =[ [3,1],
[3,2],
[3,3],
[3,4],
[3,5],
[3,6],
[3,7],
[3,8],
[3,9]
]
for x, y in d:             #모든 열이 2개(x,y) 일때만 쓰임 
    print(f"{x} x {y} = {x*y}")
print()

for i in d:
        print(f"{i[0]} x {i[1]} = {i[0]*i[1]}")
print()

for i in range(len(d)):
    print(f"{d[i][0]} x {d[i][1]} = {d[i][0]*d[i][1]}")