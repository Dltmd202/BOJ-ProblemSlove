#1197
#https://www.acmicpc.net/problem/1197
#O(E log E)

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent ,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a > b: parent[a] = b
    else:parent[b] =a

v ,e = map(int,input().split())

edges =[]

for i in range(e):
    a ,b , cost = map(int,input().split())
    edges.append((cost,a,b))


edges.sort()

parent =[0]*(v+1)
for i in range(1,v+1): parent[i] = i

answer = 0
for edge in edges:
    cost , x, y = edge
    if find_parent(parent,x) != find_parent(parent,y):
        union_parent(parent,x,y)
        answer += cost


print(answer)

'''
3 3
1 2 -1
2 3 2
1 3 3
'''