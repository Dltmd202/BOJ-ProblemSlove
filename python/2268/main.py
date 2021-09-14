import sys
input = sys.stdin.readline


class Node:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self._left, self._right = None, None
        self.data = 0

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def left(self):
        self._left = self._left or Node(self.start, self.mid)
        return self._left

    @property
    def right(self):
        self._right = self._right or Node(self.mid +  1, self.end)
        return self._right

    def query(self, left, right):
        if left <= self.start and self.end <= right:
            return self.data
        if self.end < left or right < self.start:
            return 0
        left_ = self.left.query(left, right)
        right_ = self.right.query(left, right)
        return left_ + right_

    def update(self, idx, diff):
        if idx < self.start or self.end < idx:
            return
        self.data += diff
        if not self.start == self.end:
            self.left.update(idx, diff)
            self.right.update(idx, diff)


n, m = map(int, input().split())
tree = Node(1, n)
data = [0] * (n + 1)
for i in range(m):
    order, *args = map(int, input().split())
    if order == 0:
        print(tree.query(args[0], args[1]))
    elif order == 1 and data[args[0]] != args[1]:
        diff = args[1] - data[args[0]]
        tree.update(idx=args[0], diff=diff)
        data[args[0]] = args[1]