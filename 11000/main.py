import sys
import heapq
input = sys.stdin.readline
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort(key=lambda x: x[0])

q = []
heapq.heappush(q, data[0][1])

for i in range(1, n):
    if q[0] > data[i][0]:
        heapq.heappush(q, data[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q, data[i][1])

print(len(q))