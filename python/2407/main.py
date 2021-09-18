from math import factorial

factorials = [0] * 202
factorials[0] = 1
factorials[1] = 1
factorials[2] = 2
for i in range(3, 202):
    factorials[i] = i * factorials[i - 1]

n, m = map(int, input().split())
print(int(factorials[n]//(factorials[m] * factorials[n - m])))