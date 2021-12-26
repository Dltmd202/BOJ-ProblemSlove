#11279
#https://www.acmicpc.net/problem/11279

import heapq
import sys
input = sys.stdin.readline

n = int(input())

q =[]
answer = []
for i in range(n):
    data  = int(input())
    heapq.heappush(q,-data)
    if data == 0:
        if len(q) == 0:
            answer.append(0)
        else:
            answer.append(-heapq.heappop(q))

for ans in answer:
    print(ans)
