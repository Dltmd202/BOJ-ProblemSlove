import sys
input = sys.stdin.readline
q = int(input())
data = set()


def use_set():
    for qc in range(q):
        query = list(input().split())
        if query[0] == 'add':
            data.add(int(query[1]))
        elif query[0] == 'remove':
            try:
                data.remove(int(query[1]))
            except:
                pass
        elif query[0] == 'check':
            if int(query[1]) in data:
                print(1)
            else:
                print(0)
        elif query[0] == 'toggle':
            if int(query[1]) in data:
                data.remove(int(query[1]))
            else:
                data.add(int(query[1]))
        elif query[0] == 'all':
            data = set(range(1, 21))
        elif query[0] == 'empty':
            data = set()



