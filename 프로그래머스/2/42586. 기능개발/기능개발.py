import math

def solution(progresses, speeds):
    answer = []
    stack = []
    
    for p, s in zip(progresses, speeds):
        date = math.ceil((100 - p) / s)
        
        if not stack:
            stack.append([date, 1])
        else:
            if stack[-1][0] >= date:
                stack[-1][1] += 1
            else:
                stack.append([date, 1])
                
    print(list(map(lambda x: x[1], stack)))
    return list(map(lambda x: x[1], stack))