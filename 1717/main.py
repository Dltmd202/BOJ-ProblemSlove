#1717
#https://www.acmicpc.net/problem/1717


def find_parent(parent ,x):
    if parent[x]!=x:
        parent[x] =find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a > b: parent[a]=b
    else : parent[b] =a

n ,m =map(int,input().split())
parent =[0]*(n+1)
answer = []
for i in range(1,n+1):parent[i] = i
for i in range(m):
    calc ,a ,b = map(int,input().split())
    if calc == 0:
        union_parent(parent,a,b)
    if calc == 1 :
        if find_parent(parent,a) == find_parent(parent,b):
            answer.append("YES")
        else:
            answer.append("NO")

for ans in answer:
    print(ans)