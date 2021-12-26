n = int(input())
table = [1] * (n + 1)
table[0] = 1
for i in range(1, n + 1):
    table[i] = (table[i - 1] * 31)

a = list(map(lambda x: ord(x) - ord('a') + 1, input()))
res = 0
for i in range(n):
    res += (a[i] * table[i])
print(res % 1234567891)
