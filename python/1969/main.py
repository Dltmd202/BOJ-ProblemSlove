n, m = map(int, input().split())
s = []
result = ""
cnt = 0
for i in range(n):
    a = input()
    s.append(a.upper())
for i in range(m):
    a = [0 for i in range(26)]
    for j in range(n):
        a[ord(s[j][i]) - 65] += 1
    result += chr(a.index(max(a)) + 65)
for i in range(n):
    for j in range(m):
        if s[i][j] != result[j]:
            cnt += 1
print(result)
print(cnt)