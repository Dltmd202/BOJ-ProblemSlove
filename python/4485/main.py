import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
answer = []
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

while True:
    n = int(input())
    if not n:
        break
    graph = [list(map(int,input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = graph[0][0]
    q = []
    heapq.heappush(q, (distance[0][0], 0, 0))

    while q:
        dist, y, x = heapq.heappop(q)
        if dist > distance[y][x]:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if distance[ny][nx] > dist + graph[ny][nx]:
                    distance[ny][nx] = dist + graph[ny][nx]
                    heapq.heappush(q, (distance[ny][nx], ny, nx))
    answer.append(distance[-1][-1])


for i, ans in enumerate(answer):
    print(f'Problem {i + 1}: {ans}')
