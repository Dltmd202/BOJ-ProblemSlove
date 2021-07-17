import sys
from math import *
input = sys.stdin.readline
n, m, k = map(int, input().split())
h = ceil(log2(n)) + 1
data = [1] * (n + 1)
tree = [1] * (1 << h)


def update(node, start, end, idx, val):
    if start > idx or idx > end:
        return
    if start == end:
        tree[node] = val
        return
    mid = (start + end) // 2
    update(node * 2, start, mid, idx, val)
    update(node * 2 + 1, mid + 1, end, idx, val)
    tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % 1000000007


def query(node, start, end, left, right):
    if start > right or left > end:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return (query(node * 2, start, mid, left, right) * query(node * 2 + 1, mid + 1, end, left, right)) % 1000000007


for i in range(n):
    x = int(input())
    update(1, 0, (1 << (h - 1)) - 1, i, x)

for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 0, (1 << (h - 1)) - 1, b - 1, c)
    elif a == 2:
        print(query(1, 0, (1 << (h - 1)) - 1, b - 1, c - 1))
