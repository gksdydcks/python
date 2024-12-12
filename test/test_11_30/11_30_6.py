a = [3,4,2,1]
#a. sort()# = sort(reverse =true)
a.reverse()#역순
print(a)

b=["a", "c", "d ", "b"]
b.sort()
print(b)

c = ["1", "10" , "2"]  #문자는 앞에 사전 우선 순위 
c. sort()
print(c)

d = ["강남", "강북", "서", "asdfd", "서", "서"]

first = d.index("서")+1 
print(first + d[first:].index("서"))#두번째 "서" 찾기

print(d.count("서"))


