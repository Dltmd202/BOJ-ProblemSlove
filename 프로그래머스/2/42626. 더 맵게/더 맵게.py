import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    cnt = 0
    
    if scoville and scoville[0] >= K:
        return 0
    
    while len(scoville) >= 2:
        cnt += 1
        a, b = heapq.heappop(scoville), heapq.heappop(scoville)
        c = a + (b * 2)
        heapq.heappush(scoville, c)
        
        if scoville[0] >= K:
            return cnt
    
    if scoville and scoville[0] >= K:
        return cnt + 1
    
    return -1