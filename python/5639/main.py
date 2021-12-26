import sys
sys.setrecursionlimit(int(1e5))

data = []


def div(left, right):
    if left > right:
        return

    root = data[left]
    idx = left + 1
    while idx <= right:
        if data[idx] > root:
            break
        idx += 1

    div(left + 1, idx - 1)
    div(idx, right)
    print(root)


def solution():
    while True:
        try:
            data.append(int(input()))
        except:
            break
    div(0, len(data) - 1)


solution()