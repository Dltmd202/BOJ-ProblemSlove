if __name__ == '__main__':
    N = int(input())
    lope = [int(input()) for _ in range(N)]
    lope.sort(reverse=True)

    answer = lope[0]
    cnt = 1

    for i in range(1, N):
        cnt += 1
        answer = max(answer, lope[i] * cnt)
    
    print(answer)