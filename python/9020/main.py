n = int(input())

data = []
max_value = 0
for i in range(n):
    data.append(int(input()))
    max_value = max(max_value , data[i])


table = [0] * (max_value+1)

for i in range(2,max_value+1):
    cnt = 1
    while i * cnt <(max_value+1):
        table[i*cnt] += 1
        cnt += 1

answer = []

for d in data:
    dist = 10000
    part = 10000
    for i in range(d//2+1):
        if table[i] == 1 and table[d-i] == 1 and dist > (d-i)-i:
            dist = (d-i)-i
            part = i
    answer.append(part)


for i in range(len(answer)):
    print(answer[i] , data[i]-answer[i] )
