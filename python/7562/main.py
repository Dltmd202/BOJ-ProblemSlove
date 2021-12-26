from collections import deque
import sys
input = sys.stdin.readline
tb = int(input())
inf = int(1e9)

for t in range(tb):
    n = int(input())
    night = list(map(int, input().split()))
    dest = list(map(int, input().split()))
    visited = [[inf] * (n + 1) for _ in range(n + 1)]
    dy = [1, 2, -1, -2, 1, 2, -1, -2]
    dx = [2, 1, 2, 1, -2, -1, -2, -1]
    q = deque()
    q.append(night)
    visited[night[0]][night[1]] = 0

    while q:
        y, x = q.popleft()
        if y == dest[0] and x == dest[1]:
            print(visited[y][x])
            break
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[ny][nx] > visited[y][x] + 1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny, nx])
