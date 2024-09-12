if __name__ == '__main__':
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    data.sort(key=lambda x: (x[1], x[0]))
    start, end = data[0][0], data[0][1]
    answer = 1

    for i in range(1, N):
        ts, te = data[i][0], data[i][1]

        if ts < end:
            continue

        end = te
        answer += 1
    
    print(answer)
