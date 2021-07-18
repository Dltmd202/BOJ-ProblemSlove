import heapq
import sys
input = sys.stdin.readline
t = int(input())

for tb in range(t):
    n = int(input())
    min_q = []
    max_q = []
    left, right = 0, 0
    visited = dict()
    for i in range(n):
        query = list(input().split())
        if query[0] == 'I':
            heapq.heappush(min_q, (int(query[1]), i))
            heapq.heappush(max_q, (-int(query[1]), i))
            visited[i] = False
        else:
            if int(query[1]) == -1:
                while min_q and visited[min_q[0][1]]:
                    heapq.heappop(min_q)
                if min_q:
                    visited[min_q[0][1]] = True
                    heapq.heappop(min_q)
            else:
                while max_q and visited[max_q[0][1]]:
                    heapq.heappop(max_q)
                if max_q:
                    visited[max_q[0][1]] = True
                    heapq.heappop(max_q)
    while min_q and visited[min_q[0][1]]:
        heapq.heappop(min_q)
    while max_q and visited[max_q[0][1]]:
        heapq.heappop(max_q)
    if min_q and max_q:
        print(-max_q[0][0], min_q[0][0])
    else:
        print('EMPTY')