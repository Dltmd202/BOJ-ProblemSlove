

from collections import deque

n , m = map(int,input().split())
visit = [0]*(n+1)
graph =[[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


cnt =0
for i in range(1,n+1):
    if not visit[i]:
        cnt +=1
        visit[i] =cnt
        q = deque()
        q.append((i))

        while q:
            now =q.popleft()
            for will in graph[now]:
                if not visit[will]:
                    visit[will] = visit[now]
                    q.append(will)
print(cnt)