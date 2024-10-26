def solution(prices):
    answer = [i for i in range(len(prices) - 1, -1, -1)]
    stack = []
    
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)
    
    
    return answer