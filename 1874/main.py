#1874
#Stack with deque
#O(N)

from collections import  deque
n = int(input())
data = []
stack =[]
answer = []
for i in range(n):
    data.append(int(input()))

laststack = 0
lastpop = 0
result = True
for i in data:
    if i > laststack:
        for j in range(laststack,i):
            stack.append(i)
            answer.append('+')
        laststack = i
        lastpop = i
        answer.append('-')
    elif i < lastpop:
        answer.append('-')
        lastpop = i
    else:
        result =False
        print('NO')
        break

if result:
    for ans in answer:
        print(ans)