import heapq
from collections import deque

n, c = map(int, input().split())
m = int(input())
data = [list(map(int, input().split())) for _ in range(m)]
data.sort(key=lambda x: x[1])
capacity =[c] * (n + 1)
q = deque()
stack = deque()
data = deque(data)
answer = 0

while data:
    will, now, box = data.popleft()
    for j in range(will, now):
        box = min(box, capacity[j])
    for j in range(will, now):
        capacity[j] -= box
    answer += box

print(answer)
