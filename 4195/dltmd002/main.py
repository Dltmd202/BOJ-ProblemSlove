from collections import defaultdict
import sys
input = sys.stdin.readline
tb = int(input())

for t in range(tb):
    n = int(input())
    parent = defaultdict(str)
    number = defaultdict(int)
    names = set()
    edges = []


    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]


    def union(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            parent[a] = b
            number[b] += number[a]

    for i in range(n):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1

        union(a, b)
        print(number[find(a)])
