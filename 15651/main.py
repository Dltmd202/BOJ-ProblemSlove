#15651
#https://www.acmicpc.net/problem/15651

from itertools import product

n , m = map(int,input().split())


for p in product((range(1,n+1)),repeat=m):
    for i in p:
        print(i ,end=' ')
    print()


data = range(1,n+1)
visit = [False]*(n+1)

def solution(select : list , m):
    if m == 0:
        for i in select:
            print(i,end=' ' )
        print()
        return

    for i in range(1,n+1):
        visit[i] = True
        select.append(i)
        solution(select,m-1)
        visit[i] = False
        select.pop()

solution([],m)