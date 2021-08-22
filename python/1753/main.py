#1753
#https://www.acmicpc.net/problem/1753

import sys
from heapq import heappush ,heappop

inf = int(1e9)
v ,e = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[]for _ in range(v+1)]
dp = [inf] * (v+1)
heap= []

def dijkstra(start):
    dp[start]=0
    heappush(heap,[0,start])
    while heap:
        dist , now =  heappop(heap)

        if dp[now] < dist:
            continue

        for cos,will in graph[now]:
            cost = dist + cos
            if dp[will] > cost:
                dp[will] = cost
                heappush(heap,[cost,will])

for i in range(e):
    a , b, c = map(int,sys.stdin.readline().split())
    graph[a].append([c,b])


dijkstra(start)

for i in dp[1:]:
    print(i if i != inf else "INF")