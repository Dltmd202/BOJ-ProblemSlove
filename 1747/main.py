import math
MAX = int(1e6 + 3002)
n = int(input())
prime = [False, False] + [True] * MAX

for i in range(2, int(math.sqrt(MAX)) + 1):
    if prime[i]:
        j = 2
        while i * j <= MAX:
            prime[i * j] = False
            j += 1

for i in range(n, MAX):
    if prime[i]:
        s = str(i)
        if s == s[::-1]:
            print(s)
            break
