
n , k = map(int,input().split())
data = []

for i in range(n):
    data.append(int(input()))

data.sort(reverse=True)
count = 0

for i in range(n):
    count += (k // data[i])
    k =(k % data[i])

print(count)