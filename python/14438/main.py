import sys
INF = sys.maxsize
input = sys.stdin.readline


class Node:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self._left = self._right = None
        self.data = 0

    def __str__(self):
        return f'<{self.start} {self.end} {self.data}>'

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def left(self):
        self._left = self._left or Node(self.start, self.mid)
        return self._left

    @property
    def right(self):
        self._right = self._right or Node(self.mid + 1, self.end)
        return self._right

    def update(self, idx, d):
        if self.end < idx or idx < self.start:
            return self.data
        if self.start == self.end:
            self.data = d
            return self.data
        left_ = self.left.update(idx, d)
        right_ = self.right.update(idx, d)
        self.data = min(left_, right_)
        return self.data

    def query(self, left, right):
        if left <= self.start and self.end <= right:
            return self.data
        if self.end < left or right < self.start:
            return INF
        left_ = self.left.query(left, right)
        right_ = self.right.query(left, right)
        return min(left_, right_)


if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    m = int(input())
    tree = Node(1, n)
    for i, d in enumerate(data):
        tree.update(i + 1, d)
    for _ in range(m):
        action, a, b = map(int, input().split())
        if action == 2:
            print(tree.query(a, b))
        else:
            tree.update(a, b)

