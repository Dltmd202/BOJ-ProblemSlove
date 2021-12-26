#9012
#https://www.acmicpc.net/problem/9012
#O(N)
# 2<= length <= 50

from collections import deque

n = int(input())
answer = []

def solution():
    data= input()
    q = deque()
    length = len(data)
    for j in range(length):
        if data[j] == '(':
            q.append(1)
        elif data[j] == ')':
            if q.count(1) == 0:
                return "NO"
            else:
                q.pop()

    if q.count(1) == 0:
        return "YES"
    else:
        return "NO"

for i in range(n):
    answer.append(solution())




for ans in answer:
    print(ans)

