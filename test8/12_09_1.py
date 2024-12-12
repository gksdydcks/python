#         ###문제 7 콜라츠 수열 만들기 (재귀함수 이용)
# def solution(n):
#     answer = []
    
#     def collat(x):
#         answer.append(x)
#         if x == 1:
#             return
#         elif x%2 == 0:
#             collat(x/2)
#         else :
#             collat(x*3+1)
#     collat(n)
#     return answer

#         ###숙련자 문제 1)특이한 정렬
# def solution(numlist, n):
#     answer = []
#     d = {}
#     for i in numlist:
#         d[i] = abs(i-n)
#     d1 = sorted(d.items(), key= lambda item:(item[1], -item[0]))
#     print(d.items())
#     print(d1)
    
#     for i in d1:
#         answer.append(i[0])
    
#     return answer

#             ###숙련자 문제 2) 옹알이(1)
# def solution(babbling):
#     answer = 0
    
#     can = ["aya", "ye", "woo", "ma"]
           
#     for i in babbling:
#         for j in can:
#             idx = i.find(j)
#             if idx > -1:
#                 print(idx, i, j)
#                 i= i.replace(j, '_')
#                 print (idx, i, j)
#         i = i.replace('_', '')
#         if len(i) == 0:
#             answer+=1
#     return answer


            ### 숙련자 문제 3) 하노이 탑
def solution(n):
    answer =[]
    
    def hanoi(n,f,t,v):
        if n == 1:
            answer.append([f,t])
        else :
            hanoi(n-1, f,v,t)
            answer.append([f,t])
            hanoi(n-1,v,t,f)
    hanoi(n,1,3,2)
    
    return answer


