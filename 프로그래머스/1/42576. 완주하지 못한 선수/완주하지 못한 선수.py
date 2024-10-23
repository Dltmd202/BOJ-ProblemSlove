from collections import defaultdict

def solution(participant, completion):
    answer = ''
    
    pt_map = defaultdict(int)
    for p in participant:
        pt_map[p] += 1
    
    for c in completion:
        pt_map[c] -= 1
    
    for p in participant:
        if pt_map[p] != 0:
            return p