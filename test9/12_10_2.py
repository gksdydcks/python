                ####클래수 상속

# class Country:
#     def __init__(self):
#         self.name = "나라이름"
#         self.popualation = "인구"
#         self.capital = "수도"
    
#     def show(self):
#         print("국가 클래스의 메소드")

# class Korea(Country):
#     def __init__(self, name):
#         self.name = name

#     def show_name(self):
#         print("국가 이름 : ", self.name)

# country = Korea("대한민국")
# country.show()
# print(country.name)
# country.show_name()

                ####매서드 오버라이딩
#class Country:
#    def __init__(self):
#        self.name = "나라이름"
#        self.popualation = "인구"
#        self.capital = "수도"
    
#    def show(self):
#        print("국가 클래스의 메소드")   #부모클래스 무시

#class Korea(Country):
#    def __init__(self, name):
#        self.name = name
#
#    def show(self):
#        print("국가 이름 : ", self.name)    #자식 출력

#country = Korea("대한민국")
#country.show()
#print(country.name)
# country.show_name()

            #실습3 )
class Calculator():
    def __init__(self):
        self.value = 100

    def sub(self,value):
        self.value -= value

class MinLimCalculator(Calculator):

    def sub(self,value):
        self.value = max(0, self.value-value)
                #방법2
        # super().sub(value)
        # self.value = max(0, self.value)
                #방법 3
        # self.value -= value
        # if self.value < 0:
        #     self.value = 0
        

cal = MinLimCalculator()
cal.sub(20)
cal.sub(90)
print(cal.value)
