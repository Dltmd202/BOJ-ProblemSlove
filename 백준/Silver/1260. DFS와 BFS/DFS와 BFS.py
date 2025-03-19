from collections import deque
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for g in graph:
        g.sort()

    def dfs(start, answer, visited):
        answer.append(start)
        visited[start] = True

        for next in graph[start]:
            if not visited[next]:
                dfs(next, answer, visited)

    def bfs(start, answer, visited):
        q = deque([start])
        visited[start] = True
        answer.append(start)

        while q:
            cur = q.popleft()

            for next in graph[cur]:
                if not visited[next]:
                    visited[next] = True
                    q.append(next)
                    answer.append(next)


    answer1 = []
    answer2 = []
    dfs(v, answer1, [False] * (n + 1))
    bfs(v, answer2, [False] * (n + 1))
    print(' '.join(map(str, answer1)))
    print(' '.join(map(str, answer2)))