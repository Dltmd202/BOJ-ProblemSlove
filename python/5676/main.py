import sys
input = sys.stdin.readline

tree = list()
nodes = list()


def pmz(n):
    if n > 0: return 1
    elif n < 0: return -1
    else: return 0


def update(start, end, index, cIdx, cNum):
    if end < cIdx or cIdx < start:
        return
    if start == end:
        tree[index] = cNum
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, cIdx, cNum)
    update(mid + 1, mid, index * 2 + 1, cIdx, cNum)
    tree[index] = tree[index * 2] * tree[index * 2 + 1]


def query(start, end, index, left, right):
    if end < left or right < start:
        return 1
    if left <= start and end <= right:
        return tree[index]
    mid = (start + end) // 2
    return query(start, mid, index * 2, left, right) * query(mid + 1, end, index * 2 + 1, left, right)


def init(start, end, index):
    if start == end:
        nodes[start] = pmz(nodes[start])
        tree[index] = nodes[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = init(start, mid, index * 2) * init(mid + 1, end, index * 2 + 1)
    return tree[index]


if __name__ == '__main__':
    while True:
        try:
            n, k = map(int, input().rstrip().split())
            tree = [0] * (n * 4)
            nodes = [0] + list(map(int, input().rstrip().split()))
            answer = ""
            init(1, n, 1)
            for i in range(k):
                order, *args = input().split()
                if order == 'C':
                    i, v = map(int, args)
                    nodes[i] = pmz(v)
                    update(1, n, 1, i, pmz(v))
                else:
                    i, j = map(int, args)
                    res = query(1, n, 1, i, j)
                    if res == 0:
                        answer += '0'
                    elif res > 0:
                        answer += '+'
                    else:
                        answer += '-'
            print(answer)
        except Exception:
            break