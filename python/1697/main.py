from collections import deque
MAX = 100000
n , k  = map(int,input().split())

distance = [-1] *(MAX+1)

q  =deque()
q.append(n)
distance[n] = 0

while q:
    now = q.popleft()
    if now == k:
        print(distance[k])
        break
    if 0<= now+1 <= MAX and distance[now+1] == -1:
        distance[now+1] = distance[now]+1
        q.append(now+1)
    if 0<= now-1 <= MAX and distance[now-1] == -1:
        distance[now-1] = distance[now]+1
        q.append(now-1)
    if 0<= now*2 <= MAX and distance[now*2] == -1:
        distance[now*2] = distance[now]+1
        q.append(now*2)