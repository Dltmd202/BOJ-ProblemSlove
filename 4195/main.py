import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b, cnt):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a != b:
        parent[b] = a
        cnt[a] += cnt[b]


for tb in range(int(input())):
    f = int(input())
    parents = {}
    cnt = {}
    for _ in range(f):
        friend1, friend2 = input().strip().split()

        if friend1 not in parents:
            parents[friend1] = friend1
            cnt[friend1] = 1

        if friend2 not in parents:
            parents[friend2] = friend2
            cnt[friend2] = 1

        union_parent(parents, friend1, friend2, cnt)
        print(cnt[find_parent(parents, friend1)])
