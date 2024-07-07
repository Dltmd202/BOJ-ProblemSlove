from itertools import combinations, product
from bisect import bisect_left, bisect_right

def solution(dices):
    counter = {}
    L = len(dices)
    
    data = [3, 5, 8, 10, 15]
    print(bisect_right(data, 6))
    
    
    for a_indeies in combinations(range(L), L // 2):
        b_indeies = tuple(set(range(L)) - set(a_indeies))
        
        a, b = [], []
        for order in product(range(6), repeat=L//2):
            # print(a_indeies)
            a.append(sum(dices[i][j] for i, j in zip(a_indeies, order)))
            b.append(sum(dices[i][j] for i, j in zip(b_indeies, order)))
        b.sort()
        
        
        wins = sum(bisect_left(b, num) for num in a)
        counter[wins] = list(a_indeies)
    
    
    max_key = max(counter.keys())
    return [x + 1 for x in counter[max_key]]