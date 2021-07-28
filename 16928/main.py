from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
ladders = dict()
snakes = dict()
for i in range(n):
    now, will = map(int, input().split())
    ladders[now] = will

for i in range(m):
    now, will = map(int, input().split())
    snakes[now] = will


visit = [int(1e9)] * 101

q = deque()
q.append([0, 1])

while q:
    cnt, now = q.popleft()
    if now == 100:
        print(cnt)
        break
    for i in range(1, 7):
        if now + i in snakes:
            if visit[snakes[now + i]] > cnt + 1:
                visit[snakes[now + i]] = cnt + 1
                q.append([cnt + 1, snakes[now + i]])
        elif now + i in ladders:
            if visit[ladders[now + i]] > cnt + 1:
                visit[ladders[now + i]] = cnt + 1
                q.append([cnt + 1, ladders[now + i]])
        elif now + i <= 100 and visit[now + i] > cnt + 1:
            visit[now + i] = cnt + 1
            q.append([cnt + 1, now + i])
