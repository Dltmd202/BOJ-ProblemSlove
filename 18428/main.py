#18428
#https://www.acmicpc.net/problem/18428
from collections import deque
from itertools import product,combinations

n = int(input())

graph = []

dy = [0,-1,0,1]
dx = [1,0,-1,0]

for i in range(n):
    data = input().split()
    d =[]
    for j in range(n):
        if data[j] == 'X':
            d.append(0)
        elif data[j] == 'S':
            d.append(1)
        elif data[j] == 'T':
            d.append(2)
        elif data[j] == 'O':
            d.append(3)
    graph.append(d)




def search(y,x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0 <= ny < n and 0<= nx < n) :
            while True:
                if 0 <= nx and nx < n and 0<= ny and ny < n:
                    if graph[ny][nx] == 1:
                        return False
                    elif graph[ny][nx] == 3:
                        break
                else :
                    break
                ny = ny + dy[i]
                nx = nx + dx[i]
    return True



def solution():
    for combi in combinations(product(range(n),repeat=2),3):
        result = True
        for j in combi:
            y,x = j
            if graph[y][x] != 0:
                result = False
                continue
            graph[y][x] = 3

        for i in range(n):
            for j in range(n):
                if graph[i][j] == 2:
                    if not search(i,j):
                        result = False

        if result == True:
            print("YES")
            return

        for j in combi:
            y, x = j
            if graph[y][x] == 3:
                graph[y][x] = 0
    print("NO")
    return


solution()

