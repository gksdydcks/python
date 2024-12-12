#                 # 실습 2
# stu_d = {'Alice' : 85, 'Bob':90, 'Charlie':95}
# stu_d['David']=80
# stu_d['Alice']=88
# del(stu_d['Bob'])
# for i in stu_d():
#     print(i, stu_d[i] )


#2차원 list
d=[
    [10,20],
    [30,40],
    [50,60]
]
print(d)
print(d[0][0])
print(d[1][1])
print(d.append([70, 80]))
print(d)
d[0][0] = 90
print(d)

d[1].pop(1)
print(d)

print(len(d))
print(len(d [0]))

# for i in range(0, len(4)):
#     for j in range(0, len(d[i])):
#         print(d[i][j], end="")      #for i in range =  3열일때 사용
#     print

for x, y in d:
    print(x,y)                      #for x, y in = 모든 열이 (2개[x,y] 고정)다 동일할때 사용