from collections import deque, defaultdict


class Solution:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        self.MAX = int(1e5)
        self.dx = [lambda x: x + 1, lambda x: x - 1, lambda x: x*2]
        self.time = 0
        self.answer = 0

    def solution(self):
        q = deque()
        q.append([0, self.n])
        visited = defaultdict(
            lambda: {"is_visited": False, "time": 0, "cnt": 0}
        )
        visited[self.n]["is_visited"] = True
        visited[self.n]["time"] = 0
        visited[self.n]["cnt"] = 1
        while q:
            t, n = q.popleft()
            if visited[self.k]["is_visited"] and visited[self.k]["time"] < t:
                break
            for i in range(3):
                nn = self.dx[i](n)
                if 0 <= nn <= self.MAX:
                    if not visited[nn]["is_visited"]:
                        q.append([t + 1, nn])
                        visited[nn]["is_visited"] = True
                        visited[nn]["time"] = t + 1
                        visited[nn]["cnt"] = visited[n]["cnt"]
                    elif visited[nn]["time"] == t + 1:
                        visited[nn]["cnt"] += visited[n]["cnt"]
        print(visited[self.k]["time"])
        print(visited[self.k]["cnt"])


if __name__ == "__main__":
    s = Solution()
    s.solution()
