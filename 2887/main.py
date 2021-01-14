#2887
#https://www.acmicpc.net/problem/2887

import sys
import heapq
input =sys.stdin.readline
sys.setrecursionlimit(1000000)

def find_parent(parent ,x):
    if parent[x] !=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent ,a ,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b: parent[a] = b
    else : parent[b] = a


n = int(input())

edges =[]
x=[]
y=[]
z=[]

parent = [0]*(n+1)
for i in range(n+1): parent[i] = i

for i in range(1,n+1):
    a,b,c = map(int,input().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))
x.sort()
y.sort()
z.sort()

for i in range(n-1):
    edges.append((x[i+1][0]-x[i][0],x[i][1],x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0],y[i][1],y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0],z[i][1],z[i+1][1]))

answer = 0
edges.sort()

for edge in edges:
    cost ,now ,will = edge
    if find_parent(parent,now) != find_parent(parent,will):
        union_parent(parent,now,will)
        answer += cost

print(answer)
