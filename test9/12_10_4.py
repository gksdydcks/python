            ###실습 로또 번호 뽑기
# import random
# lotto = []
# a = random.randint(1, 45)
# for i in range(6):                  #a(랜덤숫자)) 6번 반복
#     while a in lotto:               #lotto에 a(랜덤숫자)있으면
#         a = random.randint(1, 45)   #a(랜덤숫자 생성)실행
#     lotto.append(a)                 #lotto 리스트에 a(랜덤숫자)저장

# print(sorted(lotto))                #오름차순으로 lotto(리스트)출력
# random.sample
#             ##방법2
# lotto = random.sample(range(1,45), 6)
# print(sorted(lotto))

                ###datetime 모듈
# import datetime

# now = datetime.datetime.today()

# print(now)
# print(now.month, now.day)
# print(f"{now.hour}시 {now.minute}분 {now.second}초")


# today= datetime.date.today()
# print(today)    #today.hour 안됨

import datetime

print("지금까지 몇 일?")
first_day = datetime.date(2024, 11, 25)
print(first_day)

today = datetime.date.today()
print(today)

passed_time = today - first_day
print(passed_time)

print(f"개강 이후 {passed_time.days}일 지났습니다.")

