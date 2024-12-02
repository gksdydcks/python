    #리스트와 조건문 과제

    #2
#vending_machine = ['게토레이', '레쓰비', '생수', '이프로']
#a = input("마시고 싶은 음료? ")

#if a in vending_machine:
#    print(f"{a} 드릴게요")
#else: 
#    print(f"{a}는 지금 없네요")

    #3
vending_machine = ['게토레이', '레쓰비', '생수', '이프로']
user = input("사용자를 입력해주세요('주인', '소비자') : ")


if user == '소비자':
    beverage =  (input("음료 선택 : "))
    if beverage in vending_machine:
         vending_machine.pop(beverage)
    else:
        print(f"없음")
if user == '주인':
    fix = input("추가, 삭제 : ")
    if fix =='추가':
        vending_machine.append = input s