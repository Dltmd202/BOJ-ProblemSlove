import sys
from collections import defaultdict

n = int(input())
graph = [list(map(int, input().split(''))) for _ in range(n)]
dp = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: -1)))


def search(now, bought, visit):
    ret = dp[now][bought][visit]
    if ret != -1:
        return ret
    visit |= (1 << now)
    for will in range(n):
        if will == now:
            continue
        if graph[now][will] >= bought:
            if not visit & (1 << will):
                ret = max(ret, search(will, graph[now][will], visit))
    visit ^= (1 << now)
    dp[now][bought][visit] = (ret + 1)
