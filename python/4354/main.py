
def failure(pattern):
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


while True:
    s = input()
    if s == '.':
        break

    table = failure(s)
    if len(s) % (len(s) - table[-1]) == 0:
        print(len(s) // (len(s) - table[-1]))
    else:
        print(1)


