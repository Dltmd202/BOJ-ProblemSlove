from collections import deque
n = int(input())
inputs = []
tree = [[] for _ in range(n + 1)]
parent = [-1] * (n + 1)
q = deque()

for i in range(n - 1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

parent[1] = 0
q.append(1)

while q:
    now = q.popleft()
    for chd in tree[now]:
        if parent[chd] == -1:
            parent[chd] = now
            q.append(chd)

print('\n'.join(str(c) for c in parent[2:]))