from collections import deque
import sys
input = sys.stdin.readline

while True:
    n, *args = input().rstrip().split()
    n = int(n)
    if not n:
        break
    graph = list(map(int, args)) + [0]
    res = 0
    stack = deque()
    stack.append((0, graph[0]))
    for i in range(1, n + 1):
        cursor = i
        while stack and stack[-1][1] > graph[i]:
            cursor, height = stack.pop()
            res = max(res, height * (i - cursor))
        stack.append((cursor, graph[i]))
    print(res)