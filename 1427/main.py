#1427
#https://www.acmicpc.net/status?user_id=bat5273&problem_id=1427&from_mine=1
#O(logN)


data = list(map(int ,input()))

data.sort(reverse=True)

for i in data:
    print(i,end='')