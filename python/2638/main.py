import sys
from collections import deque
input = sys.stdin.readline

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


class Solution:
    def __init__(self, answer=0):
        self.n, self.m = map(int, input().split())
        self.graph = [list(map(int, input().split())) for _ in range(self.n)]
        self.answer = answer
        self.cheese = [[0] * self.m for _ in range(self.n)]
        self.will_delete = []

    def bfs(self):
        q = deque()
        q.append([0, 0])
        visited = [[False] * self.m for _ in range(self.n)]
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < self.n and 0 <= nx < self.m:
                    if not visited[ny][nx]:
                        if self.graph[ny][nx] == 0:
                            visited[ny][nx] = True
                            q.append([ny, nx])
                        else:
                            self.cheese[ny][nx] += 1
                            if self.cheese[ny][nx] >= 2:
                                self.will_delete.append([ny, nx])

    def solution(self):
        while True:
            self.bfs()
            self.cheese = [[0] * self.m for _ in range(self.n)]
            if self.will_delete:
                while self.will_delete:
                    y, x = self.will_delete.pop()
                    self.graph[y][x] = 0
                self.answer += 1
            else:
                break
        return self.answer


if __name__ == '__main__':
    s = Solution()
    print(s.solution())
