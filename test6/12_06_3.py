            #
            #!!재귀함수!!'  #종료조건 없으면 무한 반복이라 에러  
# def hello(): #출력 3번되고 멈추게 하기
#     global a
#     a += 1
#     if a < 4:
#         print("hello")
#         hello()
   
# a=0
# hello()

# #실습2 재귀함수로 피보나치 수 구하기


# def fi(n):
#     if n <= 2:          # 2보다 같거나 작으면
#         return 1        # 1출력
#     else:
#         return fi(n-1) + fi(n-2)    #출력
    
# print(fi(1))

# 큰수 구할때
memory = {1: 1, 2: 1}

def fibo_memoization(n):
    if n in memory:
        number = memory[n]  #
    else:
        number = fibo_memoization(n-1) + fibo_memoization(n-2)
        memory[n] = number
    return number

print(fibo_memoization (6))
print(fibo_memoization (100))

#하노이 탑 코드     #https://vidkidz.tistory.com/649
def hanoi(number_of_disks_to_move, from_, to_, via_):
    if number_of_disks_to_move == 1:
        print(from_, "->", to_)
    else:
        hanoi(number_of_disks_to_move-1, from_, via_, to_)
        print(from_, "->", to_)
        hanoi(number_of_disks_to_move-1, via_, to_, from_)