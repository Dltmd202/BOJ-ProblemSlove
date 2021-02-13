import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
j = []
answer = 0
for i in range(n):
    m, v = map(int, input().split())
    heapq.heappush(j, (m, v))

bag = []
for i in range(k):
    heapq.heappush(bag, int(input()))

able_gem = []
for _ in range(k):
    now = heapq.heappop(bag)
    while j and now >= j[0][0]:
        m, v = heapq.heappop(j)
        heapq.heappush(able_gem, -v)

    if able_gem:
        answer -= heapq.heappop(able_gem)

print(answer)