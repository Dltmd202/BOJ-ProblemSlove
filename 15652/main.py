#15652
#https://www.acmicpc.net/problem/15652]

from itertools import combinations_with_replacement

n , m = map(int,input().split())

combination = combinations_with_replacement(range(1,n+1),m)

for i in combination:
    for j in i:
        print(j,end=' ')
    print()


data = range(1,n+1)
visit = [False]*(n+1)

def solution(select : list , m , idx):
    if m == 0 :
        for i in select:
            print(i ,end=' ')
        print()
        return

    for i in range(idx,n+1):
        visit[i] = True
        select.append(i)
        solution(select,m-1,i)
        visit[i] =False
        select.pop()


solution([],m,1)