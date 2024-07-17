import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + data[i]
    answer = []

    for i in range(m):
        a, b = map(int, input().split())
        answer.append(str(prefix_sum[b] - prefix_sum[a - 1]))
    print('\n'.join(answer))
