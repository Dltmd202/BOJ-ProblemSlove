#15652
#https://www.acmicpc.net/problem/15652]

from itertools import combinations_with_replacement

n , m = map(int,input().split())

combination = combinations_with_replacement(range(1,n+1),m)

for i in combination:
    for j in i:
        print(j,end=' ')
    print()