
if __name__ == '__main__':
    n = int(input())
    distances = list(map(int, input().split()))
    fuels = list(map(int, input().split()))

    f_idx = 0
    min_fuel = int(1e9)
    need_fuel = 0
    for dist in distances:
        min_fuel = min(min_fuel, fuels[f_idx])
        f_idx += 1

        need_fuel += min_fuel * dist

    print(need_fuel)
