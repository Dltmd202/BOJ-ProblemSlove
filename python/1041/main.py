n = int(input())
data = list(map(int, input().split()))
answer = 0
s = []
if n == 1:
    data.sort()
    print(sum(data[: -1]))
else:
    s.append(min(data[0], data[5]))
    s.append(min(data[1], data[4]))
    s.append(min(data[2], data[3]))
    s.sort()
    answer += s[0] * (int(n**2) + 4 * int((n - 1)**2))
    answer += s[1] * 8 * (n - 1)
    answer += s[2] * 4
    print(answer)

