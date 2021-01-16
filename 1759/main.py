#1759
#https://www.acmicpc.net/problem/1759

from itertools import combinations

n , m = map(int,input().split())
data = list(map(str,input().split()))
data.sort()
answer =[]
def count(com):
    first = 0
    second = 0
    for i in range(len(com)):
        if com[i] == 'a':
            first += 1
        elif com[i] == 'i':
            first += 1
        elif com[i] == 'e':
            first += 1
        elif com[i] == 'o':
            first += 1
        elif com[i] == 'u':
            first += 1
        else:
            second += 1
    if first >= 1 and second >=2 :
        return True
    else:
        return False

for com in combinations(data,n):
    if count(com):
        answer.append(com)

for ans in answer:
    buf =''
    for i in ans:
        buf += str(i)
    print(buf)
