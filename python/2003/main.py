

n, m = map(int, input().split())
data = list(map(int, input().split()))



right = 0
sum = 0
count = 0
for start in range(len(data)):
    while sum < m and right < len(data):
        sum += data[right]
        right += 1

    if sum == m:
        count += 1

    sum -= data[start]
print(count)