#실습  #김사무엘

age = int(input("나이를 숫자로 입력해 주세요 : "))
pay = input("결제 방법을 입력해주세요('카드', 또는 '현금'만 입력) : ")
b = pay=='카드'

if age <8 or age>=75:
    if b:
        print(f"{age}세의 {pay} 요금은 무료 입니다")
    else:
        print()
elif age <14:
     if b:
        print(f"{age}세의 {pay} 요금은 450원 입니다")
     else:
        print()
elif age <20:
    if b:
        print(f"{age}세의 {pay} 요금은 720원 입니다")
    else:  
         print(f"{age}세의 {pay} 요금은 1000원 입니다")
elif age <75:
    if b:
        print(f"{age}세의 {pay} 요금은 1200원 입니다")
    else:  
         print(f"{age}세의 {pay} 요금은 1300원 입니다")

