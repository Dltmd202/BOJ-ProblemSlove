MOD = 1_000_000_000

if __name__ == '__main__':
    target = int(input())


    def solution(target):

        dp = [[0] * 11 for _ in range(target + 1)]

        dp[1] = [0] + [1] * 9 + [0]

        def get_memorized(a, b):
            try:
                val = dp[a][b]
                return val
            except:
                return 0

        for i in range(2, target + 1):
            for j in range(0, 10):
                dp[i][j] = (get_memorized(i - 1, j - 1) + get_memorized(i - 1, j + 1)) % MOD

        return sum(dp[target]) % MOD

    print(solution(target))
