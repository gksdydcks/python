# #람다식
# add = lambda x,y : x+y
# print(type(add))
# print (add (1,2))   #함수를 변수로 쓸 수 있음

# def add2(x,y):
#     return x+y

# add3=add2
# print (add(1,2))
# print (add3(1,2))
 
                    #람다함수 매개변수 전달
# def call_3(func):
#     for _ in range(3):
#         func()
# call_3(lambda : print("hi"))
# call_3(lambda : print("hello"))

# def download(startCallback,endCallback):
#     startCallback()
#     print("다운로드 중")
#     endCallback()
# download(lambda : print("다운로드 시작"),lambda : print("완료되었습니다."))

                ###
                #map #일회용 함수
# list(map(int, ["1","2","3"]))

# result = map(lambda x:3*x, [1,2,3,4])
# print(list(result))

# li = [-5,1,2,-11,76]
# value = list(filter(lambda x:x<0, li))
# print(value)

# value = list(filter(lambda x:x>10, li)) #map 과 비슷하지만 x:x>10 같이 특정한 값만 출력
# print(value)

#예제 2배후 3이상인것만 출력
li = [-5,1,2,-11,76]
print(list(filter(lambda x:x>=3, map(lambda x:x*2, li))))
