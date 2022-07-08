#성적관리
STUDENT = 5
lst = [ ]
count = 0
for i in range(STUDENT):
    value = int(input("성적을 입력 "))
    lst.append(value)

    print ("\n성적 평균 = ", sum(lst)/len(lst))
    print("최대점수", max(lst))
    print("최소점수", min(lst))
