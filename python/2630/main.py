import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
white = 0
blue =0


def divid(col, row, n):
    global white
    global blue
    result = True
    comp = paper[col][row]
    for i in range(col, col + n):
        for j in range(row, row + n):
            if comp != paper[i][j]:
                divid(col, row, n // 2)
                divid(col + n // 2, row, n // 2)
                divid(col , row + n // 2, n // 2)
                divid(col + n // 2, row + n // 2, n // 2)
                return

    if comp == 1:
        blue += 1
        return
    else:
        white += 1
        return


n = int(input())
paper = []

for i in range(n):
    paper.append(list(map(int, input().split())))


divid(0, 0, len(paper))
print(white)
print(blue)
