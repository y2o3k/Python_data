#리스트 추가 방법에 따른 시간 테스트

import time
size = 50000
start_time = time.time()
myList = []
for i in range(size):
    myList = myList + [i*i] #대입은 재설정
print("수행시간=",time.time()-start_time)


start_time = time.time()
myList = []
for i in range(size):
    myList.append(i*i) # 단순히 추가
print("수행시간=",time.time()-start_time)