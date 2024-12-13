                ##finally 예제)
# while True:
#     try:
#         num = int(input("정수 입력 : "))
#         print(f"정수 입력 성공 : {num}")    
#         break
#     except ValueError : 
#         print("정수가 아님! 정수를 입력해 주세요")
#     finally:
#         print("finally는 무조건 실행")


                ####raise
# a=1
# try:
#     a+=1
#     if a > 1:
#         raise Exception           #특정 상황에서 강제 에러발생
#     a+=2
#     print("a", a)
# except :
#     print("error",a)

                ####
class Animal:
    def breathe(self):
        print("숨을 쉰다")
    def cry(self):
        raise NotImplementedError       #오버라이드 안하면 에러발생

class Dog(Animal):
    def cry(self):
        print("멍멍")

d= Dog()
d.breathe()
d.cry()