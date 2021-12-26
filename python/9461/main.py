#9461.py
#https://www.acmicpc.net/problem/9461

n = int(input())
data=[]
for i in range(n):
    data.append(int(input()))
answer = []

d =[0]*(max(data)+1)
d[0]=0
d[1]=1
d[2]=1
d[3]=1
d[4]=2



for i in range(5,max(data)+1):
    d[i] = d[i-1]+d[i-5]

for i in range(n):
    answer.append(d[data[i]])

for i in answer:
    print(i)