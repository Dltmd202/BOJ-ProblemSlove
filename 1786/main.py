
idx =[]


def make_table(pattern):
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
    cnt = 0
    parent_size = len(parent)
    pattern_size = len(pattern)
    table = make_table(pattern)
    j = 0
    for i in range(parent_size):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j - 1]
        if parent[i] == pattern[j]:
            if j == pattern_size - 1:
                j = table[j]
                cnt += 1
                idx.append(i)
            else:
                j += 1
    return cnt

parent = input()
pattern = input()
print(kmp(parent, pattern))