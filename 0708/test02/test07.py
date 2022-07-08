#튜플 / 딕셔너리 / 세트

#튜플 - 변경 불가- ()
fruits = ("apple", "banana","grape")
print(fruits)
print(fruits[0])
for f in fruits:
    print(f, end=" ")

#튜플을 리스트로
print()
myTuple=(1,2,3,4)
myList = list(myTuple)
print()
print(myList)
#딕셔너리 - key/ value -{}

#세트 - 중복불가 - {}
print()
numbers = {1,2,3}
print("set=",numbers)

number = set([1,2,2,3,3,4,5])
print("set",numbers)

#세트 함축 연산
print()
aList = [1,2,3,4,5,1,2]
result = {x for x in aList if x % 2 ==0}
print("x=%2", result)

# 세트 - 교집합 / 합집합 / 차집합
print()
A = {"apple","banana","grape"}
B = {"apple","banana","watermelon"}
C = A&B
D = A|B
E = A-B

print("교집합",C)
print("합집합",D)
print("차집합",E)

