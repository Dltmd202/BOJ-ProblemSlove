
k , n = map(int,input().split())

data =[]

for i in range(k):
    data.append(int(input()))

data.sort()
left = 1
right = data[-1]

def calc(pivot):
    sum = 0
    for i in data:
        sum += (i // pivot)
    return sum

answer = 0

while left <= right:
    pivot = (left+right)//2
    sum = calc(pivot)


    if sum >= n:
        answer = pivot
        left = pivot +1
    else:
        right = pivot -1

print(answer)




