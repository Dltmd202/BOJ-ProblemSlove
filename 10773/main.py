#10773
#https://www.acmicpc.net/problem/10773
#O(K)

from collections import deque

import sys
input = sys.stdin.readline


k = int(input())
q = deque()

for i in range(k):
    buf = int(input())
    if buf == 0:
        q.pop()
    else :
        q.append(buf)

result = sum(list(q))

print(result)
