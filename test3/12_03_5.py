#실습 5 리스트 평균 구하기

#a = list(map(int,input("숫자 여러 개 입력 : ").split()))
#print(a)

a = list(input("숫자 여러 개 입력 : ").split())
a = [int (b) for b in a]
print(a)

max_a = max(a)
min_a = min(a)

print(f"가장 큰 값: {max_a}")     
print(f"가장 작은 값: {min_a}")

a.remove(max_a)
a.remove(min_a)
avg = sum(a)/len(a)
print(f"나머지 값의 평균:{avg}")

