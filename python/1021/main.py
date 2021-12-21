from collections import deque
n, m = map(int, input().split())
data = list(map(int, input().split()))[::-1]
cnt = 0

q = deque()
for i in range(1, n + 1):
    q.append(i)

while data:
    n = data.pop()
    idx = q.index(n)
    if idx != 0:
        if idx - 1 < len(q) - idx:
            for i in range(idx):
                q.append(q.popleft())
            cnt += idx
        else:
            for i in range(len(q) - idx):
                q.appendleft(q.pop())
            cnt += (len(q) - idx)
    q.popleft()
print(cnt)
