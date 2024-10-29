import heapq
from collections import deque
import math

def solution(jobs):
    answer = 0
    pq = []
    time = 0
    wait_time = 0
    process_count = 0
    jobs_length = len(jobs)
    jobs.sort(key=lambda x: (x[0], x[1]))
    jobs = deque(jobs)
    
    # (start_time, running_time) = jobs.popleft()
    # pq.append((running_time, start_time))
    
    while process_count < jobs_length:
        while jobs and jobs[0][0] <= time:
            (start_time, running_time) = jobs.popleft()
            heapq.heappush(pq, (running_time, start_time))
            
        if pq:
            (running_time, start_time) = heapq.heappop(pq)
            time += running_time
            wait_time += (time - start_time)
            process_count += 1
        else:
            time = jobs[0][0]
            
    return math.floor(wait_time / jobs_length)
