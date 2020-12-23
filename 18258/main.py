#18258.py
#https://www.acmicpc.net/problem/18258
#deque을 이용한 queue
#입력 시간초과로 sys를 import
#출력 시간초과로 출력값들을 \n으로 join 시킨다

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
orders = []
q = deque()
answer =[]
for i in range(n):
    order = input()
    data = order.split()
    if data[0] == 'push':
        q.append(int(data[1]))

    elif data[0] == 'pop':
        if len(q) == 0 :
            answer.append(-1)
        else:
            answer.append(q.popleft())

    elif data[0] == 'size':
        answer.append(len(q))

    elif data[0] == 'empty':
        if len(q) == 0:
            answer.append(1)
        else:
            answer.append(0)

    elif data[0] == 'front':
        if len(q) == 0:
            answer.append(-1)
        else:
            answer.append(q[0])

    elif data[0] == 'back':
        if len(q) == 0 :
            answer.append(-1)
        else :
            answer.append(q[len(q)-1])

print('\n'.join(str(ans) for ans in answer))





