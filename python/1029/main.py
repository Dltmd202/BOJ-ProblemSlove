import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
cache = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: -1)))


def search(now, bought, visit):
    ret = cache[now][bought][visit]
    if ret != -1:
        return ret
    visit |= (1 << now)
    ret = 0
    for will in range(n):
        if will == now:
            continue
        if graph[now][will] >= bought:
            if not visit & (1 << will):
                ret = max(ret, search(will, graph[now][will], visit))
    visit ^= (1 << now)

    cache[now][bought][visit] = (ret + 1)
    return cache[now][bought][visit]


print(search(0, 0, 0))