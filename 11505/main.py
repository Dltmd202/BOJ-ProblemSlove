

import sys
input = sys.stdin.readline
DIV = 1000000007

n , m , k = map(int,input().split())

data = [0] * (n+1)
tree = [1] * (n+1)

def prefix_mul(x):
    result = 1
    while x > 0:
        result =(result* tree[x])%DIV
        x -= (x & -x)
    return result

def update(i , dif):
    while i <= n:
        if(tree[i]==0):
            tree[i] = 1
        tree[i] = (tree[i] *dif) %DIV
        i += (i & -i)

def interval_mul(start,end):
    return int(prefix_mul(end) / prefix_mul(start-1)) % DIV

for i in range(1,n+1):
    x= int(input())
    data[i]=x
    update(i,x)




for i in range(m+k):
    a ,b ,c =map(int,input().split())
    print(tree[1:])
    if a == 1:
        if data[b] == 0:
            data[b] = c
            update(b ,c)
        else:
            update(b , (c/ data[b]))
        data[b] =c
    else:
        print(interval_mul(b,c))