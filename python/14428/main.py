import sys
INF = sys.maxsize
input = sys.stdin.readline


class Node:

    def __str__(self):
        return f'<{self.start} {self.end} {self.data}>'

    def __init__(self, start, end):
        self.start, self.end = start, end
        self._left = self._right = None
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
        self._right = self._right or Node(self.mid + 1, self.end)
        return self._right

    def update(self, i):
        if self.start > i or i > self.end:
            return self.data
        if not self.start == self.end:
            left_ = self.left.update(i)
            right_ = self.right.update(i)
            if data[left_] < data[right_]:
                self.data = left_
            elif data[left_] > data[right_]:
                self.data = right_
            else:
                self.data = min(left_, right_)
            return self.data
        else:
            self.data = i
            return self.data

    def query(self, left, right):
        if left <= self.start and self.end <= right:
            return self.data
        if self.start > right or self.end < left:
            return 0
        left_ = self.left.query(left, right)
        right_ = self.right.query(left, right)
        if data[left_] > data[right_]:
            return right_
        if data[left_] < data[right_]:
            return left_
        else:
            return left_ if left_ < right_ else right_


n = int(input())
data = [INF] + list(map(int, input().split()))
tree = Node(1, n)
for i in range(1, n + 1):
    tree.update(i)
m = int(input())
for i in range(m):
    order, a, b = map(int, input().split())
    if order == 2:
        res = tree.query(a, b)
        print(res)
    else:
        data[a] = b
        tree.update(a)