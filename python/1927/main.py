#1927
#O(N * log N)

import heapq
import sys
input =sys.stdin.readline

n = int(input())

q= []
answer =[]
for i in range(n):
    d = int(input())
    if d == 0 :
        if len(q):
            answer.append(heapq.heappop(q))
        else:
            answer.append(0)
    else:
        heapq.heappush(q,d)



for ans in answer:
    print(ans)