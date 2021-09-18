import sys
sys.setrecursionlimit(int(1e8))


def pre(in_left, in_right, post_left, post_right):
    if in_left > in_right or post_left > post_right:
        return
    root = post_order[post_right]
    in_root = pos[root]
    print(root, end=' ')
    post_left_len = in_root - in_left
    post_right_start = post_left + post_left_len
    pre(in_left, in_root - 1, post_left, post_left + post_left_len - 1)
    pre(in_root + 1, in_right, post_right_start, post_right - 1)


n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
pos = [0] * (n + 1)

for i in range(n):
    pos[in_order[i]] = i

pre(0, n - 1, 0, n - 1)

'''
15
8 7 9 2 10 6 11 1 12 5 13 3 14 4 5
8 9 7 10 11 6 2 12 13 5 14 15 4 3 1
'''