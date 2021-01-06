#2164
#https://www.acmicpc.net/problem/2164

from collections import deque

n =int(input())

q = deque()

for i in range(1,n+1):
    q.append(i)


while len(q) > 1:
    end = q.popleft()
    next = q.popleft()
    q.append(next)

print(q[0])