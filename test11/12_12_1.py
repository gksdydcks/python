        ##readline

# f4= open("text.txt")        
# print(f4.readlines())
# f4.close()    

# f= open("text.txt", "w")    
# f.write("12345678")     
# f.close()                   

# f5= open("text.txt", "r+")     
# print(f5.read())
# print(f5.tell())            #seek = 특정 위치로 이동 
# f5.seek(4)                  #seek(0) = 처음으로 돌아가서 읽음 
# print(f5.write("8"))
# f5.close() 

# f6= open("text.txt", "r+")  
# str6 = f6.read()      
# print(f6.tell())            
# f6.seek(str6.find('5'))                 
# print(f6.write("8"))
# f6.close() 


#                 ###with~ as
# with open("text.txt", "r+") as f7:
#     str6 = f7.read()    
#     print(f7.tell())            
#     f7.seek(str6.find('4'))                 
#     print(f7.write("6"))

# import random
# import time


                ###영어타자연습 프로그램 만들기
import random
import time
import sys
# with open("word.txt", 'w') as f:
#     word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
#             'grape', 'garlic', 'onion', 'potato']

try:                                    #if os.path.exists("word.txt"):
    with open("word.txt", 'r') as f:    #    with open("word.txt", 'r') as f:
        word = f.read().split()         #        word = f.read().split()

except:                                 #else :
    print("파일을 찾을 수 없습니다.")     #    word = ['sky', 'earth', 'moon', 'flower', 'tree', 'apple',
    sys.exit(0)                         #        'grape', 'garlic', 'onion', 'potato']

n = 1
input("[타자 게임] 준비되면 엔터!")
start = time.time()

while n <11:
    print("문제", n)
    question = random.choice(word)  
    print(question)
    user = input()
    if question == user:
        print("통과!!")
        n += 1
    else:
        print("오타! 다시도전!")

end = time.time()
et = end -start
print(f"게임 소요시간 : {et: .2f}초") 

