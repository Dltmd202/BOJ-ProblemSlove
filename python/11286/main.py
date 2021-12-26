from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
minq = []
for query in range(n):
    d = int(input())
    if d == 0:
        try:
            absolute, now = heappop(minq)
        except:
            now = 0
        print(now)
    else:
        heappush(minq, (abs(d), d))
