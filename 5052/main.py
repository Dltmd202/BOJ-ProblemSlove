import re
import sys

input = sys.stdin.readline

for tb in range(int(input())):
    n = int(input())
    s = []
    for i in range(n):
        s.append(input().rstrip())
    s.sort()
    result = True
    for i in range(n - 1):
        if s[i + 1][:len(s[i])] == s[i]:
            result = False

    print("YES" if result else "NO")
