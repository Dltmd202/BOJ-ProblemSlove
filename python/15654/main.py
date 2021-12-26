
from itertools import permutations

n, m = map(int, input().split())
data = list(map(int, input().split()))
answer = []

for permutation in permutations(data, m):
    answer.append(permutation)
answer.sort()

for ans in answer:
    print(' '.join(str(num) for num in ans))