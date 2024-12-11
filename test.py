            ##test10 - 12_11_5.py
            ##bbb, modules 폴더
from modules.mylib import food


print(food.name)
food.cook()
food.eat()

from modules.mylib.food import cook, eat, name
print(name)
cook()
eat()

# import bbb
# print(bbb.cm2.add(1,2))

import bbb.cm2                  #bbb폴더의 cm2 파일 가져오기
print(bbb.cm2.add(1,2))         #cm2파일에 설정된 add함수 출력

import bbb.cm2 as bc            #bbb bc로 변경
print(bc.add(1,2))
