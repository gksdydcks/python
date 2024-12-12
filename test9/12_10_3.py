# #                     ##모듈
#     #방법1
# import clac_module            #ctrl 클릭 하면 해당 모듈작성된 파일로 이동

# print(clac_module.add(1,2))
# print(clac_module.sub(1,2))
# print(clac_module.mul(1,2))
# print(clac_module.div(1,2))
#     #방법 2
# from clac_module import add
# print(add(1,2))
# # calc_module.add() # 안됨
#     #방법3
# import clac_module as cm        #clac_module 에서cm 으로 모듈 이름 변경
# print(cm.add(1,2))

            ##파이썬 표준모듈 -math
#     ##방법1
# import math
# print(math.floor(3.141592))
# print(math.ceil(3.141592))
# print(math.sqrt(9))

#     ##방법2
# from math import floor, ceil
# print(floor(3.141592))
# print(ceil(3.141592))

        ##random
# import random
# print(random.randint(1,5))
# print(random.uniform(1,2))
# print(random.random())
# print(random.randrange(1,3))    #(b 미포함>b-1까지)
# print(random.randrange(1,5,2)) #(a,b,step)

            ##실습)up_down_game
import random

com = random.randint(1, 100)
count = 0
score = 100
min_v = 1
max_v = 100

while True:
    try: 
        if count == 10:
            print(f"횟수 초과")
            break   

        count += 1
        score -= 10            
        guess = int(input(f"숫자 입력({count}회]%d ~ %d) : " % (min_v, max_v)))
        
        if guess < 0 or guess > 100:
            print("입력범위 초과")
        elif com == guess:
            print(f"정답! {guess}")
            print(f"점수 : {score}")
            break

        elif com > guess:
            print("랜덤 수 보다 작아요")
            min_v = guess
            
        else:
            print("랜덤 수 보다 커요")
            max_v = guess
           
    except ValueError:
        print("숫자만 입력 가능합니다.")