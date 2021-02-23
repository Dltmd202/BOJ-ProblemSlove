from collections import deque
import sys
input = sys.stdin.readline

for tc in range(int(input())):

    n = int(input())
    data = list(map(int, input().split()))
    data.sort(reverse=True)
    data = deque(data)
    log = deque([data.popleft()])
    length = len(data)
    answer = 0

    while len(data) > 1:
        first = data.popleft()
        second = data.popleft()
        dq_first = log[0]
        dq_second = log[-1]

        sep_ftf = max(dq_first - first, dq_second - second)
        sep_fts = max(dq_second - first, dq_first - second)

        if sep_ftf < sep_fts:
            log.appendleft(first)
            log.append(second)
            answer = max(answer, sep_ftf)
        else:
            log.append(first)
            log.appendleft(second)
            answer = max(answer, sep_fts)
    if data:
        left = data.popleft()

        dq_first = log[0]
        dq_second = log[-1]

        if dq_first - left < dq_second - left:
            log.appendleft(left)
            answer = max(answer, dq_first - left)
        else:
            log.append(left)
            answer = max(answer, dq_second - left)
    answer = max(answer, abs(log[0] - log[-1]))
    print(answer)
