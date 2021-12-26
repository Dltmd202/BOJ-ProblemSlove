#10989
#https://www.acmicpc.net/problem/10989
#O(N)

import sys
input = sys.stdin.readline

count = [0] *10001

n = int(input())

for i in range(n):
    a = int(input())
    count[a] += 1

for b in range(len(count)):
    if count[b] !=0:
        for c in range(count[b]):
            print(b)

