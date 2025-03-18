import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())

    names = []
    for i in range(n):
        name, score = input().split()
        names.append((name, int(score)))

    names.sort(key=lambda x: x[1])

    scores = []
    for i in range(m):
        score = int(input())
        scores.append((score, i))
    scores.sort(key=lambda x: x[0])

    res = [0] * m
    tmp_idx = 0
    for score, idx in scores:
        while tmp_idx < n and score > names[tmp_idx][1]:
            tmp_idx += 1
        res[idx] = names[tmp_idx][0]

    print('\n'.join(res))
