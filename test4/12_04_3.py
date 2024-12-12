#             #dictionary
# a = {}
# print(type(a))
# b = {1} # set()
# print(type(b))  #딕셔너리는 key와 값으로 이뤄짐
# c = dict()
# c = {1:'a', 'b':'b'} #1=key 'a'=values
# print(c)
# #딕셔너리추가
# c[2] = 'c'     #2는 key
# c['c'] = 2     #key c 추가
# print(c)
# del c[2]    #c의 키 2 삭제
# del c['b']  #c의 키 b 삭제
# print(c)
# #print(c[2])    #2 위에서 2 지워서 에러
# print(c.get(2))  #없으면 none 으로 출력 있으면 출력
# print(c.keys())  #c의 모든키 출력
# print(c.values()) # c의 모든값 출력

# for i in c.keys():
#     print(i, c.get(i))

# # for i in c.values():
# #     print(i, c.value(i))

# print('c'in c)
# print(2 in c.values())

#               #딕셔너리 응용(try 대신 if/else사용)
dic = {
    "비트": "0이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위",
    "변수": "어떤 1개의 자료를 저장하기 위한 메모리 할당 공간",
    "리스트": "여러 개의 연속적인 자료를 저장하는 자료구조"
}


print("★ 컴퓨터 사전 ★")
word = input("검색할 단어를 입력하세요: ")
if word in dic : 
    print(f'{word}: {dic[word]}')
else:
    print("정의된 단어가 없습니다.")