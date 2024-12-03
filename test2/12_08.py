#3 자판기 프로그램 응용
vending_machine = ['게토레이','게토레이','레쓰비','레쓰비','생수','생수','생수','이프로']
user = ['소비자','1', '주인', '2']
set = ['추가', '1', '삭제', '2']

user =input("사용자를 입력해 주세요 \n 1.소비자   2.주인\n : ")

if user == '소비자' or user == '1':
    a =input("마시고 싶은 음료? ")
    if a in vending_machine:
        print(f"{a} 드릴게요")
        vending_machine.remove(a)
        print(f"남은 음료수{vending_machine}")
    else: 
        print(f"{a}는 지금 없네요")
else:
    print("Error")  

if user == '주인' or user == '2':
    set =input("    수정 사항 입력 \n 1.추가    2.삭제 \n : " )
    if set =='추가' or set =='1':
        print(f"남은 음료수{vending_machine}")
        a =input("추가할 음료수를 입력해주세요 : ")
        vending_machine.append(a)
        vending_machine.sort()
        print(f"추가 완료.\n남은음료수 : {vending_machine}")
    elif set == '삭제' or set =='2':
        print(f"남은 음료수 : {vending_machine}")
        a =input("삭제할 음료수를 입력해주세요 : ")
        if a in vending_machine :
            vending_machine.remove(a)
            print(f"삭제 완료.\n남은음료수 : {vending_machine}")
        else:
            print(f"{a}는 없습니다.")
    else:
        print("Error") 