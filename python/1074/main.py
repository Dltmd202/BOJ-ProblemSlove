import sys
sys.setrecursionlimit(int(1e5))

n, r, c = map(int, input().split())
cnt = 0

while n >= 1:
    grid = 2 ** (n - 1)
    r_grid = r // grid
    c_grid = c // grid
    r = r % grid
    c = c % grid
    if not r_grid and c_grid:
        cnt += (grid * grid)
    elif r_grid and not c_grid:
        cnt += (2 * (grid * grid))
    elif r_grid and c_grid:
        cnt += (3 * (grid * grid))
    n -= 1

print(cnt)
