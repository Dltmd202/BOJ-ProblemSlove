from collections import deque

if __name__ == '__main__':
    n = int(input())
    data = deque(sorted(map(int, input().split())))
    budget = int(input())
    answer = 0

    while data:
        personal = budget // len(data)
        d = data.popleft()

        if d < personal:
            answer = d
            budget -= answer
        else:
            answer = personal
            break

    print(answer)

