#슬라이스 응용
lst = [1,2,3,4,5,6,7,8]
lst[0:3]= ['white','black','grey']
print(lst)

lst = [1,2,3,4,5,6,7,8]
lst[::2]= [99,99,99,99]
print(lst)

lst= [1,2,3,4,5,6,7,8]
lst[:]= [ ]
print(lst)

#출력식 : 입력 리스트
squares= [ x * x for x in range(10)]
print("=>>",squares)

#출력식:입력리스트:조건식
squares= [ x * x for x in range(10) if x %2 == 0]
print("%2=>>",squares)