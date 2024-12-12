#복습1
# def solution(arr):
#     answer = []
#     for i in arr:
#         if i >=50 and i%2 ==0:
#             answer.append(i//2)
#         elif i<50 and i%2 ==1:  
#             answer.append(i*2)
#         else:
#             answer.append(i)
#     return answer

#복습 2
def solution(myString):
    answer =[]
    o = myString.split("x")
    for i in o:
        answer.append(len(i))

    return answer

#복습 3
def solution(str1, str2):
    
    if str1 in str2:
        return 1
    else:
        return 0