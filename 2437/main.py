
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
i = 0
while i < n:
    if target >= data[i]:
        target += data[i]
        i += 1
    else:
        break
print(target)