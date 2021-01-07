#2581
#https://www.acmicpc.net/problem/2581

import math

m = int(input())
n = int(input())

table =[0]*(n+1)
table[0] = True
table[1] = True
for i in range(2,n+1):
    cnt = 2
    while i * cnt <= n :
        table[i*cnt] = True
        cnt += 1
sum = 0
min = -1
for i in range(m,n+1):
    if table[i] == False:
        sum += i
        if min == -1:
            min = i
if min == -1 :
    print(-1)
else:
    print(sum)
    print(min)

