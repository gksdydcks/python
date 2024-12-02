    #리스트와 조건문 과제

 #2
vending_machine = ['게토레이', '레쓰비', '생수', '이프로']
a = input("마시고 싶은 음료? ")

if a in vending_machine:
    print(f"{a} 드릴게요")
else: 
    print(f"{a}는 지금 없네요")
   