import heapq
import math
from itertools import combinations

n = int(input())
init = []
for i in range(n):
    init.append(input())

alpha = [0] * 27

cnt = 0
for i in init:
    cnt = 0
    for j in range(len(i) - 1, -1, -1):
        alpha[ord(i[j]) - ord('A')] += int(10 ** cnt)
        cnt += 1

answer = 0
alpha.sort(reverse=True)
for i in range(9, -1, -1):
    answer += i * alpha[0]
    alpha = alpha[1:]

print(answer)