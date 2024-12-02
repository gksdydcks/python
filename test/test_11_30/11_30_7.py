rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
print(f"1번")
print(rainbow[2])   #인덱스값 출력

print(f"2번")
rainbow.sort()
print(rainbow)  #알파벳 순서로 정령

print(f"3번")
rainbow.append("silver")    #좋아하는 색 추가
print(rainbow)

print(f"4번")
del rainbow[3:7]    #3~6번째 값 삭제
print(rainbow)