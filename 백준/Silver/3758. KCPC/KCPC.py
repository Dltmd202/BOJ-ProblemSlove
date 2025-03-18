if __name__ == '__main__':
    T = int(input())

    for tc in range(T):
        n, k, t, m = map(int, input().split())
        score = [[0] * k for _ in range(n)]
        submit = [0] * n
        time = [0] * n
        board = [[[0] * 2 for _ in range(k)] for _ in range(n)]
        total = [[0] * 3 for _ in range(n)]

        for idx in range(m):
            i, j, s = map(int, input().split())
            i -= 1
            j -= 1

            score[i][j] = max(score[i][j], s)
            submit[i] += 1
            time[i] = idx

        line = []

        for i in range(n):
            line.append([sum(score[i]), submit[i], time[i], i])
        line.sort(key=lambda x: (-x[0], x[1], x[2]))

        for i in range(n):
            if line[i][3] == t - 1:
                print(i + 1)
