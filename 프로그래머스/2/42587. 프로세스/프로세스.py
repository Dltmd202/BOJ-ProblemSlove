from collections import deque

def solution(priorities, location):
    q = deque((i, j) for i, j in enumerate(priorities))
    answer = []
    
    while q:
        process = q.popleft()
        if q and any(process[1] < item[1] for item in q):
            q.append(process)
        else:
            answer.append(process)
        
    for i in range(len(answer)):
        if answer[i][0] == location:
            return i + 1