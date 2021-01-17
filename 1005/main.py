#1005
#https://www.acmicpc.net/problem/1005

from collections import deque


import sys
input = sys.stdin.readline


for tb in range(int(input())):
    n ,k =map(int,input().split())
    d = list(map(int,input().split()))
    d=[0]+d
    graph =[[] for _ in range(n+1)]
    indegree = [0]*(n+1)
    cost =[0]*(n+1)
    q= []

    for i in range(k):
        a, b = map(int,input().split())
        graph[a].append(b)
        indegree[b] +=1
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
            cost[i]=d[i]
    w=int(input())

    while q:
        now = q.pop()
        for will in graph[now]:
            indegree[will] -=1
            cost[will] = max(cost[will],cost[now])
            if indegree[will] == 0:
                cost[will] = max(cost[will],cost[now])+d[will]
                q.append(will)

    print(cost[w])


