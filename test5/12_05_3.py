#             #매개변수 리스트로 (배열)전달
# def times(l):
#     l2=[i*2 for i in l]
#     return set(l2)

# v2 =times([1,2,3,4,5])
# print(v2)

# def sum_mul(a,b):
#     sum=a+b
#     mul=a-b
#     return sum, mul ##리턴 2개 가능

# s, m = sum_mul(2,3)
# print(s,m)

            #실습3자판기 프로그램 함수화
vending_machine = ['게토레이', '게토레이', '레쓰비', '생수', '이프로']

def check_machine(vending_machine):
    print("남은 음료수: ", vending_machine)

def is_drink(vending_machine, drink):
    return drink in vending_machine

def add_drink(vending_machine, drink):
    vending_machine.append(drink)
    vending_machine.sort()

def remove_drink(vending_machine, drink):
    vending_machine.remove(drink)

while(1):
    check_machine(vending_machine)
    who = input("사용자 종류를 입력하세요(1.소비자, 2.주인) : ")
    if who == '1':
        drink = input("마시고 싶은 음료? ")
        if is_drink(vending_machine, drink):
            print(drink, "드릴게요")
            remove_drink(vending_machine, drink)
        else:
            print(f"{drink}는 지금 없네요")
    elif who == '2':
        todo = input("할 일 선택(1.추가, 2.삭제) : ")
        if todo == '1':
            drink = input("추가할 음료수? ")
            add_drink(vending_machine, drink)
            print("추가 완료")
        elif todo == '2':
            drink = input("삭제할 음료수? ")
            if is_drink(vending_machine, drink):
                remove_drink(vending_machine, drink)
                print("삭제 완료")
            else:
                print(f"{drink}는 지금 없네요")
        else:
            print("값이 잘 못 되었어요.")
    else:
        print("값이 잘 못 되었어요.")