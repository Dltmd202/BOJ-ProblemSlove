import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    graph[i] += line


def div(n, y, x):
    if n == 1:
        return {graph[y][x]: 1}
    buf = {-1: 0, 0: 0, 1: 0}
    for i in range(y, y + n, n // 3):
        for j in range(x, x + n, n // 3):
            div_res = div(n // 3, i, j)
            for d in div_res.keys():
                buf[d] += div_res[d]
    res = {-1: 0, 0: 0, 1: 0}
    if sorted(list(buf.values()), reverse=True)[0] == 9:
        res[graph[y][x]] += 1
    else:
        for d in buf.keys():
            res[d] += buf[d]
    return res


res = div(n, 0, 0)
print(res[-1])
print(res[0])
print(res[1])