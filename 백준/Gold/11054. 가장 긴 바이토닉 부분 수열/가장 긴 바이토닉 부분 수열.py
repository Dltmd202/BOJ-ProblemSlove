from bisect import bisect_left

if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))

    inc = [1] * len(data)
    des = [1] * len(data)

    for i in range(len(data)):
        for j in range(i):
            if data[i] > data[j]:
                inc[i] = max(inc[i], inc[j] + 1)

    for i in range(len(data) - 1, -1, -1):
        for j in range(i + 1, n):
            if data[i] > data[j]:
                des[i] = max(des[i], des[j] + 1)

    max_val = 0

    for f, b in zip(inc, des):
        max_val = max(max_val, f + b)
    print(max_val - 1)
