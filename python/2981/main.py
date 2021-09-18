import math

n = int(input())
data = []
gcd = 0
for i in range(n):
    data.append(int(input()))
data.sort()

for i in range(n):
    if i == 1:
        gcd = data[i] - data[i - 1]
    gcd = math.gcd(gcd, data[i] - data[i - 1])

answer = set()
for i in range(2, int(math.sqrt(gcd)) + 1):
    if gcd % i == 0:
        answer.add(i)
        answer.add(gcd // i)
answer.add(gcd)
answer = list(answer)
answer.sort()
print(' '.join(str(num) for num in answer))