                ###time 모듈
import time

# a=time.time()
# time.sleep(2)
# b=time.time()
# print(b-a)

# print(time.time())
# print(time.localtime())
# time_Str = time.localtime()
# print(time_Str.tm_year)

# print(time.ctime())
# # print(time.ctime(a))
# # print(time.ctime(b))
    
# year = (time.time()/(365*24*60*60))    ##1970년 1월1일 기준
# print(year)
# day = (time.time()/(24*60*60)) 
# print(day)
                #####
            ##수행시간 측정
# start = time.time()

# for i in range(10):
#     print(i)
#     time.sleep(1)

# end = time.time()
# print(f"수행시간 : {round(end-start)}초")

            ##수행시간 측정함수로 만들기
def check_time(func):
    start = time.time()
    func()
    end = time.time()
    print(f"수행시간 : {round(end-start)}초")

def a():
     for i in range(10):
        print(i)
        time.sleep(1)
def b():
     for i in range(100):
        print(i)
        time.sleep(0.5)        

# check_time(a)
check_time(b)