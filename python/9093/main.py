from collections import deque

for _ in range(int(input())):
    strings = input().strip().split()
    for s in strings:
        print(s[::-1], end=' ')
