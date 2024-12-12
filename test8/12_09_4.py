# class Movie:
#     count = 0 
#     def __init__(self, title, audience):    #init =초기화
#         self.__title = title             #__직접 접근 안되고 함수만들어 접근
#         self._audience = audience
#         Movie.count += 1  
        

#     def get_title(self):
#         return self.__title
    
#     # def set_title(self,title):          #함수를 만들어서 접근
#     #     self.__title = title

#     def get_audience(self):
#         return self._audience

# movie1 = Movie("파묘", 100)
# # print(movie1.__title)                  #title에 접근할수 없어 안됨
# print(movie1.get_title())
# # movie1.__title="오겜"                  #movie1.__title 새로 만듬 (위__title 과는 다름)
# # print(movie1.get_title())
# # print(movie1.__title)
# print(movie1._audience)
# print(movie1.get_audience())
# movie1._audience = "300" 
# print(movie1.get_audience())

                ####연습문제
class MyAdd:
    __a = 1
    __b = 2
    
    def sum(self):                      #sum 설정
        return self.__a + self.__b      #__a+__b 
    def set_a(self, a):                 #set_a 라는 함수 만들기
        self.__a = a
a = MyAdd()
print(a.sum()) # 3
a.set_a(3)                              #a를 3으로 변경
print(a.sum()) # 5

                ###정보 은닉
class Health:
    def __init__(self, name):
        self.__name = name
        self.__hp = 100

    def getName(self):
        return self.__name
    
    def setHp(self, hp):
        hp = max(hp, 0)
        hp = min(hp, 100)
        self.__hp = hp

    def getHpStr(self):
        return "hp: " + str(self.__hp)
    
    def exercise(self, hours):
        self.setHp(self.__hp + hours)
        print(f"{hours}시간 운동하다")

    def drink(self, cups):
        self.setHp(self.__hp - cups)
        print(f"술을 {cups}잔 마시다")

p1 = Health("나몸짱")
p1.setHp(100)
p1.exercise(5)
p1.drink(2)
print(f"{p1.getName()} - {p1.getHpStr()}")

p2 = Health("나약해")
p2.setHp(10)
p2.exercise(1)
p2.drink(12)
print(f"{p2.getName()} - {p2.getHpStr()}")