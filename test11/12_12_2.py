    ##파일쓰기 -입력받기       #output폴더 input파일
# import sys
# with open("./output/input.txt", "a") as f:          #"a" 파일에 계속 추가
#     while True:
#         text = input("저장할 내용을 입력해 주세요(종료 -z) : ")
#         if text == 'z' or text == 'Z':
#             break
#             #sys.exit(0)
#         f.write(text + "\n")
    
                    ##
            #실습1) 회원 명부 작성
# with open("./output/members.txt", "a") as a:
#     for i in range(3):
#         n = input("이름 입력 : ")
#         p = input("비밀번호 입력 : ")
#         a.write(f"{n}  {p}\n")

# with open("./output/members.txt", "r") as a:
#     print(a.read())


                ##실습2)

# n = input("이름 입력 : ")
# p = input("비밀번호 입력 : ")

# with open("./output/members.txt", "r") as a:
#     for i in a:
#         n_n, p_p = i.split() 
#         if n_n == n and p_p ==p:
#             print("성공")
#             break
#         else:
#             print("실패")
#             break

                ##실습2)방법2)딕셔너리 사용     #for문 안써도됨 #여러번 반복가능
# dictUser = {}       

# with open("./output/members.txt", "r") as a:
#     for line in a:
#         n, p = line.split()
#         dictUser[n] = p
# # print(dictUser)       
# # for i in range(100) :                         #반복
# name = input("이름을 입력하세요: ")
# pw = input("비밀번호를 입력하세요: ")

# if pw == dictUser.get(name):
#     print("로그인 성공!")

# else:
#     print("로그인 실패!")


                ###실습3)로그인 성공시 전화번호 저장하기
dictUser = {}       

with open("./output/members.txt", "r") as a:
    for line in a:
        n, p = line.split()
        dictUser[n] = p

name = input("이름을 입력하세요: ")
pw = input("비밀번호를 입력하세요: ")

if pw == dictUser.get(name):
    print("로그인 성공!")
    with open("./output/members_tel.txt", "a") as b:
        tel = input(("전화번호를 입력하세요 : "))
        b.write(f"{name}  {tel}\n")
        b_b= open("./output/members_tel.txt", "r")
        for i in b_b:
            if b_b in name:
                b_b.seek(5)
                print(b.write(tel))

else:
    print("로그인 실패!")