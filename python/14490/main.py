
import math

data = list(map(int, input().split(':')))
GCD = math.gcd(data[0], data[1])
print(f'{data[0] // GCD}:{data[1] // GCD}')