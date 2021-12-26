#10866
#https://www.acmicpc.net/status?user_id=dltmd202&problem_id=10866&from_mine=1
from collections import deque

n = int(input())

answer = []
d = deque()

for i in range(n):
    data = list(input().split())
    a = data[0]
    if len(data) == 2 :
        b = data[1]
    else:
        b=None

    if a == "push_back":
        d.append(int(b))

    elif a =="push_front":
        d.appendleft(int(b))

    elif a =="pop_front":
        if len(d) == 0:
            answer.append(-1)
        else:answer.append(d.popleft())

    elif a =="pop_back":
        if len(d) == 0:
            answer.append(-1)
        else:answer.append(d.pop())

    elif a =="size":
        answer.append(len(d))

    elif a =="empty":
        if len(d) == 0:
            answer.append(1)
        else:
            answer.append(0)
    elif a =="front":
        if len(d) == 0:
            answer.append(-1)
        else:
            answer.append(d[0])
    elif a =="back":
        if len(d) == 0:
            answer.append(-1)
        else:
            answer.append(d[-1])
for ans in answer:
    print(ans)


