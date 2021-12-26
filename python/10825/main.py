#10825
#https://www.acmicpc.net/status?user_id=bat5273&problem_id=10825&from_mine=1

n = int(input())

data =[]
for i in range(n):
    name, kor ,eng, mat = input().split()
    data.append((name,int(kor),int(eng),int(mat)))

data.sort(key=lambda x :(-x[1],x[2],-x[3],x[0]))
for i in range(len(data)):
    print(data[i][0])