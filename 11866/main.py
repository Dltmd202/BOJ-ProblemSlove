#11866
#https://www.acmicpc.net/problem/11866

from collections import deque


n , k = map(int,input().split())

q =deque()
answer =[]
for i in range(1,n+1):
    q.append(i)

while q:
    for i in range(k-1):
        poped = q.popleft()
        q.append(poped)
    removeing = q.popleft()
    answer.append(removeing)

print('<',end='')
for i in range(len(answer)-1):
    print(answer[i],end=', ')

print("%d>"%answer[len(answer)-1])
