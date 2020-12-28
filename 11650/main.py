#11650
#https://www.acmicpc.net/problem/11650

n = int(input())

data = []

for i in range(n):
    y,x = map(int,input().split())
    data.append((y,x))


data.sort()

for i in data:
    y,x = i
    print(y,x)