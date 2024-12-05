# def oneop():
#     global x    #함수 밖에 있는 x 의미
    
#     x=x+1
#     return x
# x = 0
# print(oneop())
# print(oneop())
# print(oneop())

#파이선은 선언과 할당이 따로 존재x

#실습 5
count = 0
n = 3
def get_times(n):
    global count
    for i in range(1,31):
        if i %n ==0:
            print(i, end=" ")
            count +=1

get_times(n)
print(f'\n{n}의 배수의 개수: {count}')