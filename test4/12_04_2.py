            #set2 응용
#name = ["1","2","3","2"]
#a = []
#for i in range(len(name)):
#    if name.count(name[i])>1:
#        #print(name[i]) 
#        name.remove(name[i])
#        a.append(name[i])
#name_set = set(name)
#print(name_set)
#name_list = list(name_set)
#name_list.sort()
#print(name_list)

            #set 응용 문제 : for 루프 이용해 중복제거
name = ["1","2","3","2"]
a = []  
for i in range(len(name)): #a 기준으로 하나씩 없으면 넣고 있으면 패스
   if a.count(name[i]) < 1: ##
       a.append(name[i])
name = a
print(name)

# name = ["1","2","3","2"]
# a = []

# for i in name:
#     if i not in a:
#         a.append(i)
# print(a)