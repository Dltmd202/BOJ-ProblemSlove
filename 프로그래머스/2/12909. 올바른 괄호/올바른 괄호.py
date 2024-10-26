def solution(s):
    answer = True
    stack = []
    
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False

    return len(stack) == 0