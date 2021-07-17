import sys
input = sys.stdin.readline
n, m = map(int, input().split())
names = ['']
dictionary = dict()
for i in range(1, n + 1):
    name = input().rstrip()
    dictionary[str(i)] = name
    dictionary[name] = i
for i in range(m):
    query = input().rstrip()
    print(dictionary[query])
