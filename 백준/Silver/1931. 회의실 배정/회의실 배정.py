import sys

input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    meetings = [tuple(map(int, input().split())) for _ in range(n)]
    meetings.sort(key=lambda x: (x[1], x[0]))

    # print(meetings)

    answer = 0
    cur = (0, 0)

    for meeting in meetings:
        if cur[1] <= meeting[0]:
            cur = meeting
            answer += 1

    print(answer)
