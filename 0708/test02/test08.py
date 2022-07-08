#딕셔너리
capitals = {"Korea": "Seoul","USA":"Washington","Uk":"London"}
print(capitals["USA"])
print(capitals["Uk"])
for key in capitals: # 키 출력
    print(key, end = " ")

    print()

for key in capitals: # 값 출력
    print(capitals[key], end =" ")

    print()

for key in capitals: # 키/값 출력
    print(key,":", capitals[key],end =" , ")

    print()

    #딕셔너리 함축
    values = [1,2,3,4,5,6]
    dic = {x:x**2 for x in values if x%2 == 0}
    print(dic)