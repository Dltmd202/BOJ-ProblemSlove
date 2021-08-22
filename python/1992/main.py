import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]
division = []


def div(y, x, n):
    if n == 1:
        return graph[y][x]
    res = []
    same = True
    for i in range(y, y + n, n // 2):
        for j in range(x, x + n, n // 2):
            buf = div(i, j, n // 2)
            if type(buf) is list:
                same = False
            res.append(buf)
    if same and (sum(res) == 4 or sum(res) == 0):
        return graph[y][x]
    else:
        return res


def printp(start):
    if type(start) is not list:
        print(start, end='')
        return
    print("(", end='')
    for will in start:
        printp(will)
    print(")", end='')


division = div(0, 0, n)
printp(division)