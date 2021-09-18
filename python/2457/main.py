import sys
input = sys.stdin.readline
n = int(input())
flowers = [list(map(int, input().split())) for _ in range(n)]
flowers.sort(key=lambda x: [[x[0], x[1]], [-x[2], -x[3]]])
mon = 3
date = 1
end_month = 3
end_date = 1
idx = 0
answer = 0
while True:
    if mon > 11 or mon == 11 and date == 31:
        break
    for i in range(n):
        if flowers[i][0] < mon or flowers[i][0] == mon and flowers[i][1] <= date:
            if flowers[i][2] > end_month or flowers[i][2] == end_month and flowers[i][3] >= end_date:
                end_month = flowers[i][2]
                end_date = flowers[i][3]

    if mon == end_month and date == end_date:
        answer = 0
        break
    answer += 1
    mon = end_month
    date = end_date

print(answer)