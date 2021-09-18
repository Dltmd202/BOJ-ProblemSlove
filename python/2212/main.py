import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
data = list(map(int, input().split()))
length = len(data)
dist = []
data.sort()
for i in range(len(data) - 1):
    dist.append(data[i + 1] - data[i])
dist.sort()

i = 0
while i < k - 1:
    if dist:
        dist.pop()
    i += 1

print(sum(dist))