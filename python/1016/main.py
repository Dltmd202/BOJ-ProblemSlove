import math
from collections import Counter

min, max = map(int, input().split())

data = [False] * (max - min + 1)
n = 2

while n ** 2 <= max:
    pivot = n ** 2
    cnt = min / pivot
    cnt = math.ceil(cnt)
    while pivot * cnt <= max:
        data[pivot * cnt - min] = True
        cnt += 1
    n += 1
counter = Counter(data)
print(counter[False])
