#15650
#https://www.acmicpc.net/problem/15650

from itertools import combinations

n , m = map(int,input().split())

combination = list(combinations(range(1,n+1),m))

for combi in combination:
    for c in range(m):
        print(combi[c],end=' ' )
    print()

data = range(1,n+1)
visit = [False]*(n+1)


def solution(select :list , m,idx):
    if m == 0:
        for i in select:
            print(i , end=' ')
        print()
        return


    for i in range(idx,n+1):
        visit[i] = True
        select.append(i)
        solution(select,m-1,i+1)
        select.remove(i)
        visit[i] = False

solution([],m,1)
