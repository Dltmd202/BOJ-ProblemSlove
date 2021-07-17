import sys
input = sys.stdin.readline
from math import *

n, m = map(int, input().split())
h = ceil(log2(n)) + 1
size = (1 << h)
tree = [inf] * size
init = [inf] * (1 << (h - 1))

for i in range(n):
    init[i] = int(input())


def init_tree(node, start, end):
    if start == end:
        tree[node] = init[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = min(init_tree(node * 2, start, mid), init_tree(node * 2 + 1, mid + 1, end))
    return tree[node]


def query(node, start, end, left, right):
    if start > right or left > end:
        return inf
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return min(query(node * 2, start, mid, left, right), query(node * 2 + 1, mid + 1, end, left, right))



init_tree(1, 0, (1 << (h - 1)) - 1)
for i in range(m):
    a, b = map(int, input().split())
    print(query(1, 0, (1 << (h - 1)) - 1, a - 1, b - 1))
