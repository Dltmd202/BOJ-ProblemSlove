#15650
#https://www.acmicpc.net/problem/15650

from itertools import combinations

n , m = map(int,input().split())

combination = list(combinations(range(1,n+1),m))

for combi in combination:
    for c in range(m):
        print(combi[c],end=' ' )
    print()

