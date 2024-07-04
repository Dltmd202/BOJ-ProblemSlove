if __name__ == '__main__':
    s = input()
    t = input()

    def serach(a):
        if len(a) == len(s):
            return a == s

        if a[-1] == 'A' and serach(a[:-1]):
            return True

        if a[::-1][-1] == 'B' and serach(a[::-1][:-1]):
            return True

        return False

    print(1 if serach(t) else 0)
