import heapq
from collections import defaultdict

def solution(ops):
    answer = []
    max_heap = []
    max_dict = defaultdict(int)
    min_heap = []
    min_dict = defaultdict(int)
    cnt = 0
    
    for op in ops:
        order, val = op.split(' ')
        
        if order == 'I':
            heapq.heappush(max_heap, -int(val))
            heapq.heappush(min_heap, int(val))
            cnt += 1
        
        elif order == 'D' and val == '1':
            while max_heap:
                rm = -heapq.heappop(max_heap)
                if min_dict[rm] > 0:
                    min_dict[rm] -= 1
                    continue
                else:
                    max_dict[rm] += 1
                    cnt -= 1
                    break
            
        
        elif order == 'D' and val == '-1':
            while min_heap:
                rm = heapq.heappop(min_heap)
                if max_dict[rm] != 0:
                    max_dict[rm] -= 1
                    continue
                else:
                    min_dict[rm] += 1
                    cnt -= 1
                    break
    
    if cnt > 0:
        max_val, min_val = 0, 0
        while max_heap:
            rm = -heapq.heappop(max_heap)
            if min_dict[rm] > 0:
                min_dict[rm] -= 1
                continue
            else:
                max_val = rm
                break
        
        while min_heap:
            rm = heapq.heappop(min_heap)
            if max_dict[rm] != 0:
                max_dict[rm] -= 1
                continue
            else:
                min_val = rm
                break
        
        
        return [max_val, min_val]
    return [0, 0]