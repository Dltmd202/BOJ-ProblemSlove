import sys
MAX = 100000
input = sys.stdin.readline

for tb in range(int(input())):
    n = int(input())
    candidates = []

    for i in range(n):
        [a, b] = map(int, input().split())
        candidates.append((a, b))

    candidates.sort()

    paper_min = candidates[0][0]
    interview_min = candidates[0][1]
    count = 1

    for paper, interview in candidates[1:]:
        if interview > interview_min:
            continue
        else:
            interview_min = min(interview, interview_min)
            count += 1

    print(count)
