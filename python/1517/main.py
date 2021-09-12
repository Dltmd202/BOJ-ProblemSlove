import sys
input = sys.stdin.readline


def update(idx, d):
    while idx <= n:
        tree[idx] += d
        idx += (idx & -idx)


def query(start, end):
    if end < start:
        return 0
    res = 0
    idx = end
    s_, e_ = 0, 0
    while idx > 0:
        e_ += tree[idx]
        idx -= (idx & -idx)
    idx = start - 1
    while idx > 0:
        s_ += tree[idx]
        idx -= (idx & -idx)
    return e_ - s_


def convert(origin):
    sorted_ = sorted(origin)
    indexed = dict().fromkeys(sorted_, 0)
    res = []
    visited = [False] * (len(origin) + 1)
    for i, temp in enumerate(indexed):
        indexed[temp] = i + 1
    for i in origin:
        if not visited[indexed[i]]:
            res.append(indexed[i])
            visited[indexed[i]] = True
    return res


n = int(input())
origin = list(map(int, input().split()))
converted = convert(origin)
tree = [0] * (n + 1)
ans = 0
for i in range(len(converted)):
    ans += (query(converted[i], len(converted)))
    print("ans ", ans)
    update(converted[i], 1)
print(ans)