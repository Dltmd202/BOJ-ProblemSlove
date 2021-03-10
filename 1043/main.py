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


n, m = map(int, input().split())
data = list(map(int, input().split()))
c, truth = data[0], data[1:]
party = []
parents = [i for i in range(n + 1)]
for i in range(m):
    data = list(map(int, input().split()))
    party.append(data[1:])
    for j in range(1, len(data) - 1):
        if find_parent(parents, data[j]) != find_parent(parents, data[j + 1]):
            union_parent(parents, data[j], data[j + 1])

truth_parents = set()
for i in truth:
    truth_parents.add(find_parent(parents, i))

cnt = 0
for i in range(m):
    result = True
    for member in party[i]:
        if find_parent(parents, member) in truth_parents:
            result = False
    if result:
        cnt += 1

print(cnt)