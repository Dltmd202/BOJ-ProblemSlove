import sys
import math
ans = list()
res = list()


def permutations(depth: int):
    global m, n
    if depth == m:
        s = ' '.join(map(str, res))
        if s not in ans:
            ans.append(s)
        return
    for i in range(n):
        if not visited[i]:
            res.append(data[i])
            visited[i] = True
            permutations(depth + 1)
            res.pop()
            visited[i] = False


n, m = map(int, input().split())
visited = [False] * n
data = list(map(int, input().split()))
data.sort()
permutations(0)
for s in ans:
    print(s)
