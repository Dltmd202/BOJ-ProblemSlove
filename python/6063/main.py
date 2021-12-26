from itertools import combinations

while True:
    data = list(map(int,input().split()))
    if data[0] == 0:
        break

    for combination in combinations(data[1:], 6):
        for a in combination:
            print(a, end=' ')
        print()
    print()
