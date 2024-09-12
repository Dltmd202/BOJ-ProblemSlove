import collections

if __name__ == '__main__':
    N, K = map(int, input().split())
    data = [int(input()) for _ in range(N)]
    answer = 0

    for i in range(N -1, -1, -1):
        cnt = K // data[i]
        answer += cnt
        K %= data[i]
    
    print(answer)
