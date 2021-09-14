import sys
input = sys.stdin.readline


def query(start, end, node, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    left_ = query(start, mid, node * 2, left, right)
    right_ = query(mid + 1, end, node * 2 + 1, left, right)
    return left_ + right_


def update(start, end, node, idx, val):
    if idx < start or end < idx:
        return tree[node]
    if start == end:
        tree[node] = val
        return tree[node]
    mid = (start + end) // 2
    left_ = update(start, mid, node * 2, idx, val)
    right_ = update(mid + 1, end, node * 2 + 1, idx, val)
    tree[node] = (left_ + right_)
    return left_ + right_


n, m = map(int, input().split())
tree = [0] * (n * 4)
ans = []
for i in range(m):
    order, *args = map(int, input().split())
    if order == 0:
        ans.append(query(1, n, 1, min(args), max(args)))
    elif order == 1:
        update(1, n, 1, args[0], args[1])

print('\n'.join(str(r) for r in ans))