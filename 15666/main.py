
from itertools import combinations_with_replacement

n, m = map(int, input().split())
data = list(map(int, input().split()))
answer = set()

for permutation in combinations_with_replacement(data, m):
    line = []
    for p in permutation:
        line.append(p)
    line.sort()
    answer.add(tuple(line))

for ans in sorted(answer):
    print(' '.join(str(num) for num in ans))
