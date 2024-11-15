from heapq import heappush, heappop

if __name__ == '__main__':
    n = int(input())
    data = [int(input()) for _ in range(n)]

    def solution(data):
        if len(data) == 1:
            return [data[0]]

        answer = []
        min_pq, max_pq = [], []

        for d in data:
            if not max_pq:
                heappush(max_pq, (-d, d))
            elif max_pq[0][1] < d:
                if len(max_pq) > len(min_pq):
                    heappush(min_pq, (d, d))
                else:
                    heappush(min_pq, (d, d))
                    val = heappop(min_pq)
                    heappush(max_pq, (-val[1], val[1]))
            else:
                if len(min_pq) >= len(max_pq):
                    heappush(max_pq, (-d, d))
                else:
                    heappush(max_pq, (-d, d))
                    val = heappop(max_pq)
                    heappush(min_pq, (val[1], val[1]))

            answer.append(max_pq[0][1])

        return answer

    print(*solution(data), sep='\n')

