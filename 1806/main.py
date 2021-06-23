import sys
input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))
prefix = [0]
left, right = 0, 1

answer = int(1e9)

for i in range(1, n + 1):
    prefix.append(prefix[i - 1] + data[i - 1])

while left < n:
    if prefix[right] - prefix[left] >= s:
        answer = min(answer, right - left)
        left += 1
    else:
        if right < n:
            right += 1
        else:
            left += 1


if answer >= int(1e8):
    print(0)
else:
    print(answer)


