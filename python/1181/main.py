#1181
#https://www.acmicpc.net/problem/1181

import sys
input = sys.stdin.readline
n = int(input())

data = []

for i in range(n):
    d = input().rstrip()
    if d in data:
        continue
    data.append(d)

data.sort(key=lambda x: (len(x),x))


for i in data:
    print(i)
