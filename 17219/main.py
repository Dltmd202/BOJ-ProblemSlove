import sys
input = sys.stdin.readline
n, m = map(int, input().split())
accounts = dict()

for i in range(n):
    ids, p = (input().rstrip()).split()
    accounts[ids] = p

for j in range(m):
    ids = input().rstrip()
    print(accounts[ids])