import heapq


capacity = []
n = int(input())
caps = list(map(int, input().split()))
caps.sort()

m = int(input())
boxes = list(map(int, input().split()))
boxes.sort()
answer = 0

max_idx = n - 1
result = True
capacity.append([0, caps[max_idx]])
while boxes:
    box = boxes.pop()
    if box > max(caps):
        result = False
        break
    while max_idx > 0 and caps[max_idx - 1] >= box:
        max_idx -= 1
        capacity.append([0, caps[max_idx]])
    capacity.sort(key=lambda x: x[0])
    capacity[0][0] += 1
    answer = max(answer, capacity[0][0])

if result:
    print(answer)
else:
    print(-1)
