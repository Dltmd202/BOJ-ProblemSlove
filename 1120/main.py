
a, b = input().split()
min_value = 100

for i in range(len(b) - len(a)+1):
    diff = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            diff += 1
    min_value = min(min_value, diff)

print(min_value)
