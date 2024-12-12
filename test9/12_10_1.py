#                 ###실습 2) supermarket 클래스
# class Market:
#     count = 0

#     def __init__(self, location, name, product, customer):
#         self.__location = location
#         self.__name = name
#         self.__product = product
#         self.__customer = customer
#         Market.count += 1

#     def print_location(self):
#         print(f"가게 위치 : {self.__location}")
       
    
#     def change_category(self, product):
#         self.__product = product
    
#     def show_list(self):
#         print(f"파는 물건 : {self.__product}")
    
#     def enter_customer(self):
#         self.__customer +=1
    
#     def show_info(self):
#         print(f"가게 이름 : {self.__name}")   
#         print(f"가게 위치 : {self.__location}")
#         print(f"파는 물건 : {self.__product}")
#         print(f"손님 수 : {self.__customer}")      
    
#     def show_supermarket_count(self):
#         print(f"인스턴스 갯수{Market.count}")
    
# a = Market("공덕", "gs", "물", 10)  
# b = Market("홍대","cu", "콜라", 6)

# a.print_location()
# a.change_category("우유")
# a.show_list()
# a.enter_customer()
# a.show_info()

# a.show_supermarket_count()

            ## 실습2(리더님 코드)
class SuperMarket:
    instance = 0 
    def __init__(self, location, name, product, customer):
        SuperMarket.instance+=1
        self.__location= location # 위치
        self.__name= name # 가게 이름
        self.__product= product # 파는 물건
        self.__customer= customer # 고객의 수

    def print_location(self):
        print(f'위치: {self.__location}')

    def change_category(self, another_product):
        self.__product = another_product

    def show_list(self):
        print(f'상품: {self.__product}')

    def enter_customer(self):
        print("손님 입장")
        self.__customer += 1
        return self.__customer

    def show_info(self):
        print(f'위치: {self.__location}, 이름: {self.__name}, '
             f'상품: {self.__product}, 고객수: {self.__customer}')
    
    def show_supermarket_count(self):
        print("클래스 인스턴스 개수 : ", SuperMarket.instance)
        


# 테스트
super1 = SuperMarket("마포구 염리동", "마켓온", "과일", 10)
super1.print_location()
super1.change_category("음료")
super1.show_list()
super1.enter_customer()  # 고객 들어옴
super1.enter_customer()
super1.show_info()
super1.show_supermarket_count()

super2 = SuperMarket("마포구 도화동", "마켓투", "채소", 15)
super2.show_info()
super2.show_supermarket_count()