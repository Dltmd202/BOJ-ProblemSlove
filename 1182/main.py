
n, s = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
# print(data)
second =1
sum = data[0]
cnt = 0

for first in range(n-1):
    while second < n and sum < s :
        # print(first , second , sum)
        if data[second] > 0 and data[second] > - data[first] and second > first + 1:
            break
        sum += data[second]
        second += 1
    if sum == s:
        cnt += 1
    sum -= data[first]

    # print("first++",first +1 , second , sum)
print(cnt)