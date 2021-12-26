import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(int, input().split()))
prefix = [0]
sum = 0
for i in range(n):
    sum += data[i]
    prefix.append(sum)

for i in range(m):
    a, b = map(int, input().split())
    print(prefix[b] - prefix[a - 1])