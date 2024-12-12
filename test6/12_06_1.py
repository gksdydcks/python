                #!!중요!!
                #!!중요!!
                #!!중요!! 함수의 기본 매개변수
# def pr_str(txt, count=1, count2=1):   #디폴트가 앞에 나와야 하는이유 : 어떤게 생략 됬는지 알기위해
#     for i in range(count):
#         print(txt)
#         print(count2)

# pr_str("Hello", 3, 2)
# pr_str("Hello", 3)
# print()
# pr_str("Hello")
# print()
# # pr_str() #txt='12'
# # l=[]
# # l.pop

                #!!중요!!
                #!!중요!!
                #!!중요!! 함수의 가변 매개변수
# def calc_avg(*numbers):                 #수정못하게 튜플로 들어옴
#     print(type(numbers))
#     print(numbers)
#     return sum(numbers)/len(numbers)

# print(calc_avg(1,2))                    #위 *없으면 [(1,2)]튜플로 넣기
# print(calc_avg(1,2,3,4,5))

# def a():
#     return 1,2
# print(a())  

            #가변 키워드 매개변수
def intro(**kw):
    print(type(kw))
    for k, v in kw.items():     ##!중요!.item 딕셔너리에 사용 
        print(f"{k}: {v}")
    for i in kw:
        print(f"{i}")

intro(name="Alice", age=25, city="NY")
