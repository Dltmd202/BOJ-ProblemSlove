from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
names = defaultdict(bool)
for i in range(n):
    data = input().strip().split()
    if data[1] == 'enter':
        names[data[0]] = True
    elif data[1] == 'leave':
        names[data[0]] = False

for name, res in sorted(names.items(), key=lambda x: x[0], reverse=True):
    if res:
        print(name)