from collections import deque

MAX_VAL = int(1e9)
M = 100_000
dp = [MAX_VAL] * (M + 1)

if __name__ == '__main__':
    n, k = map(int, input().split())
    q = deque()
    q.append(n)
    dp[n] = 0

    while q:
        # print(q)
        now = q.popleft()

        if now != 0 and now * 2 <= M and dp[now * 2] > dp[now]:
            dp[now * 2] = dp[now]
            q.append(now * 2)

        if now - 1 >= 0 and dp[now - 1] > dp[now] + 1:
            dp[now - 1] = dp[now] + 1
            q.append(now - 1)

        if now + 1 <= M and dp[now + 1] > dp[now] + 1:
            dp[now + 1] = dp[now] + 1
            q.append(now + 1)

    print(dp[k])
    # print(dp[:30])
