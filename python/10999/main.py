import sys
input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = data[start]
    else:
        mid = (start + end) // 2
        init(start, mid, node * 2)
        init(mid + 1, end, node * 2 + 1)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


def update_lazy(node, start, end):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0


def update(start, end, node, left, right, diff):
    update_lazy(node, start, end)
    if end < left or right < start:
        return
    if left <= start and end <= right:
        tree[node] += (end - start + 1) * diff
        if start != end:
            lazy[node * 2] += diff
            lazy[node * 2 + 1] += diff
        return

    mid = (start + end) // 2
    update(start, mid, node * 2, left, right, diff)
    update(mid + 1, end, node * 2 + 1, left, right, diff)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(start, end, node, left, right):
    update_lazy(node, start, end)
    if end < left or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query(start, mid, node * 2, left, right) + query(mid + 1, end, node * 2 + 1, left, right)


n, m, k = map(int, input().split())
data = [0] + [int(input()) for _ in range(n)]
ans = []
tree = [0] * (n * 4)
lazy = [0] * (n * 4)

init(1, n, 1)

for _ in range(m + k):
    order, *args = map(int, input().split())
    if order == 1:
        update(1, n, 1, args[0], args[1], args[2])
    elif order == 2:
        ans.append(query(1, n, 1, args[0], args[1]))

print('\n'.join(str(a) for a in ans))