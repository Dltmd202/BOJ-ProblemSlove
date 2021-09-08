from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

n = int(input())
peoples = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
dp = defaultdict(lambda: {"true": -1, "false": -1})


def search(now):
    dp[now]["true"] = peoples[now]
    dp[now]["false"] = 0
    ret = peoples[now]
    child = 0
    for will in graph[now]:
        if dp[will]["true"] == -1:
            search(will)
            dp[now]["true"] += dp[will]["false"]
            dp[now]["false"] += max(dp[will]["true"], dp[will]["false"])


for i in range(n - 1):
    now, will = map(int, input().split())
    graph[now].append(will)
    graph[will].append(now)

search(1)
print(max(dp[1]["true"], dp[1]["false"]))