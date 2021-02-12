import sys
sys.setrecursionlimit(int(1e5))
n = int(input())
data = list(map(int, input().split()))
visit = [False] * (n + 1)
answer = 0


def dfs(cnt, selected: list):
    global answer
    if len(selected) == n:
        ans = 0
        for turn in range(len(selected) - 1):
            ans += abs(selected[turn] - selected[turn + 1])
        answer = max(answer, ans)

    for i in range(n):
        if not visit[i]:
            visit[i] = True
            selected.append(data[i])
            dfs(cnt + 1, selected)
            selected.pop()
            visit[i] = False


dfs(0, [])
print(answer)