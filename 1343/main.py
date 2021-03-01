
s = input()
answer = ""
result = True
cnt = 0
for i in range(len(s)):
    if s[i] == 'X':
        cnt += 1
    else:
        if cnt % 2 != 0:
            result = False
            break
        else:
            if cnt % 4 == 2:
                answer += ('A' * (cnt - 2))
                answer += ('B' * 2)
            else:
                answer += ('A' * cnt)
            cnt = 0
            answer += '.'

if cnt:
    if cnt % 2 != 0:
        result = False
    else:
        if cnt % 4 == 2:
            answer += ('A' * (cnt - 2))
            answer += ('B' * 2)
        else:
            answer += ('A' * cnt)
        cnt = 0

if result:
    print(answer)
else:
    print(-1)