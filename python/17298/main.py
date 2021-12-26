import sys

input = sys.stdin.readline
n = int(input())

data = list(map(int, input().split()))
stack = []

answer = [-1]*(n)

for i in range(n):
    while len(stack) and data[stack[-1]] < data[i]:
        answer[stack[-1]] = data[i]
        stack.pop()
    stack.append(i)
print(*answer)