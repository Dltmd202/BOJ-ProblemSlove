from collections import defaultdict
import sys
input = sys.stdin.readline

trees = dict()
total = 0

while True:
    tree = input().strip()
    if not tree:
        break
    if not tree in trees:
        trees[tree] = 0
    trees[tree] += 1
    total += 1

for tree, cnt in sorted(trees.items()):
    print(f"{tree} {format(cnt / total * 100, '0.4f')}")
