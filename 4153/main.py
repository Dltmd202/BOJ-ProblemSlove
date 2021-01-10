#4153
#https://www.acmicpc.net/status?user_id=bat5273&problem_id=4153&from_mine=1


data = []

while True:
    t =  list(map(int,input().split()))
    t.sort(reverse=True)
    if t[0] == 0:
        break
    data.append(t)

answer = []

for t in data:
    if t[0]**2  == t[1]**2 + t[2]**2:
        print("right")
    else:
        print("wrong")

