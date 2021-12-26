#15649
#https://www.acmicpc.net/problem/15649


from itertools import permutations


n , m = map(int,input().split())
answer =list(permutations(range(1,n+1),m))


for i in answer:
    for j in i:
        print(j ,end=' ')
    print()



