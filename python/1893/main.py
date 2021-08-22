import sys
input = sys.stdin.readline

n = int(input())

answer = [[] for _ in range(n)]
ans_str = [[] for _ in range(n)]


def get_table(pattern):
    length = len(pattern)
    table = [0] * length
    j = 0
    for i in range(1, length):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table


def kmp(parent, pattern):
    length = len(parent)
    pattern_size = len(pattern)
    table = get_table(pattern)
    j = 0
    cnt = 0
    result = False
    for i in range(length):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j - 1]
        if parent[i] == pattern[j]:
            if j == pattern_size - 1:
                if result:
                    return False
                result = True
                cnt += 1
                j = table[j]
            else:
                j += 1
    return result


for tb in range(n):
    a = sys.stdin.readline()
    w = sys.stdin.readline()
    s = sys.stdin.readline()

    conv = dict()
    for i in range(len(a)):
        conv[a[i]] = a[(i + 1) % len(a)]

    for shift in range(len(a)):
        if shift != 0:
            ret = ''
            for j in range(len(w)):
                ret += conv[w[j]]
            w = ret
        result = kmp(s, w)
        if result:
            answer[tb].append(shift)

for ans in answer:
    if not ans:
        print("no solution")
    elif len(ans) == 1:
        print("unique:", ans[0])
    else:
        print("ambiguous: ",end='')
        for a in ans:
            print(a, end=' ')
        print()