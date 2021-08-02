
from collections import defaultdict, Counter

def solution():

    n, m = map(int, input().split())
    data = []
    dataset = defaultdict(int)
    cnt = 0
    study = set()

    for i in range(n):
        s = input()
        data.append(s)

    if m < 5:
        return cnt

    for word in data:
        for w in word:
            dataset[w] += 1
    teach = Counter(dataset).most_common(m)
    
    for i in teach:
        study.add(i[0])

    for i in range(n):
        if study.issubset(set(data[i])):
            cnt += 1
    return cnt

print(solution())