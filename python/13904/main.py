import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
max_deadline = 0
for i in range(n):
    max_deadline = max(max_deadline, data[i][0])
parent = [i for i in range(max_deadline + 1)]
data.sort(key=lambda x: x[1])
answer = 0

while data:
    deadline, score = data.pop()
    match_dead = find_parent(parent, deadline)
    if match_dead:
        answer += score
        union_parent(parent, match_dead, match_dead - 1)

print(answer)