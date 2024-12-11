            ###캘린더 모듈
import calendar
# calendar.prcal(2024)
# calendar.prmonth(2024,12)
# print(calendar.weekday(2024,12,11)) ##0=mon 1=tue 2=wed ~6sun

import datetime

days = ['월', '화', '수','목','금','토','일']
weekday = datetime.date.today().weekday()
print(f"오늘은 {days[weekday]}요일")

def getWeekday(yyyy, mm, dd):
    days = ['월', '화', '수','목','금','토','일']
    weekday = datetime.date(yyyy,mm,dd).weekday()
    print
getWeekday(2024, 12, 11)





weekday = datetime.date(2025, 12, 25).weekday()
print(f"크리스마스는 {days[weekday]}요일")