from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize


class Node:
    def __str__(self):
        return f'{self.start} {self.end} {self.data}'

    def __init__(self, start, end):
        self.start, self.end = start, end
        self._right = self._left = None
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

    def update(self, idx):
        if idx < self.start or self.end < idx:
            return self.data
        if not self.start == self.end:
            left_ = self.left.update(idx)
            right_ = self.right.update(idx)
            res = 0
            if data[left_] < data[right_]:
                self.data = left_
            elif data[left_] > data[right_]:
                self.data = right_
            else:
                self.data = min(left_, right_)
            return self.data
        else:
            self.data = idx
            return self.data

    def query(self):
        return self.data


n = int(input())
data = [INF] + list(map(int, input().split()))
indexes = defaultdict(list)
tree = Node(1, n)
for i, d in enumerate(data):
    indexes[d] = 1
    tree.update(i)
m = int(input())
for i in range(m):
    order, *args = map(int, input().split())
    if order == 2:
        print(tree.query())
    else:
        data[args[0]] = args[1]
        tree.update(args[0])
