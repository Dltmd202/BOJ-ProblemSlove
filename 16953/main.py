
a, b = map(int, input().split())

answer = int(1e9)


def solution(a, b, cnt):
    global answer
    if a > b:
        return
    elif a == b:
        answer = min(answer, cnt)

    solution(a * 2, b, cnt + 1)
    solution(a * 10 + 1, b, cnt + 1)


solution(a, b, 0)
if answer >= int(1e9):
    print(-1)
else:
    print(answer + 1)
