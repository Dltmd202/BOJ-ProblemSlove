import math

if __name__ == '__main__':
    H, W, N, M = map(int, input().split())
    print(int(math.ceil(H / (N + 1)) * math.ceil(W / (M + 1))))
