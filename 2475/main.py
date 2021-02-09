data = list(map(int,input().split()))
ret = 0
for d in data:
    ret += d**2

print(int(ret)%10)
