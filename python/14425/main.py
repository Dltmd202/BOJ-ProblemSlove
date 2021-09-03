from collections import defaultdict
import sys
input = sys.stdin.readline


class TrieNode:
    def __init__(self, key, data=None):
        self.children = defaultdict(str)
        self.key = key
        self.data = data


class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, string):
        curr_node = self.root

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode(char)
            curr_node = curr_node.children[char]
        curr_node.data = string

    def search(self, string):
        curr_node = self.root

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        if curr_node.data:
            return True
        return False


n, m = map(int, input().split())
trie = Trie()
cnt = 0
for i in range(n + m):
    string = input().strip()
    if i < n:
        trie.insert(string)
    else:
        if trie.search(string):
            cnt += 1
print(cnt)

