from collections import deque, defaultdict
import sys
input = sys.stdin.readline
t = int(input())

for tb in range(t):
    origin, target = map(int, input().split())

    def D(n):
        return (2 * n) % 10000

    def S(n):
        if n == 0:
            return 9999
        else:
            return n - 1

    def L(n):
        d = str(n)
        return int(n % 1000 * 10 + n / 1000)

    def R(n):
        d = str(n)
        return int(n % 10 * 1000 + n // 10)

    def search():
        q = deque()
        visited = [False] * (10000)
        q.append(['', origin])
        while q:
            res, now = q.popleft()
            if now == target:
                return res
            will = D(now)
            if not visited[will]:
                visited[will] = True
                q.append([res + 'D', will])
            will = S(now)
            if not visited[will]:
                visited[will] = True
                q.append([res + 'S', will])
            will = L(now)
            if not visited[will]:
                visited[will] = True
                q.append([res + 'L', will])
            will = R(now)
            if not visited[will]:
                visited[will] = True
                q.append([res + 'R', will])


    print(search())