#10816
#

MAX =int(1e7)

def index(x):
    if x >= 0:
        return x+MAX
    else:
        return MAX+x



n = int(input())
first = list(map(int,input().split()))
m = int(input())
second = list(map(int,input().split()))

hash = [0]*(MAX*2+1)


for i in range(n):
    hash[index(first[i])] += 1

for i in range(m):
    print(hash[index(second[i])],end=' ')
