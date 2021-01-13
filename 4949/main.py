
from collections import deque

data =[]
answer =[]
while True:
    d = input()
    if d[0] =='.':
        break
    data.append(d)

for i in range(len(data)):
    s = deque()
    result = True
    first = 0
    for j in data[i]:
        if j == "(":
            s.append(1)
        elif j == ")":
            if len(s) == 0:
                result =False
                break
            else:
                if s.pop() != 1:
                    result =False
                    break
        if j =='[':
            s.append(2)
        elif j ==']':
            if len(s) == 0:
                result =False
                break
            else:
                if s.pop() != 2:
                    result=False
                    break
    if len(s) != 0 :
        result =False
    if result:
        answer.append("yes")
    else:
        answer.append("no")

for ans in answer:
    print(ans)