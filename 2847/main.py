
n = int(input())
data = []
answer = 0
for i in range(n):
    data.append(int(input()))

for i in range(n - 2, -1, -1):
    if data[i] >= data[i + 1]:
        answer += (data[i] - data[i + 1] + 1)
        data[i] = data[i + 1] - 1
print(answer)
