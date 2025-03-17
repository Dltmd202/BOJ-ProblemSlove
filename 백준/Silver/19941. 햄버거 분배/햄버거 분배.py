from collections import deque

if __name__ == '__main__':
    N, K = map(int, input().split())
    data = list(input())
    ans = 0

    for idx in range(N):
        if data[idx] == 'P':
            for i in range(max(idx - K, 0), min(idx + K + 1, N)):
                if data[i] == 'H':
                    data[i] = 0
                    ans += 1
                    break
    print(ans)