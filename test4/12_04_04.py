                #set 실습 1

# import sys                    #속도향상
# input = sys.stdin.readline    #속도향상
n, m = map(int, input().split()) # 입력한 값에서 n, m 설정
s = set()

for i in range(n): #n번 만큼 루프
    data = input()
    s.add(data) # s에 data 추가

count = 0
for i in range(m):
    data = input()
    if data in s:
        count +=1

print(count)
