from collections import defaultdict, Counter

name = input()

char = defaultdict(int)

for c in name:
    char[c] += 1

count = Counter(char)
answer =[]
result = True

if len(name) % 2 == 0:
    for cnt in count:
        if count[cnt] % 2 == 0:
            answer += [cnt] * (count[cnt]//2)
        else:
            print("I'm Sorry Hansoo")
            result = False
            break
    if result:
        answer.sort()
        answer += answer[::-1]
        print(''.join(str(a) for a in answer))
else:
    odd = -1
    for cnt in count:
        if count[cnt] % 2 == 0:
            answer += [cnt] * (count[cnt]//2)
        else:
            if odd == -1:
                odd = cnt
                answer += [cnt] * (count[cnt]//2)
            else:
                print("I'm Sorry Hansoo")
                result = False
                break
    if result:
        answer.sort()
        answer += ([odd] + answer[::-1])
        print(''.join(str(a) for a in answer))

