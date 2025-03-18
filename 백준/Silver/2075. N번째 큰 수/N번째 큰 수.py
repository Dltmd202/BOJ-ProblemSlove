import heapq

if __name__ == '__main__':
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    pqs = []

    for d in zip(*data):
        pqs.append(list(map(lambda x: -x, d)))

    for pq in pqs:
        heapq.heapify(pq)
    answer = 0
    for _ in range(n):
        max_pq = []
        max_val = -int(1e11)
        for pq in pqs:
            if len(pq) == 0:
                continue
            if max_val < -pq[0]:
                max_val = -pq[0]
                max_pq = pq

        answer = -heapq.heappop(max_pq)
    print(answer)
