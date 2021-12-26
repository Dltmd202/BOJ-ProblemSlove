#18310
#https://www.acmicpc.net/problem/18310

n = int(input())
data =list(map(int,input().split()))
data.sort()

if n % 2 != 0:
    print(data[n//2])
else :
    left = 0
    right = 0
    for i in range(len(data)):
        left += abs(data[i] - data[n//2-1])
        right += abs(data[i] - data[n//2])
    if left <= right:
        print(data[n//2-1])
    else:
        print(data[n//2])