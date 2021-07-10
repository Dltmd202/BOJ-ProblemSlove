

def fail(pattern):
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


n = int(input())
s = input()
table = fail(s)
print(table)
print(len(s) - table[-1])