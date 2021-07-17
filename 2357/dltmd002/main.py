import sys
input = sys.stdin.readline
from math import *

n, m = map(int, input().split())
h = int(ceil(log2(n))) + 1
size = (1 << h)
tree_max = [0] * size
tree_min = [inf] * size
init_max = [0] * (1 << (h - 1))
init_min = [inf] * (1 << (h - 1))

for i in range(n):
    c = int(input())
    init_min[i] = c
    init_max[i] = c


def min_init(node, start, end):
    if start == end:
        tree_min[node] = init_min[start]
        return tree_min[node]
    mid = (start + end) // 2
    tree_min[node] = min(min_init(node * 2, start, mid), min_init(node * 2 + 1, mid + 1, end))
    return tree_min[node]


def max_init(node, start, end):
    if start == end:
        tree_max[node] = init_max[start]
        return tree_max[node]
    mid = (start + end) // 2
    tree_max[node] = max(max_init(node * 2, start, mid), max_init(node * 2 + 1, mid + 1, end))
    return tree_max[node]


def min_query(node, start, end, left, right):
    if start > right or end < left:
        return inf

    if left <= start and end <= right:
        return tree_min[node]
    mid = (start + end) // 2
    return min(min_query(node * 2, start, mid, left, right), min_query(node * 2 + 1, mid + 1, end, left, right))


def max_query(node, start, end, left, right):
    if start > right or end < left:
        return 0
    if left <= start and end <= right:
        return tree_max[node]
    mid = (start + end) // 2
    return max(max_query(node * 2, start, mid, left, right), max_query(node * 2 + 1, mid + 1, end, left, right))


min_init(1, 0, (1 << (h - 1)) - 1)
max_init(1, 0, (1 << (h - 1)) - 1)

for i in range(m):
    a, b = map(int, input().split())
    print(min_query(1, 0, ((1 << (h - 1)) - 1), a - 1, b - 1), end=' ')
    print(max_query(1, 0, ((1 << (h - 1)) - 1), a - 1, b - 1))
