from collections import defaultdict
import sys
input = sys.stdin.readline


class Node:
    def __init__(self, data=False):
        self.children = defaultdict(Node)
        self.data = data


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, strings):
        node = self.root

        for s in strings:
            node = node.children[s]
        node.data = True

    def search(self):
        self.dfs(self.root, 0)

    def dfs(self, node, depth):
        for child in sorted(node.children):
            print("--" * depth + child)
            self.dfs(node.children[child], depth + 1)


n = int(input())
trie = Trie()
for i in range(n):
    depth, *args = input().split()
    trie.insert(args)

trie.search()
