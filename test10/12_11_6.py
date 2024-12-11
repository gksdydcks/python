# ##파일 입출력   
##text.txt                     #"w" = 파일 지우고 새로 열기
# f= open("text.txt", "w")    #!!!실행하느 코드 위치 기준이 아닌 실행하는 위치 기준 text.txt 생성!!  
# f.write("hello world\n")      #hello world 작성
# f.close()                   #파일 닫기

# f2= open("text.txt", "r") 
# f2= open("text.txt")
# print(f2.read())                #read () 괄호안 글자수 출력
# f2.close()


# f3= open("text.txt", "a")        #"a" = 내용 추가
# f3.write("hello world222\n")      
# f3.close()    

# f2= open("text.txt")
# print(f2.read())               
# f2.close()


# f= open("text.txt", "w")   
# print(f.write("hello world\n"))    
# input("멈춰!")
# f.close()                   


f2= open("text.txt")        
print(f2.read())       
f2.close()    

f3= open("text.txt")           #readline = 한줄씩 처리
print(f3.readline(), end ="")
print(f3.readline(), end ="") 
print(f3.readline(), end ="")    
f3.close()    
