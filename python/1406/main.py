import sys
input = sys.stdin.readline

left = list(input().strip())
right = []
for _ in range(int(input())):
    order, *args = input().strip().split()
    if order == 'L':
        if left:
            right.append(left.pop())
    elif order == 'D':
        if right:
            left.append(right.pop())
    elif order == 'B':
        if left:
            left.pop()
    elif order == 'P':
        left.append(args[0])
print(''.join(left + list(reversed(right))))
