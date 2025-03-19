from collections import Counter

if __name__ == '__main__':
    n, k = map(int, input().split())
    data = list(map(int, input().split()))


    def solution():
        if n < 2:
            return len(data)

        left, right = 0, 0
        counter = Counter()
        answer = 0

        while right < n:
            if counter[data[right]] >= k:
                counter[data[left]] -= 1
                left += 1
            else:
                counter[data[right]] += 1
                right += 1
                answer = max(answer, right - left)
        return answer

    print(solution())