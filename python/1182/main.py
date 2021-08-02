import sys
input = sys.stdin.readline

def find(idx, sum):
    global cnt
    if idx >= len(data):
        return
    sum += data[idx]
    if sum == s:
        cnt += 1
    find(idx + 1, sum - data[idx])
    find(idx + 1, sum)


cnt = 0
n, s = map(int, input().split())
data = list(map(int, input().split()))
find(0, 0)
print(cnt)