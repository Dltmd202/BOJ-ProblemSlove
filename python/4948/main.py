#4948
#https://www.acmicpc.net/problem/4948

data = []

max = -1
while True:
    d = int(input())
    if d == 0:
        break
    if d > max:
        max =  d
    data.append(d)


prime = [0] * ( (2 *max) + 2)
prime[1] = 1

for i in range(2,2 * max + 2):
    cnt = 1
    while i * cnt <= (2 * max + 1):
        prime[i*cnt] += 1
        cnt += 1

answer = []

for i in data:
    count = 0
    for j in range(i+1,2*i +1):
        if prime[j] == 1:
            count += 1
    answer.append(count)

for ans in answer:
    print(ans)


