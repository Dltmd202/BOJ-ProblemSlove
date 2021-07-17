from collections import defaultdict, deque
import heapq
n = input()
data, n = list(map(int, n)), int(n)
m = int(input())
remote = {str(i) for i in range(10)}

if m > 0:
    remote -= set(map(str, input().split()))

current = 100
min_val = abs(current - n)

for i in range(int(1e6)):
    ch = str(i)
    for j in range(len(ch)):
        if ch[j] not in remote:
            break
        if len(ch) - 1 == j:
            min_val = min(min_val, abs(i - n) + len(ch))

print(min_val)



