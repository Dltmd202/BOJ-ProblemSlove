if __name__ == '__main__':
    s = list(input())

    left_1 = s.count('1') // 2
    left_0 = s.count('0') // 2

    for i in range(len(s)):
        if s[i] == '1' and left_1 > 0:
            s[i] = ''
            left_1 -= 1

    for i in range(len(s) - 1, -1, -1):
        if s[i] == '0' and left_0 > 0:
            s[i] = ''
            left_0 -= 1
    print(''.join(s))
