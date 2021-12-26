#10844
#https://www.acmicpc.net/status?from_mine=1&problem_id=10844&user_id=bat5273

n = int(input())
left = int(1e9)
count = [9]
zero = [0]
nine = [1]

one = [1]
eight = [1]

two = [1]
seven = [1]

three = [1]
six = [1]

four = [1]
five = [1]

number = [[0],[1],[1],[1],[1],[1],[1],[1],[1],[1]]
for i in range(1,n+1):
    number[0].append(number[1][i-1]%left)
    number[9].append(number[8][i-1]%left)

    for j in range(1,9):
        number[j].append((number[j-1][i-1]%left+number[j+1][i-1]%left)%left)
    count.append( (count[i-1]*2%left - (number[0][i-1]+number[9][i-1]))%left)

print(count[n-1])