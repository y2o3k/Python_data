#슬라이싱 - 한번에 여러개의 항목을 추출하는 기법

numbers = [10, 20, 30 , 40, 50, 60, 70, 80, 90]
sublist = numbers[2:7]
print(sublist)
prelist = numbers[:3]
print(prelist)
postlist=numbers[3:]
print(postlist)
alllist = numbers[:]
print(alllist)

numbers[::-1]
print("리스트-1 : ",numbers)