#15651
#https://www.acmicpc.net/problem/15651

from itertools import product

n , m = map(int,input().split())


for p in product((range(1,n+1)),repeat=m):
    for i in p:
        print(i ,end=' ')
    print()

