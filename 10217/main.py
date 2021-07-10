import sys
input = sys.stdin.readline
INF = sys.maxsize

for tc in range(int(input())):
    n, m, k = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(k):
        u, v, c, d = map(int, input().split())
        graph[u].append([v, c, d])

    dp = [[INF] * (m + 1) for _ in range(n + 1)]
    dp[1][0] = 0
    for money in range(m + 1):
        for now in range(1, n + 1):
            if dp[now][money] == INF:
                continue
            n_dist = dp[now][money]
            for will, w_m, w_d in graph[now]:
                if money + w_m > m:
                    continue

                dp[will][money + w_m] = min(dp[will][money + w_m], n_dist + w_d)

    answer = min(dp[n])
    print("Poor KCM" if answer >= INF else answer)