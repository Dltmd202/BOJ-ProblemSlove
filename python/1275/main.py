import sys
input = sys.stdin.readline


class Node:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self._left = None
        self._right = None
        self.data = 0

    @property
    def left(self):
        self._left = self._left or Node(self.start, self.mid)
        return self._left

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def right(self):
        self._right = self._right or Node(self.mid + 1, self.end)
        return self._right

    def update(self, idx, diff):
        if idx < self.start or self.end < idx:
            return

        self.data += diff
        if not self.start == self.end:
            self.left.update(idx, diff)
            self.right.update(idx, diff)

    def query(self, left, right):
        if right < self.start or left > self.end:
            return 0
        if left <= self.start and self.end <= right:
            return self.data

        left_res = self.left.query(left, right)
        right_res = self.right.query(left, right)
        return left_res + right_res


n, q = map(int, input().split())
tree = Node(1, n)
data = [0] + list(map(int, input().split()))
for i, d in enumerate(data):
    tree.update(i, d)
for _ in range(q):
    x, y, a, b = map(int, input().split())
    res = tree.query(min(x, y), max(x, y))
    print(res)
    diff = b - data[a]
    data[a] = b
    tree.update(a, diff)
