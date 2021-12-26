#3273
#https://www.acmicpc.net/problem/3273

n = int(input())
data =list(map(int,input().split()))
x= int(input())
data.sort()


count = 0
interval_sum = 0
end = n-1
start = 0

while(start <end):
    interval_sum = data[start]+data[end]
    if interval_sum >x :
        end -=1
    elif interval_sum <x:
        start +=1
    else:
        count += 1
        end -=1
        start +=1
print(count)