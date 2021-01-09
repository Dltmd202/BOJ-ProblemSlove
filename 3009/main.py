#3009
#https://www.acmicpc.net/problem/3009

x =[]
y =[]

for i in range(3):
    a , b= map(int,input().split())
    x.append(a)
    y.append(b)

remX = sorted(x)[1]
remY = sorted(y)[1]

for i in range(2):
    x.remove(remX)
    y.remove(remY)


print(x[0],y[0])

