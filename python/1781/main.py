import sys
import heapq
input = sys.stdin.readline
n = int(input())
prob = [list(map(int, input().split())) for _ in range(n)]
prob.sort()
answer = []

for p, re in prob:
    heapq.heappush(answer, re)
    if len(answer) > p:
        heapq.heappop(answer)

print(sum(answer))