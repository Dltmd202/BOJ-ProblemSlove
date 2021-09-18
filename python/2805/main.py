

n , m= map(int,input().split())
data =list(map(int,input().split()))
data.sort()

def calc(data , pivot):
    sum = 0
    for i in range(len(data)):
        if data[i] > pivot:
            sum += (data[i]-pivot)
    return sum

left = 0
right = data[-1]
answer = 0


while left<=right:
    pivot = (left + right) //2
    now = calc(data,pivot)
    if now >= m:
        answer = pivot
        left = pivot + 1
    else:
        right = pivot-1

print(answer)