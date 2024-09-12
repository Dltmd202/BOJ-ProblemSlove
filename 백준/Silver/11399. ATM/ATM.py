if __name__ == '__main__':
    N = int(input())
    data = list(map(int, input().split()))

    data.sort()
    tmp = data[0]
    answer = data[0]

    for i in range(1, N):
        tmp += data[i]
        answer += tmp
    
    print(answer)