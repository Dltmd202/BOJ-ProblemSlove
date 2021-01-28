n =int(input())
data = []
answer = []

for i in range(n):
    data.append(int(input()))
data.sort(reverse=True)
data = [0] + data

for i in range(1,n+1):
    answer.append(i*data[i])
print(max(answer))