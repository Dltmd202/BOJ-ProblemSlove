import heapq
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    pq = []

    answer = []
    for _ in range(n):
        d = int(input())

        if d == 0:
            if not pq:
                answer.append(0)
            else:
                answer.append(heapq.heappop(pq))
        else:
            heapq.heappush(pq, d)

    print('\n'.join(map(str, answer)))