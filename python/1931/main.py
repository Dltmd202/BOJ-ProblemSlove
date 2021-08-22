#1931
#https://www.acmicpc.net/problem/1931

n = int(input())
data = []

for i in range(n):
    data.append(list(map(int,input().split())))

data.sort(key=lambda x : [x[0], (x[1]-x[0])])
answer = 0
cnt = 0
start = 0
end = 0

for i in range(n):
    if data[i][0] >= end :
        start = end
        end = data[i][1]
        cnt += 1
    elif data[i][1] <= end:
        end = data[i][1]

print(cnt)

