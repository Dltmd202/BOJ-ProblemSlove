from math import log2


def set_width(k: int) -> int:
    if k == 0:
        widths[k] = 5
        return widths[k]
    else:
        widths[k] = set_width(k - 1) * 2 + 1
        return widths[k]


def set_height(k: int, height: int):
    heights[k] = height
    for i in range(k - 1, -1, -1):
        heights[i] = heights[i + 1] // 2


def start(step, y, x):
    if step == 0:
        for dx in range(5):
            graph[y][x - dx] = 1
        graph[y - 1][x - 1] = 1
        graph[y - 1][x - 3] = 1
        graph[y - 2][x - 2] = 1
    else:
        start(step - 1, y, x)
        start(step - 1, y - heights[step - 1], x - heights[step - 1])
        start(step - 1, y, x - (widths[step - 1] + 1))


height = int(input())
k = int(log2(height//3))
widths = [0] * (k + 1)
heights = [0] * (k + 1)
width = set_width(k)
set_height(k, height)
graph = [[0] * (width + 1) for _ in range(height + 1)]
start(k, height, width)
ans = ""
for line in graph[1:]:
    for dot in line[1:]:
        ans += ("*" if dot else " ")
    ans += "\n"

print(ans)