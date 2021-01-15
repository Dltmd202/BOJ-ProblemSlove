#1996
#https://www.acmicpc.net/problem/1996

from collections import deque
t = int(input())

answer = []
def solution():

    n , m = map(int,input().split())
    data = list(map(int,input().split()))

    q = deque()
    for i in range(n):
        q.append((data[i],i))

    target = data[m]

    data.sort(reverse=True)

    # print()
    cnt = 1
    max_idx = 0
    while q:
        # print(q)
        # print(data)
        cost , now = q.popleft()
        # print(data,max_idx)
        # print(data[max_idx])
        if data[max_idx] == cost:
            # print(m,now)
            if m == now:
                return cnt
            cnt +=1
            max_idx+=1

        else:
            if data[0] in q:
                q.append((cost,now))
            else:
                q.append((cost,now))



for i in range(t):
    answer.append(solution())

for i in answer:
    print(i)