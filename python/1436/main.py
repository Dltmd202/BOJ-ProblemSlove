#1436
#https://www.acmicpc.net/status?user_id=bat5273&problem_id=1436&from_mine=1
#O(target)

import time
# start = time.time()
n = int(input())

cnt = 0
target = 666

while True :
    if '666' in str(target):
        cnt += 1
    if cnt == n:
        print(target)
        # end = time.time()
        break
    target += 1


# print(end-start)