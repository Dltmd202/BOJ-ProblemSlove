import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.sort()
answer = int(1e10)
ans = []

for i in range(n - 1):
    left = i + 1
    right = n - 1
    while left < right:
        mix = data[i] + data[left] + data[right]
        if abs(answer) > abs(mix):
            ans = (data[i], data[left], data[right])
            answer = mix

        if mix < 0:
            left += 1
        elif mix > 0:
            right -= 1
        else:
            break

print(' '.join(str(i) for i in ans))

