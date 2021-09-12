from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [int(input()) for _ in range(n)] + [0]
res = 0
stack = deque()
stack.append((0, graph[0]))
for i in range(1, n + 1):
    c = i
    while stack and stack[-1][1] > graph[i]:
        c, temp = stack.pop()
        res = max(res, temp * (i - c))
    stack.append((c, graph[i]))
print(res)