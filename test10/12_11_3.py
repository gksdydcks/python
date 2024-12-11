                ####sys모듈####
# import sys

# print(sys.argv)

# args = sys.argv[1:]
# print(args)

# print(int(sys.argv [1])+ int(sys.argv[2]))

            ##예제
# import sys

# args = sys.argv[1:]
# print(args)

# sum = 0
# for i in args:
#     sum +=int(i)

# print(f"합 : {sum}")

            ##예제2
import sys
args = sys.argv[1:]

if len(args) <=2 or len(args) >=4:
    print("Error")
    sys.exit(0)                                 #(or) break
if sys.argv[1]== "mul":
    print(int(sys.argv[2]) * int(sys.argv[3]))
elif sys.argv[1] == "add":
    print(int(sys.argv[2]) + int(sys.argv[3]))

##방법2
# import sys

# args = sys.argv
# if (len(args)!=4):
#     print("입력오류")
#     # sys.exit(0)   #파이선 종료
# else :
#     cmd = args[1]
#     num1 = int(args[2])
#     num2 = int(args[3])
#     if cmd == "mul":
#         print(num1*num2)
#     elif cmd == "add":
#         print(num1+num2)