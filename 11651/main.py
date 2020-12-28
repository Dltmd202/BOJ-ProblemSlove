#11651
#https://www.acmicpc.net/problem/11651

n = int(input())

data = []

for i in range(n):
    y,x = map(int,input().split())
    data.append((y,x))




data.sort(key = lambda x :(x[1],x[0]))


for i in data:
    y,x = i
    print(y,x)
