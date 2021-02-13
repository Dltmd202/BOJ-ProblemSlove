
n, l = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
cnt = 0
left_length = 0
turn = 0

while turn < n:
    if 1 <= turn < n and data[turn] - data[turn - 1] + 0.5 <= left_length:
        while 1 <= turn < n and data[turn] - data[turn - 1] + 0.5 <= left_length:
            left_length -= (data[turn] - data[turn - 1])
            turn += 1
    else:
        cnt += 1
        left_length = (l - 0.5)
        turn += 1

print(cnt)