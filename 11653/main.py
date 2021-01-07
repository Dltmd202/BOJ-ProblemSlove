#11653
#https://www.acmicpc.net/status?from_mine=1&problem_id=11653&user_id=bat5273

import math

n = int(input())

table = [0]*(n+1)
table[0] = -1
table[1] = -1
new_n = n
for i in range(2,n+1):
    cnt = 1
    while i *cnt <= new_n:
        if table[cnt*i] != -1 and cnt == 1:
            while new_n % i == 0 and new_n > 1:
                new_n /= i
                table[i] += 1
        else:
            table[cnt*i] = -1
        cnt += 1



for i in range(n+1):
    if table[i] >= 1:
        for j in range(table[i]):
            print(i)