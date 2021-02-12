import math

n = int(input())
data = list(map(int, input().split()))

for wheel in data[1: ]:
    gcd = math.gcd(data[0], wheel)
    print(f'{data[0]//gcd}/{wheel//gcd}')

