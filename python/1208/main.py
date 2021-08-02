from itertools import combinations
from collections import Counter
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
data = list(map(int, input().split()))
pivot = n // 2
left, right = data[:pivot], data[pivot:]
left_sum, right_sum = [], []

for i in range(pivot + 2):
    if i <= len(left):
        for com in combinations(left, r=i):
            left_sum.append(sum(com))
    if i <= len(right):
        for com in combinations(right, r=i):
            right_sum.append(sum(com))

left_sum.sort()
right_sum.sort(reverse=True)
left_idx, right_idx = 0, 0
left_len, right_len = len(left_sum), len(right_sum)
left_counter, right_counter = Counter(left_sum), Counter(right_sum)
res = 0

while left_idx < left_len and right_idx < right_len:
    if left_sum[left_idx] + right_sum[right_idx] == s:
        left_duplicated = left_counter[left_sum[left_idx]]
        right_duplicated = right_counter[right_sum[right_idx]]
        res += (left_duplicated * right_duplicated)
        left_idx += left_duplicated
        right_idx += right_duplicated
    elif left_sum[left_idx] + right_sum[right_idx] < s:
        left_idx += 1
    elif left_sum[left_idx] + right_sum[right_idx] > s:
        right_idx += 1

print(res - 1 if s == 0 else res)