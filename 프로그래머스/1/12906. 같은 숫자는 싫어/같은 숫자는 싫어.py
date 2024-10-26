def solution(arr):
    stack = []
    
    for data in arr:
        if stack and data == stack[-1]:
            continue
        stack.append(data)
        
    return stack