
n, k = map(int, input().split())
data = list(map(int, ' '.join(str(num) for num in input()).split()))
stack = []
length = n - k

for i in range(len(data)):
    while k > 0 and stack and stack[-1] < data[i]:
        stack.pop()
        k -= 1
    stack.append(data[i])
print(''.join(str(num) for num in stack[: length]))
