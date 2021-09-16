import sys
input = sys.stdin.readline


def init(start, end, node):
    if start == end:
        tree[node] = data[start]
    else:
        mid = (start + end) // 2
        init(start, mid, node * 2)
        init(mid + 1, end, node * 2 + 1)
        tree[node] = tree[node * 2] ^ tree[node * 2 + 1]


def update_lazy(start, end, node):
    if lazy[node] != 0:
        tree[node] ^= lazy[node] if (start - end + 1) % 2 else 0
        if start != end:
            lazy[node * 2] ^= lazy[node]
            lazy[node * 2 + 1] ^= lazy[node]
        lazy[node] = 0


def update(start, end, node, left, right, val):
    update_lazy(start, end, node)
    if right < start or end < left:
        return
    if left <= start and end <= right:
        tree[node] ^= val if (start - end + 1) % 2 else 0
        if start != end:
            lazy[node * 2] ^= val
            lazy[node * 2 + 1] ^= val
        return

    mid = (start + end) // 2
    update(start, mid, node * 2, left, right, val)
    update(mid + 1, end, node * 2 + 1, left, right, val)
    tree[node] = tree[node * 2] ^ tree[node * 2 + 1]


def query(start, end, node, left, right):
    update_lazy(start, end, node)
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query(start, mid, node * 2, left, right) ^ query(mid + 1, end, node * 2 + 1, left, right)


if __name__ == '__main__':
    n = int(input())
    ans = []
    tree = [0] * (n * 4)
    lazy = [0] * (n * 4)
    data = list(map(int, input().split()))
    init(0, n - 1, 1)
    for _ in range(int(input())):
        order, *args = map(int, input().split())
        if order == 1:
            update(0, n - 1, 1, args[0], args[1], args[2])
        elif order == 2:
            ans.append(query(0, n - 1, 1, args[0], args[1]))

    print('\n'.join(str(a) for a in ans))