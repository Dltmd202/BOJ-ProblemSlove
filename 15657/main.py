from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
data = list(map(int, input().split()))
answer = set()

for pro in combinations_with_replacement(data , m):
    line = []
    for p in pro:
        line.append(p)
    line.sort()
    answer.add(tuple(line))


for ans in sorted(list(answer)):
    print(' '.join(str(num) for num in sorted(ans)))

