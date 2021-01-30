import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

unheard = collections.defaultdict(int)

for i in range(n):
    unheard[input().rstrip()] += 1

for i in range(m):
    unheard[input().rstrip()] += 1

ordered = [word for word in unheard.keys() if unheard[word] == 2]
ordered.sort()

print(len(ordered))
print('\n'.join(word for word in ordered))
