if __name__ == '__main__':
    N = int(input())
    data = list(map(int, input().split()))
    M = int(input())

    left, right = 0, max(data)
    answer = 0

    def is_valid(target):
        tmp = list(filter(lambda x: x < target, data))
        res = sum(tmp)
        res += target * (len(data) - len(tmp))
        return res <= M

    while left <= right:
        mid = (left + right) // 2

        if is_valid(mid):
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1

    print(answer)

