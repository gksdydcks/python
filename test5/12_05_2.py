        #함수 
        #interprint 방식이라 함수쓸려면 위에서 모든 함수 선언하고 사용
# def f(x):   #매개변수 있을때
#     result = x**2 + 2*x + 1
#     return result
# print(f(3))

# def sayhi():  
#     print("hi")
#     print("hi")
#     print("hi")
# sayhi()    

# x = 10
# def func2():
#     print("func2",x) 

# def func():
#     x = 20
#     y = 11
#     print("func",x, y) #함수 안에서만 사용가능
# func()
# print("main",x)

# func2()#함수와 떨어져 있어도 사용가능

# def func3(x):
#     print("func3",x)
# func3(3)    #지역변수라 10이 아닌 3
                
                #실습1

# def a(x,y):  

#     if x == y :
#         print(f"결과(곱): {x*y}")
#     else:
#         print(f"결과(합): {x+y}")  
# a(2,2) 
# a(2,3)

                #실습2
def price(a,b):
    if a*b >= 20000:
        print(f"상품1 가격: {a*b}원")
    else:
         print(f"상품2 가격: {a*b+2500}원")
price(10000,3)
price(15000,1)