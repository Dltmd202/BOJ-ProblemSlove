if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    answer = [0] * n

    for target in range(n):
        target_cnt = data[target]
        for tmp in range(n):
            if answer[tmp] == 0 and target_cnt == 0:
                answer[tmp] = target + 1
                break
            elif answer[tmp] == 0:
                target_cnt -= 1
    print(' '.join(map(str, answer)))
