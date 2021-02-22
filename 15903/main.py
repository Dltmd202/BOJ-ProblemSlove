import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
answer = 0
heapq.heapify(data)
for _ in range(m):
    first = heapq.heappop(data)
    seoncd = heapq.heappop(data)
    heapq.heappush(data, first + seoncd)
    heapq.heappush(data, first + seoncd)

print(sum(data))