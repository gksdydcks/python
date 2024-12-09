            ##실습1) 사칙연산 클래스 만들기
class Num:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def add(self):                     
        return self.__a + self.__b 

    def sub(self):
        return self.__a - self.__b

    def mul(self):
        return self.__a * self.__b
    
    def div(self):
        if self.__b  == 0:  #사칙연산에서 0이 나오면 안됨 
            return "Error"
        else:
            return self.__a / self.__b
a= Num(4,0)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())