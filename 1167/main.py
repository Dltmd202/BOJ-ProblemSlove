from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
ind = [0] * (n + 1)
visit = [False] * (n + 1)
res = 0
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(1, len(line) - 1, 2):
        graph[line[0]].append([line[j + 1], line[j]])
        graph[line[j]].append([line[j + 1], line[0]])


def search(start):
    global res
    visit[start] = True
    left, right = 0, 0
    for c, will in graph[start]:
        depth = 0
        if not visit[will]:
            depth = search(will)
            if depth + c > left:
                right = left
                left = depth + c
            elif depth + c > right:
                right = depth + c
    res = max(res, left + right)
    return max(left, right)


search(1)
print(res)