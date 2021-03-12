import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e11)
data = list(map(int, input().split()))
left = 0
right = len(data) - 1
answer = INF
ans = []

while left < right:
    mix = data[right] + data[left]
    if abs(answer) > abs(mix):
        answer = mix
        ans = [data[left], data[right]]

    if mix > 0:
        right -= 1
    elif mix < 0:
        left += 1
    else:
        break


print(' '.join(str(i) for i in ans))