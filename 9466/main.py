import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

for tc in range(int(input())):
    n = int(input())
    data = [0] + list(map(int, input().split()))
    visit = [False] * (n + 1)
    result = []

    def dfs(start):
        visit[start] = True
        stack.append(start)
        will = data[start]

        if visit[will]:
            if will in stack:
                while True:
                    top = stack[-1]
                    stack.pop()
                    result.append(top)
                    if will == top:
                        break
        else:
            dfs(will)

    for i in range(1, n + 1):
        if not visit[i]:
            stack = []
            dfs(i)
    print(n - len(result))