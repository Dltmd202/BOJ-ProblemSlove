import sys
from collections import deque
input = sys.stdin.readline
MAX = 100001


n, k = map(int, input().split())
visit = [-1] * (MAX)
q = deque()
visit[n] = 0
q.append(n)

while q:
    now = q.popleft()
    if 0 <= now * 2 < MAX and visit[now * 2] == -1:
        visit[now * 2] = visit[now]
        q.append(now * 2)
    if 0 <= now - 1 < MAX and visit[now - 1] == -1:
        visit[now - 1] = visit[now] + 1
        q.append(now - 1)
    if 0 <= now + 1 < MAX and visit[now + 1] == -1:
        visit[now + 1] = visit[now] + 1
        q.append(now + 1)
    if visit[k] != -1:
        print(visit[k])
        break

