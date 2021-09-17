MOD = 1_000_000_007


def pow(n, m):
    if m == 1:
        return n
    else:
        ret = pow(n, m // 2)
        powerd = ret * ret % MOD
        if m % 2 == 0:
            return powerd % MOD
        else:
            return (powerd * n) % MOD


n, m = (int(input()) for _ in range(2))
print(pow(n, m))
