#10816
#

MAX =int(1e7)

n = int(input())
first = list(map(int,input().split()))
m = int(input())
second = list(map(int,input().split()))

hash = [0]*(MAX+1)

for i in range(n):
    hash[first[i]] += 1

for i in range(m):
    print(hash[second[i]],end=' ')