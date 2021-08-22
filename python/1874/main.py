from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
stack = deque()
answer = []


min_stack = 1
result = True

for d in data:
    if not stack or min_stack <= d:
        for i in range(min_stack, d):
            stack.append(i)
            answer.append("+")
        answer.append("+")
        answer.append("-")
        min_stack = d + 1
    else:
        sd = stack.pop()
        if d != sd:
            answer = ["NO"]
            break
        else:
            answer.append("-")

print("\n".join(ans for ans in answer))