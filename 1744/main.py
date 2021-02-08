import sys
input = sys.stdin.readline

n = int(input())


positives = []
negatives = []
left = []

for i in range(n):
    a = int(input())
    if a > 1:
        positives.append(a)
    elif a < 0:
        negatives.append(a)
    else:
        left.append(a)
positives.sort(reverse=True)
result = 0

for i in range(0, len(positives) - 1, 2):
    result += (positives[i] * positives[i + 1])
if len(positives) % 2:
    result += positives[-1]
negatives.sort()
for i in range(0, len(negatives) - 1, 2):
    result += (negatives[i] * negatives[i + 1])
if len(negatives) % 2:
    if 0 not in left:
        result += negatives[-1]
result += sum(left)

print(result)

