from collections import defaultdict

def solution(genres, plays):
    answer = []
    ge_count = defaultdict(int)
    ge_list = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        ge_count[g] += p
        ge_list[g].append((i, p))
    
    # print(sorted(ge_count.items(), key=lambda x: -x[1]))
    
    for k, v in sorted(ge_count.items(), key=lambda x: -x[1]):
        ge_music = ge_list[k]
        ge_music.sort(key=lambda x: (-x[1], x[0]))
        answer.extend(map(lambda x: x[0], ge_music[:2]))
    
    # print(answer)

    
    return answer