n = int(input())
comp = [1, 2, 3]
ans = []
turn = 1
for i in range(n):
    if i % 2 == 0:
        ans.append(1)
    else:
        if turn == 1:
            ans.append(2)
            turn *= -1
        else:
            ans.append(3)
            turn *= -1

print(''.join(str(s) for s in ans))
