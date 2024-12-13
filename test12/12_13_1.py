# with open("./output/data.bin", "wb") as f:
#     txt = "안녕"
#     # f.write(txt)
#     f.write(txt.encode())

# with open("./output/data.bin", "rb") as f:
#     data = f.read()
#     print(data)
#     print(data.decode())

# with open("./output/cap_1.jpg", "rb")as f1:
#     img = f1.read()
    
# with open("./output/cap_2.jpg", "wb") as f2:
#     f2.write(img)

                    ####
            ###예외처리 실습)
# try:
#     num = int(input("정수 입력"))
# except ValueError : 
#     print("정수가 아님!")

# try:
#     num = int(input("정수 입력"))
# except ValueError as msg:           #에러난 이유 확인가능
#     print(msg)

# try:
#     num = int(input("정수 입력"))
# except Exception as msg:            #최상단인 exception만 알아도 됨
#     print(msg)
# else:
#     print("예외 없음")

# try:
#     num = int(input("정수 입력"))
# except IndexError as msg:            #!!index - value -excep (작은순)순으로 쓴느게 좋음
#     print("IndexError",msg)
# except ValueError as msg:           #똑같은 오류는 순서 중요
#     print("ValueError", msg)
# except Exception as msg:            #최상단인 exception만 알아도 됨!
#     print("Exception",msg)
# else:
#     print("예외 없음")


                ###실습2 )정수 입력받기
# import sys
while True:
    try:
        num = int(input("정수 입력 : "))
        print(f"정수 입력 성공 : {num}")
        break
        # sys.exit(0)
    except ValueError : 
        print("정수가 아님! 정수를 입력해 주세요")
    
        
