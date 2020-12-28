#10814
#https://www.acmicpc.net/problem/10814

import sys
input = sys.stdin.readline
n = int(input())

data = []

for i in range(n):
    d = input().rstrip().split()
    data.append((int(d[0]),d[1],i+1))

data.sort(key=lambda x:(x[0],x[2]))


for i in data:
    age , name ,idx = i
    print(age,name)
