#1715
#https://www.acmicpc.net/problem/1715

import heapq

n = int(input())

data = []

for i in range(n):
    heapq.heappush(data,int(input()))
sum = 0

while True:
    fir = heapq.heappop(data)
    if data:
        sec = heapq.heappop(data)
    else:
        break
    sum += (fir+sec)
    heapq.heappush(data,fir+sec)


print(sum)
