from collections import Counter, defaultdict
from itertools import combinations

def solution(dice):
    answer = []
    total_cnt = len(dice)
    counter = Counter()
    
    for d in dice:
        d.sort()
    
    memo = defaultdict(Counter)


    def search(counter, cur, idx):
        if tuple(cur) in memo:
            counter += memo[tuple(cur)]
            return
            
        if idx == len(dice):
            this_counter = Counter()
            for c in combinations(list(enumerate(cur)), len(dice) // 2):
                def get_my_score(c):
                    score = 0
                    for i, s in c:
                        score += s
                    return score

                def get_this_id(c):
                    ids = []
                    for i, s in c:
                        ids.append(i)
                    return tuple(ids)
                
                total_sum = sum(cur)
                my_score = get_my_score(c)
                other_score = total_sum - my_score

                if my_score > other_score:
                    this_counter[get_this_id(c)] += 1
            counter += this_counter
            memo[tuple(cur)] = this_counter
            return
        
        for target in dice[idx]:
            cur.append(target)
            search(counter, cur, idx + 1)
            cur.pop()
    
    search(counter, [], 0)
    return list(map(lambda x: x + 1, counter.most_common()[0][0]))
