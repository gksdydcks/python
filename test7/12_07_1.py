    # # 함수 안에 함수 사용 가능
# def b():
#     def c():
#         print("c")
#     c()
# b()

## l = ["p","y","t","h","o","n"]   # 문자를 리스트로 변환 = join
## print("".join(l))

                        ##복습 문제1
# def solution(arr, divisor):
#     answer = []
#     for i in arr:
#         if i % divisor == 0:
#             answer.append(i)
#     if len(answer)==0:  
#             answer= [-1]
#     return sorted(answer)


        ###print (1 if 1<0 else 0)  
        ###print ("abc"if 1>0 else "bcd")  #많이 쓰임
        ##위 두문장과 같음
        ## if 1<0:
        ##     print("abc")
        ## else:
        ##     print("bcd")


                        ##복습문제 2
# def solution(numbers):
#    set_a = set()
#    l = len(numbers)
#    for i in range(l-1):
#        for j in range(i+1, l):
#             set_a.add (numbers[i]+numbers[j])          
#    return sorted(set_a)


                ##복습문제 3 하샤드수
##1번방법
# def solution(x):
#     x_1 = sum(list(map(int, str(x))))
#     if x%x_1 ==0:
#          answer = True
#     else:
#          answer = False
#     return answer

##2번 방법
# def solution(x):
#     s= str(x)
#     sum = 0
#     for i in s:
#         sum +=int(i)
# #return True if x %sum ==0 else False
#     return x%sum ==0


                ##복습문제4  문자열 내림차순으로 배치
##1번방법
# def solution(s):
#     l = list(s)
#     l.sort()
#     l.reverse()
#     answer ="".join(l)
#     return answer

##2번방법


                ##복습문제5(딕셔너리)  추억점수               #김다운 크루#김희수 크루
    ##1번방법 !!!시간초과 남
def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        sum = 0
        for j in range(len(name)):
            if name[j] in photo[i]:
                 sum += yearning[j]
        answer.append(sum)     
    return answer

    ##2번방법 !!!딕셔너리!!!  zip사용 !딕셔너리 사용하면 시간초과 안남
def solution(name, yearning, photo):
    answer = []
    d = {}
    for i in range(len(name)):
        d[name[i]]=yearning[i]
    d=dict(zip(name,yearning))
    for i in photo:
        sum = 0
        for j in i:
            v=d.get(j)
            if v:
                sum +=v
        answer.append(sum)
    return answer
    ##3번 방법 !딕셔너리 사용 zip사용x
def solution(name, yearning, photo):
    answer = []
    d = dict()
    
    for i in range(len(name)):
        d[name[i]] = yearning[i]
    
    for j in photo:
        total = 0
        for names in j:
            if names in d:
                total += d[names]
        answer.append(total)
    
    return answer

                ##복습문제 6 (list 슬라이싱) 크기가 작은 부분 문자열
def solution(t, p):
    answer = 0
    lp =len(p)
    for i in range(len(t)-lp+1):
        if t[i:i+lp] <= p:
            answer+=1
    return answer